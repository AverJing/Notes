'''
def my_name(x):
    if x:
        print("Aver Jing")
    else:
        print("None")

my_name(0)
'''

#print(print(1+2))
#print无返回值

'''
import math

def quadratic(a,b,c):
    delta = b*b-4*a*c
    if delta < 0:
        return None
    else:
        tmp = math.sqrt(delta)
        return {(-b + tmp)/(2*a), (-b - tmp)/(2*a)}
    #注意python中整数除法是精确的
    #而且看起来函数可以返回不同类型的结果
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != {-0.5, -1.0}:
    print('测试失败')
elif quadratic(1, 3, -4) != {1.0, -4.0}:
    print('测试失败')
else:
    print('测试成功')
'''

'''
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())
'''

#fix

'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
'''

'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

#print(calc(1,2,3))
print(calc(*[1,2,3]))
'''

'''
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

person('AverJing', 23, city='SuZhou', gender = 'M')

extra = {'city':'suzhou', 'gender':'M'}

person('AverJing', 23, **extra) #更简洁
'''

'''
def person(name, age, *, city='beijing', gender, birth):
    print(name, age, city, gender, birth)

person('aver', 23, gender='M', birth='1995')
'''

'''
def product(*numbers):
    if not numbers:#numbers为空的判断
        raise TypeError
    res = 1
    for i in numbers:
        res*=i
    return res

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
 '''

def fact(n):
     return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)

print(fact(10))