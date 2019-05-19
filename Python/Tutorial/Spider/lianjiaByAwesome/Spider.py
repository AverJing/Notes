import json
import requests
from bs4 import BeautifulSoup
import os
import time
import random
import pymongo


f = open('./city_urls.json', 'r')
data = json.load(f)

ershoufangCityURL = {}
# 爬取信息
def GetInfo(url, cityname):
	print('[INFO]:Start to get infos...')
	headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	}
	url_city = url+'ershoufang/'
	res = requests.get(url_city, headers=headers)
	soup = BeautifulSoup(res.text, 'lxml')
	s = soup.find_all('div', attrs={'class': 'ershoufang'})
	if s:
		pass
	else:
		s = soup.find_all('div', attrs={'data-role': 'ershoufang'})
	if s:
		try:
			urls = s[0].find_all('a')
			ershoufangHerf = []
			for e in urls:
				link = e.get('href')
				city_urls = url + link.strip('/')
				ershoufangHerf.append(city_urls)
			ershoufangCityURL[cityname] = ershoufangHerf
		except:
			pass
		time.sleep(random.randint(5,10))	

# main fun.
def main():
	city_name = ['安庆','滁州','合肥','马鞍山','芜湖', '北京', '重庆', '福州', '龙岩','泉州', '厦门', '漳州', '东莞', '佛山', '广州', '惠州', '江门', '清远', '深圳', '珠海', '湛江', '中山', '贵阳', '北海', '桂林', '柳州', '南宁', '兰州', '黄石', '黄冈', '武汉', '襄阳', '咸宁', '宜昌', '长沙', '常德', '岳阳', '株洲', '保定', '承德', '邯郸', '衡水', '廊坊', '秦皇岛', '石家庄', '唐山', '邢台', '张家口', '保亭', '澄迈', '儋州', '定安', '海口', '临高', '乐东', '陵水', '琼海', '琼中', '三亚', '五指山', '文昌', '万宁',  '开封',  '洛阳',  '新乡',  '许昌',  '郑州',  '哈尔滨',  '常州',  '淮安',     '南京',     '南通',     '苏州',     '无锡',     '徐州',     '盐城',    '镇江',  '长春',  '吉林',  '赣州',  '九江',  '吉安',  '南昌',  '上饶',  '大连',  '丹东',  '沈阳',  '呼和浩特',  '银川',  '上海',  '成都',  '德阳',  '达州',  '乐山',  '凉山',  '绵阳',  '眉山',  '南充',  '济南',  '临沂',  '青岛',  '潍坊',  '威海',  '烟台',  '淄博',  '宝鸡',  '汉中',  '西安',  '咸阳',  '晋中',  '太原',  '天津',  '大理',  '昆明',  '西双版纳',  '杭州',  '湖州',  '嘉兴',  '金华',  '宁波',  '绍兴',  '台州',  '温州']
    #city_name = input('Input the city name you want to know:')
	#city_name_pinyin = input('Input the city name pinyin you want to know:')
	for index in range(0, len(city_name)):
		try:
			city_url = data[city_name[index]]
			print(city_url)
		except:
			print('[Error]: City name parse error...')
			return
		GetInfo(city_url, city_name[index]) 
		if index % 10 == 0:
			with open('city_ershoufang_urls.json', 'w') as f:
				json.dump(ershoufangCityURL, f)
    #GetInfo('https://sy.fang.lianjia.com/loupan/', page_num, 'shenyang', '沈阳')

if __name__ == '__main__':
	while True:
		main()