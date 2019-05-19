#-*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup
import os
from pyquery import PyQuery as pq

# headers = {
# 			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
# 	}
# res = requests.get('https://aq.lianjia.com/ershoufang/', headers=headers)
# soup = BeautifulSoup(res.text, 'lxml')
# s = soup.find_all('div', attrs={'data-role': 'ershoufang'})
# urls = s[0].find_all('a')

# for url in urls:
# 	link = url.get('href')
# 	print(link)

# hello = {'hello':"hi"}
# for i in range(0,3):
#     with open('city_ershoufang_urls.json', 'w') as f:
# 	    json.dump(hello, f)

headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	}
response = requests.get('https://su.lianjia.com/ershoufang/107100661535.html', headers=headers, timeout=3)
# print(response.status_code)
doc = pq(response.text)
# unit_price = doc(".unitPriceValue").text()
# unit_price = unit_price[0:unit_price.index("元")]
# title = doc("h1").text()
# area = doc(".areaName .info a").eq(0).text().strip()
# communityName = doc('.communityName .info').text()
# print(communityName)


# detail_dict = dict()
# s = doc('.base .content li').items()
# for item in s:
#     #print(item('span').text())
#     name = item('span').text()
#     detail_dict[name] = item.remove('span').text()
#     #detail_dict[item('span').text()] = item.remove('span').text()

# print(detail_dict)


# name = 'hello'

# def hi():
#     global name
#     name = 'sss'

# hi()
# print(name)
