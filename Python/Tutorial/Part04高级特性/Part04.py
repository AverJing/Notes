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

#generator 
'''
g = (x*x for x in range(10))

for i in g:
    print(i)
'''
#输出generator生成的值
'''
def fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n+=1
    return "done"

for s in fib(10):
    print(s)

g = fib(6)

while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print("Generator return value: ", e.value)
        break
'''

#计算组合数
'''
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result*=i
    return result

def comb(n,m):
    return factorial(n)//(factorial(n-m) * factorial(m))
'''

#没有考虑，不合理性
'''
def comb(n,m):
    result1 = 1
    result2 = 1
    for i in range(n-m+1, n+1):
        result1 *= i
    for i in  range(1, m+1):
        result2 *= i
    return result1//result2

def triangles(n):
    i = 0
    while i < n:
        result=[]
        j = 0
        while j < i+1:
            result.append(comb(i,j))
            j+=1
        i+=1
        yield result
'''

#to generate the Yanghui triangle by generator
#better answer
N = [1]
for i in range(0):
    print(N[i-1])

def triangles(max):
    N = [1]
    while True:
        yield N
        S=N[:]
        S.append(0)
        N = [S[i-1] + S[i] for i in range(len(S))] #elegant

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles(10):
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')