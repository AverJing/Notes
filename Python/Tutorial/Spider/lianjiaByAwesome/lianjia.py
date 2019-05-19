# -*- coding: utf-8 -*-
import requests
from concurrent.futures import ThreadPoolExecutor
from pyquery import PyQuery as pq
import json
import threading
import time
import pymongo
import random
from conversion import getlnglat

f = open('./city_ershoufang_urls.json', 'r')
ershoufang_urls = json.load(f)

cityName = '苏州'

def get_list_page_url(city):
    page_url_list = list()
    try:
        start_url = ershoufang_urls[city]
    except:
        return page_url_list
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }

    for e_url in start_url:
        try:
            response = requests.get(e_url, headers=headers)
            # print(response.status_code, response.text)
            doc = pq(response.text)
            total_num = int(doc(".resultDes .total span").text())
            total_page = total_num // 30 + 1
            # 只能访问到前一百页
            if total_page > 100:
                total_page = 100

            for i in range(total_page):
                url = e_url + "/pg" + str(i + 1) + "/"
                page_url_list.append(url)
                # print(url)
        except:
            print("获取总套数出错,请确认起始URL是否正确")
            print(e_url)
            continue
    return page_url_list

detail_list = list()


# 需要先在本地开启代理池
# 代理池仓库: https://github.com/Python3WebSpider/ProxyPool
def get_valid_ip():
    url = "http://localhost:5000/get"
    try:
        ip = requests.get(url).text
        return ip
    except:
        print("请先运行代理池")


def get_detail_page_url(page_url):
    global detail_list
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'https://bj.lianjia.com/ershoufang'
    }

    try:
        response = requests.get(page_url, headers=headers, timeout=3)
        doc = pq(response.text)
        # broswer.get(page_url)
        # print(page_url)
        # doc = pq(broswer.page_source)
        i = 0
        detail_urls = list()
        for item in doc(".sellListContent li").items():
            i += 1
            if i == 31:
                break
            child_item = item(".noresultRecommend")
            if child_item == None:
                i -= 1
            detail_url = child_item.attr("href")
            detail_urls.append(detail_url)
        return detail_urls
    except:
        print("获取列表页" + page_url + "出错")


lock = threading.Lock()


def detail_page_parser(res):
    global detail_list
    detail_urls = res.result()
    if not detail_urls:
        print("detail url 为空")
        return None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'https://bj.lianjia.com/ershoufang'
    }
    for detail_url in detail_urls:
        try:
            response = requests.get(url=detail_url, headers=headers, timeout=3)
            # print(response.status_code)
            detail_dict = dict()
            doc = pq(response.text)
            unit_price = doc(".unitPriceValue").text()
            unit_price = unit_price[0:unit_price.index("元")]
            title = doc("h1").text()
            area = doc(".areaName .info a").eq(0).text().strip()
            communityName = doc('.communityName .info').text()
            detail_dict["title"] = title
            detail_dict["area"] = area
            detail_dict["price"] = unit_price
            detail_dict["communityName"] = communityName
            lng_lat_result = getlnglat(cityName+area+communityName)
            if lng_lat_result['status'] == 0:
                detail_dict['lng'] = lng_lat_result['result']['location']['lng']
                detail_dict['lat'] = lng_lat_result['result']['location']['lat']
            else:
                detail_dict['lng'] = '暂无'
                detail_dict['lat'] = '暂无'
            
            s = doc('.base .content li').items()           
            for item in s:
                name = item('span').text()
                detail_dict[name] = item.remove('span').text()
            detail_list.append(detail_dict)

            print(unit_price, title, area)

        except:
            print("获取详情页出错,换ip重试")
            proxies = {
                "http": "http://" + get_valid_ip(),
            }
            try:
                response = requests.get(url=detail_url, headers=headers, proxies=proxies)
                # print(response.status_code)
                detail_dict = dict()
                doc = pq(response.text)
                unit_price = doc(".unitPriceValue").text()
                unit_price = unit_price[0:unit_price.index("元")]
                title = doc("h1").text()
                area = doc(".areaName .info a").eq(0).text().strip()
                communityName = doc('.communityName .info').text()
                detail_dict["name"] = title
                detail_dict["district_main"] = area
                detail_dict["main_price"] = unit_price
                detail_dict["communityName"] = communityName
                lng_lat_result = getlnglat(cityName+area+communityName)
                if lng_lat_result['status'] == 0:
                    detail_dict['lng'] = lng_lat_result['result']['location']['lng']
                    detail_dict['lat'] = lng_lat_result['result']['location']['lat']
                else:
                    detail_dict['lng'] = '暂无'
                    detail_dict['lat'] = '暂无'
                
                s = doc('.base .content li').items()           
                for item in s:
                    name = item('span').text()
                    detail_dict[name] = item.remove('span').text()
                detail_list.append(detail_dict)

                print(unit_price, title, area)
            except:
                print("重试失败...")


def save_data(data, filename):
    with open(filename + ".json", 'w', encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))

def main():
	# cq,cs,nj,dl,wh,cc
    global cityName
    city_list = ['佛山', '中山']
    city_name_pinyin = ['foshan','zhongshan']
    conn = pymongo.MongoClient(host='localhost', port=27017)
    lianjia = conn['lianjia']

    for index in range(len(city_list)):  
        print(city_list[index]+city_name_pinyin[index])    
        cityName = city_list[index]
        page_url_list = get_list_page_url(cityName)
        if page_url_list:
            data = lianjia[city_name_pinyin[index] + '_ershoufang']
            # pool = threadpool.ThreadPool(20)
            # requests = threadpool.makeRequests(page_and_detail_parser, page_url_list)
            # [pool.putRequest(req) for req in requests]
            # pool.wait()
            
            p = ThreadPoolExecutor(30)
            
            for page_url in page_url_list:
                p.submit(get_detail_page_url, page_url).add_done_callback(detail_page_parser)
            # 这里的回调函数拿到的是一个对象。
            # 先把返回的res得到一个结果。即在前面加上一个res.result(),这个结果就是get_detail_page_url的返回
            p.shutdown()
            #print(detail_list)
            
            #save_data(detail_list, city)
            data.insert(detail_list)
            
            detail_list.clear()
            time.sleep(random.randint(5,10))


if __name__ == '__main__':
	old = time.time()
	main()
	new = time.time()
	delta_time = new - old
	print("程序共运行{}s".format(delta_time))