import json
import requests
from bs4 import BeautifulSoup
import os
import time
import random
import pymongo
from conversion import getlnglat


f = open('./city_urls.json', 'r')
data = json.load(f)

def isNone(result):
    if result is None:
        return '暂无'
    else:
        return result

# 爬取信息
def GetInfo(tmp, page_num=10,name='suzhou',city_name='苏州'):
    conn = pymongo.MongoClient(host='localhost', port=27017)
    lianjia = conn['lianjia']
    suzhou = lianjia[name]

    print('[INFO]:Start to get infos...')
    headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	}
    infos = []
    for i in range(0, page_num):
        url = tmp + 'pg{}/'.format(i+1)
        res = requests.get(url, headers=headers)
        if 400 <= res.status_code < 600:
            break
        soup = BeautifulSoup(res.text, 'lxml')
        resblocks = soup.find_all('div', attrs={'class': 'resblock-name'})
        resblocks_area = soup.find_all('div', attrs={'class': 'resblock-area'})
        resblocks_location = soup.find_all('div', attrs={'class': 'resblock-location'})
        resblocks_price = soup.find_all('div', attrs={'class': 'resblock-price'})
        assert len(resblocks) == len(resblocks_area); assert len(resblocks) == len(resblocks_location); assert len(resblocks) == len(resblocks_price)
        info_num = len(resblocks)
        for k in range(info_num):
            resblock_price = resblocks_price[k]
            if resblock_price.find('span', attrs={'class': 'desc'}) is None or resblock_price.find('span', attrs={'class': 'desc'}).string.strip() == '万/套(均价)':
            	main_price = '暂无'
            else:
            	main_price = resblock_price.find('span', attrs={'class': 'number'}).string.strip()
            if resblock_price.find('div', attrs={'class': 'second'}) is None:
                second_price =  '暂无'
            else:
                second_price = resblock_price.find('div', attrs={'class': 'second'}).string.strip()
            resblock_location = resblocks_location[k]
            resblock_locationAll = resblock_location.find_all('span')
            location1 = resblock_locationAll[0].string.strip()
            location2 = resblock_locationAll[1].string.strip()
            location3 = isNone(resblock_location.find('a').string).strip().split(',')[0]
            resblock_area = resblocks_area[k]
            if resblock_area.find('span').string is None:
                area = '暂无'
            else:
                area = resblock_area.find('span').string.strip().split(' ')[1][:-2]
            resblock = resblocks[k]
            resblock_name = isNone(resblock.find('a').string).strip()
            resblock_type = isNone(resblock.find('span', attrs={'class': 'resblock-type'}).string).strip()
            resblock_status = isNone(resblock.find('span', attrs={'class': 'sale-status'}).string).strip()
            lng_lat_result = getlnglat(city_name+location1+location2+location3)
            if lng_lat_result['status'] == 0:
                data={
                'name':resblock_name,
                'district_main':location1,
                'district_second':location2,
                'location':location3,
                'status':resblock_type + '-' + resblock_status,
                'main_price':main_price,
                'second_price':second_price,
                'area':area,
                'lng':lng_lat_result['result']['location']['lng'],
                'lat':lng_lat_result['result']['location']['lat']
            }
            else:
                data={
                'name':resblock_name,
                'district_main':location1,
                'district_second':location2,
                'location':location3,
                'status':resblock_type + '-' + resblock_status,
                'main_price':main_price,
                'second_price':second_price,
                'area':area,
                'lng':'暂无',
                'lat':'暂无'
            }
            
            suzhou.insert_one(data)
        print("%d is ok" %(i+1))
        time.sleep(random.randint(5,10))
    return infos

def test(tmp):
    print('[INFO]:Start to get infos...')
    headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	}
    for i in range(1):
        url = tmp + 'pg{}/'.format(i+1)
        res = requests.get(url, headers=headers)
        print(url)
        soup = BeautifulSoup(res.text, 'lxml')
        resblocks = soup.find_all('div', attrs={'class': 'resblock-name'})
        resblocks_area = soup.find_all('div', attrs={'class': 'resblock-area'})
        resblocks_location = soup.find_all('div', attrs={'class': 'resblock-location'})
        resblocks_price = soup.find_all('div', attrs={'class': 'resblock-price'})
        assert len(resblocks) == len(resblocks_area); assert len(resblocks) == len(resblocks_location); assert len(resblocks) == len(resblocks_price)

        resblock_location = resblocks_location[0]
        resblock_locationAll = resblock_location.find_all('span')
        location1 = resblock_locationAll[0].string
        location2 = resblock_locationAll[1].string
        location3 = isNone(resblock_location.find('a').string).strip()
        # print(location1)
        # print(location2)
        # print(location3)

# main fun.
def main():
    city_name = ['宝鸡',  '汉中',  '西安',  '咸阳',  '晋中',  '太原',  '天津',  '大理',  '昆明',  '西双版纳',  '杭州',  '湖州',  '嘉兴',  '金华',  '宁波',  '绍兴',  '台州',  '温州']
    city_name_pinyin = ['baoji',  'hanzhong',  'xi_an',  'xianyang',  'jinzhong',  'taiyuan',  'tianjin',  'dali',  'kunming',  'xishuangbanna',  'hangzhou',  'huzhou',  'jiaxing',  'jinhua',  'ningbo',  'shaoxing',  'taizhou',  'wenzhou']
    #city_name = input('Input the city name you want to know:')
	#city_name_pinyin = input('Input the city name pinyin you want to know:')
    #for index in range(len(city_name)):
    #try:
    #    city_url = data[city_name[index]] + '/loupan/'
    #    print(city_url)
    #except:
    #    print('[Error]: City name parse error...')
    #    return
    try:
        page_num = input('Input the page num you want to get:')
        page_num = int(page_num)
    except:
        print('[Error]: Page number should be number...')
        return
    #GetInfo(city_url, page_num, city_name_pinyin[index], city_name[index]) 
    GetInfo('https://sy.fang.lianjia.com/loupan/', page_num, 'shenyang', '沈阳')

if __name__ == '__main__':
	while True:
		main()