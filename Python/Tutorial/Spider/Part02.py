from urllib.request import urlopen
from bs4 import BeautifulSoup

#f 1.0
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
#get_text() 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回一个只包含文字的字符串。


# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html)

# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)

# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)