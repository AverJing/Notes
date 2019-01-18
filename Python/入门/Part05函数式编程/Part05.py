#test reduce
'''
from functools import reduce
def add(x,y):
    return x*10+y

print(reduce(add, [1]))
'''
#string to int
'''
from functools import reduce
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

print(str2int('28918291829'))
'''

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
'''
def normalize(name):
    if name is not None:
        result=[]
        result.append(name[0].upper())
        for i in range(1,len(name)):
            result.append(name[i].lower())
        return ''.join(result)
    return name

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''
'''
def format_name(s):
    s1=s[0:1].upper()+s[1:].lower()
    return s1
print map(format_name, ['adam', 'LISA', 'barT'])
'''

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
'''
from functools import reduce

def prod(L):
    return reduce(lambda x, y : x * y, L)

#test
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
'''

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
from functools import reduce
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2float(s):
    L = s.split('.')
    return reduce(lambda x,y: x*10+y, map(char2num, L[0])) + reduce(lambda x,y: x * 0.1 + y, map(char2num, L[1][::-1]))/10 

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
'''
'''
from functools import reduce
reduce(lambda x,y: x*10+y, [1,2,3,4,5,6,7])
'''

#找自然数中的素数
'''
def _odd_iter(max):
    n = 1
    while n < max:
        n += 2
        yield n

def _not_visible(n):#自动捕获？
    return lambda x : x % n > 0

#def prime(max):
#    yield 2
#    #it = _odd_iter(max)
#    L = list(range(2,max))
#    it = iter(L)
#    n = 3
#    while n < max:
#        n = next(it)
#        yield n
#        it = filter(_not_visible(n), it)


def prime(max):
    yield 2
    it = _odd_iter(max)
    n = 2
    while n < max:
        n = next(it)
        yield n
        it = filter(_not_visible(n), it)

for i in prime(100):
    print(i)
'''

#def is_palindrome(n):
#    result = 0
#    tmp = n
#    while n:
#        result = result * 10 + n%10
#        n //= 10
#    return result  == tmp

#def is_palindrome(n):
#    return str(n) == str(n)[::-1]

'''
def is_palindrome(n):
    a=int(len(str(n)))#在VC++中to_string的实现其实思想和这个一样
    b=int(a/2)
    if(b==0):
        b=1
    return str(n)[:b]==str(n)[-b:]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
'''

'''
# sort
def byNmae(t):
    #lambda x : return x[0]
     return t[0]
def by_name(t):
    #return sorted(t, key = byNmae)#key do not support lambda??
    return sorted(t, key=lambda x : x[0])
print(by_name([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]))
'''

def test(*args):
    print(args)

test([1,2,3,4],[5,6,7,8], {'a':1,'b':2}, 1,2,3,{'c':3})
