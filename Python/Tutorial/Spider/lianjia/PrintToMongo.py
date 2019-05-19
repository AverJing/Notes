# import json
# import pymongo

# conn = pymongo.MongoClient(host='localhost', port=27017)
# lianjia = conn['lianjia']
# suzhou = lianjia['suzhou']

# data = {'title': 'hello', 'img':'jpg', 'url':'world'}

# suzhou.insert_one(data)

i=10
print("%d is ok" %i)

def isNone(result):
    if result is None:
        return '暂无'
    else:
        return result

print('hello'.strip())