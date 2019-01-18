## 高级特性
Python追求的是代码的精简？

### 切片
	切片操作是否会涉及到内存的分配？
	我估计大多数情况不会，因为一般Python中str，或者数字都是不可改变的，也即很可能在底层实现时，仅仅是基于指针访问的。也即浅拷贝。有待验证。这说的很粗浅。切片还能支持插入，替换，删除（借助del）更灵活的操作。
	注意负的索引
	切片范围，仍然满足左闭右开。

### 迭代
	默认情况，dict迭代的是key。也可以迭代value，也可以同时两者迭代
	通过colloections模块的Iterable类型判断一个对象是否可迭代。（3.7是colloections.abc）
	Python内置函数enumerate可以把list变成索引-元素对。

### 列表生成式
	基于for。。。in的语法糖。
	注意如果要加if需要放在for的后边

### 生成器	
	创建generator，第一种将列表生成式生成的[]改为()。还可以使用函数来创建generator，函数定义中包含yield关键字。generator函数，在每次调用next的时候，遇到yield语句返回，再次执行时从上次返回的yield语句处执行。
	用for循环调用generator时，发现拿不到generator的返回值。如果要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
	猜想：生成器应该就是类似于C++中的仿函数。
	杨辉三角的生成，参考代码实现的很优雅。和C++数组下标访问不同，Python中支持负数索引，其实C++重载运算符也可以实现。
### 迭代器
	区分Iterable和Iterator。Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
	异常，StopIteration