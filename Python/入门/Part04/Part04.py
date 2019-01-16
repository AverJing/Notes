#去掉字符串首尾的空格
'''
def trim(s):
    start = 0
    end = len(s) - 1
    for i in s:
        if i == ' ':
            start+=1
        else:
            break
    for i in range(end, -1, -1):
        if s[i] == ' ':
            end-=1
        else:
            break
    return s[start:end+1]

    
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''


#dict的key和value迭代
'''
d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
    print('[', k, v, ']')
'''

#判断一个对象是否是可迭代的
'''
from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance(1, Iterable))
'''

#使用迭代查找一个list中最小和最大值，并返回一个tuple
'''
def findMinAndMax(numbers):
    if not numbers:
        return (None, None)
    NumMin = numbers[0]
    NumMax = numbers[0]
    for i in numbers:
        if i < NumMin:
            NumMin=i
        if i > NumMax:
            NumMax=i
    return (NumMin, NumMax)

#减少比较次数
def findMinAndMax(numbers):
    if not numbers:
        return (None, None)
    NumMin = numbers[0]
    NumMax = numbers[0]
    for i in range(1, len(numbers), 2):
        if numbers[i] < numbers[i-1]:
            NumMin = (NumMin if(numbers[i] >= NumMin) else numbers[i])
            NumMax = (NumMax if(numbers[i-1] <= NumMax) else numbers[i-1])
        else:
            NumMin = (NumMin if(numbers[i-1] >= NumMin) else numbers[i-1])
            NumMax = (NumMax if(numbers[i] <= NumMax) else numbers[i])

    return (NumMin, NumMax)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''

#将list中的str类型变为小写
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) ]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
'''
