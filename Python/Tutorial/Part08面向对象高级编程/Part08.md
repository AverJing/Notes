## 面向对象高级编程

###　使用__slots__
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法

Student.set_score = set_score给class绑定方法

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性。
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

### 使用@property（很强）
@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作。
还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性。

### 多重继承
略

### 定制类
Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

- __str__   __repr__
可以更改默认类实例输出的内容。

- __iter__
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

- __getitem__
要表现得像list那样按照下标取出元素，需要实现__getitem__()方法。可以支持索引，也可以支持切片。
__setitem__()，__delitem__()

- __getattr__
注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性。
作用，可以针对完全动态的情况作调用。

- __call__
实例对象变成可调用对象。相当于C++小括号的重载。
相当于一个实例访问其内的函数调用运算符。

###　枚举类

### 使用元类
暂略