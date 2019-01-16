## [Python基础](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658427513eef3d9dd9f7c48599116735806328e81000)

Python采用缩进方式，不同于C++（感觉后者更好点）。
Python是对大小写敏感的。

### 数据类型和变量
- 整数
	Python可以处理任意大小的整数。详细可以看Decimal[文档](https://docs.python.org/3.7/library/decimal.html)
- 浮点数
	不知道Python中还区分float和double不。不区分，参看[文档](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)。float point numbers使用C中的double实现的。你机器硬件决定float的精度和范围，可通过sys.float_info查看。如果需要很高精度或者巨大的浮点运算，可以使用Decimal。如果想在输入了解，可以查看Cpython的代码。
- 字符串
	如果字符串内部包含'或者"可以使用转义字符\。Python还允许r' '表示' '内部的字符串不转义。注意不能是奇数个\在右边（和字符串结尾分号'挨着，否者Python会理解为\'，这造成字符串没有终结，自然报错），[问题看这](https://stackoverflow.com/questions/41074815/python-why-raw-strings-are-not-allowed-to-have-odd-number-of-backslashes)。对比C++11中regex，raw string literals
	Python允许用'''...'''的格式表示多行内容，注意...代表你要输出的内容，而且还要手工换行以后输出才是，好鸡肋。
	
- 布尔值
	True和False，注意大小写。
	布尔值可以用and，or和not运算。
	
- 空值
	None是一个特殊的空值。
	
- 变量
	变量名必须是字母，数字和\_的组合。
	在Python中等号=是赋值语句，可以把任意类型数据赋值给变量，同一个变量可以反复赋值，而且是不同类型的变量。这种变量本身类型不固定的语言称之为动态语言。至于赋值的内部操作，以后再说（基于地址，还是重新创建？）。
	
- 常量
	在Python中整数的除法也是精确的。
	当然它也有//，称为地板除，得到的永远是整数。
	
### 字符串和编码
- 字符编码
	Unicode编码到UTF-8
- Python的字符串
	Python中的字符串是以Unicode编码的。对于单个字符的编码，Python提供ord（获取字符的整数表示）和chr（把编码转换为对应的字符）。Python中的字符串类型是str，通过其encode方法可以指定编码。len函数可以计算字符串长度，也可以计算字符串字节数。
- 格式化
	在Python中采用的和C语言中一样。
	
### 使用list和tuple   为了节省时间，仅仅给出要点内容，参看廖雪峰的教程
- list，**有序**的集合。
	支持负下标操作。 	
	可在尾部（append），指定位置插入元素（insert）（效率？），删除尾部（pop），删除指定位置（pop），替换个别元素（直接赋值），而且list中元素类型可以不一样。
- tuple
	 和list非常类似，但是tuple一旦初始化就不能修改。
	 用小括号可以直接创建tuple，如果只有一个元素，加逗号区分数字。
	 如何限制tuple内指向的对象也是不可变的？
	 
### 条件判断
- if elif else  记得写冒号，和C++类似，if条件存在隐式转换
- input函数默认输入的是str类型。

### 循环
- for...in循环，对应C++的范围for循环（语法糖，其实就是使用迭代器的for）
	range函数（左闭右开），生成一个连续的整数序列，再通过list函数可以转换为list
- while
- break
- continue

## 使用dict和set
- dict，类比C++中的map和unordered_map
	简单的查了一下，是基于hash的，而且冲突解决是开放定址法，不知道最新的更改了吗？还是需要去Cpython中看源码。
	记住创建用的是大括号
	in关键字
	get方法，如果不存在返回None，也可以指定返回值
	pop用来删除
	dict中key必须是不可变对象。
	
- set
	创建set，需要一个list作为输入集合
	add，remove函数操作
	两个set作&是交，作|是并
	
- 再议不可变对象
	str是不可变对象，虽然由replace操作，但是其本事还是没变
	估计python中把对应C++中比较繁琐但是精华的const简略了。