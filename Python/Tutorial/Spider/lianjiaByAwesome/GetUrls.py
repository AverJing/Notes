# 爬取所有城市的链接
from bs4 import BeautifulSoup
import requests
import json


city_urls = {}
url = 'https://www.lianjia.com/city/'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
response = soup.find_all('div', attrs={'class': 'city_province'})
for s in response:
	try:
		urls = s.find_all('a')
		print(urls)
		for url in urls:
			city_name = url.string
			city_name = city_name.strip()
			link = url.get('href')
			city_urls[city_name] = link
	except:
		continue

f = open('city_urls.json', 'w')
json.dump(city_urls, f)
f.close()

# 注意还需要清洗。