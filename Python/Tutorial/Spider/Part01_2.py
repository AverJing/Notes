from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

''' 
#f 01
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsobj = BeautifulSoup(html.read())
#任何 HTML（或XML）文件的任意节点信息都可以被提取出来，只要目标信息的旁边或附近有标记就行。
print(bsobj.h1)
'''

# try:
#     html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# except HTTPError as e:
#     print(e)
# else:
#    if html is None:
#        print("url is not found")
#    else:
#        print("hello")
#如果你想要调用的标签不存在,BeautifulSoup 就会返回 None 对象。不过，如果再调用这个None对象下面的子标签，就会发生AttributeError错误

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)