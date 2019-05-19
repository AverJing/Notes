from urllib.request import urlopen
html = urlopen("http://www.baidu.com")
#print(type(html.read()))
#read读出来的是bytes类型，不是str
with open("baidu.txt", 'w', encoding="utf-8") as f:
    f.write(html.read().decode("utf-8"))
#https://blog.csdn.net/LolitaQ/article/details/78117838