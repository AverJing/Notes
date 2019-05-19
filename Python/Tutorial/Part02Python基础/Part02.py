# v1 = 1000000000000000000000000000000000000000000000000000000000000000000000000
# v2 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

# print(v1+v2)

'''
from decimal import *

v3 = Decimal(1000000000000000000000000000000000000000000000000000000000000000000000000)
v4 = Decimal(7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777)

print(v3+v4)
'''

'''
import sys

print(sys.float_info)
'''

#https://stackoverflow.com/questions/41074815/python-why-raw-strings-are-not-allowed-to-have-odd-number-of-backslashes
#print(r'\\\t\\')
#print(r'F:\wamp1\www\stats\'')
#print(r'F:\wamp1\www\stats\')
#print(r'(F:\wamp1\www\stats\)')

#print('''line1 
#line2 
#line3''')

'''
a=1
print(a)
a='ABC'
print(a)

'''

#print("你好")

#print('hello, %s %%%s ' % ('Aver', 'Jing'))

'''
height = float(input("height: (m)"))
weight = float(input("weight: (kg)"))

BMI = weight / ( height * height)

if BMI > 32:
    print("111111")
elif BMI >=28:
    print('222222')
elif BMI >= 25:
    print('333333')
else:
    print('444444')

'''

'''
con = list(range(1,101))

sum=0
for i in con:
    sum+=i

print(sum)
'''


'''
sum=0
for i in range(1,101):
    sum+=i

print(sum)
'''

'''
d = {'M':98, 'B':88, 'C':70}

#print('T' in d)
print(d.get('T'))
print(d.get('T', -1))
print(d.get('B'))
'''

