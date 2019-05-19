import json
import requests
from bs4 import BeautifulSoup
import os
import time
import random
import pymongo

def GetPageNum(tmp='https://mas.lianjia.com/loupan/'):
    url = tmp
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        print(1111)
    #soup = BeautifulSoup(res.content, 'html.parser')
    #resblocks = soup.find(class_='page-box')
    #page = soup.select('.page-box')
    #resblocks = soup.find_all('div', attrs={'class': 'resblock-name'})
    #print(resblocks)
    #print(resblocks.find_all('a'))

GetPageNum()