### [C++模板导学](https://github.com/wuye9036/CppTemplateTutorial)

> 了解的不在赘述，仅仅记录重点或者盲点。

----------

#### 0 前言

##### 0.1 简介

- Bjarne在《The Design and Evolution of C++》一书中，详细的解释了C++为什么会变成如今（C++98/03）的模样。
- 模板作为C++中最有特色的语言特性，它堪称玄学的语法和语义，理所应当的成为初学者的梦魇。甚至很多工作多年的人也对C++的模板部分保有充分的敬畏。
- 其中对元编程技法贡献最大的当属Alexandrescu的《Modern C++ Design》及模板程序库Loki。这一2001年发表的图书间接地导致了模板元编程库的出现。书中所使用的Typelist等泛型组件，和Policy等设计方法令人耳目一新。但是因为全书用的是近乎Geek的手法来构造一切设施，因此使得此书阅读起来略有难度。
- 2002年出版的另一本书《C++ Templates》，可以说是在Template方面的集大成之作。它详细阐述了模板的语法、提供了和模板有关的语言细节信息，举了很多有代表性例子。但是对于模板新手来说，这本书细节如此丰富，让他们随随便便就打了退堂鼓缴械投降。
- 本文的写作初衷，就是通过“编程语言”的视角，介绍一个简单、清晰的“模板语言”。我会尽可能的将模板的诸多要素连串起来，用一些简单的例子帮助读者学习这门“语言”，让读者在编写、阅读模板代码的时候，能像 `if(exp) { dosomething(); }`一样的信手拈来，让“模板元编程”技术成为读者牢固掌握、可举一反三的有用技能。

##### 0.2 适宜读者群
- 熟悉C++的基本语法；
- 使用过STL；
- 熟悉一些常用的算法，以及递归等程序设计方法。
- 从知识结构上，我建议大家可以先读本文，再阅读《C++ Templates》获取**更丰富的语法与实现细节**，以更进一步；《Modern C++ Design》除了元编程之外，**还有很多的泛型编程示例**，原则上泛型编程的部分与我所述的内容交叉不大，读者在读完1-3章了解模板的基本规则之后便可阅读《MCD》的相应章节；元编程部分（如Typelist）建议在阅读完本文之后再行阅读，或许会更易理解。

##### 0.3 版权
- @空明流转 [知乎已注销](https://www.zhihu.com/people/wuye9036/activities)

##### 0.4 环境

- [在线编译器](https://gcc.godbolt.org/)
- VS2019

#### 1 Template的基本语法

-----------

##### 1.1 Template class基本语法

- 模板类的声明

```c++
template <typename T> class ClassA;
```

- 模板类的定义

```c++
template <typename T> class ClassA
{
	T member;
};
```

- 模板的使用
  - 把通过类型绑定到模板类变成“普通的类”的过程，称为**模板实例化**。
- 模板类的成员函数的定义
  - 在成员函数实现的时候，**必须要提供模板参数**。此外，为什么类型名不是`vector`而是`vector<T>`呢？ 如果你了解过模板的偏特化与特化的语法，应该能看出，这里的vector在语法上类似于特化/偏特化。实际上，这里的函数定义也确实是成员函数的偏特化。

##### 1.2 Template Functino的基本语法
- 和模板类类似
- 在学习模板的时候，要反复做以下的思考和练习：

    - 提出问题：我的需求能不能用模板来解决？

    - 怎么解决？

    - 把解决方案用代码写出来。

    - 如果失败了，找到原因。是知识有盲点（例如不知道怎么将 T& 转化成 T），还是不可行（比如试图利用浮点常量特化模板类，但实际上这样做是不可行的）？
- 通过重复以上的练习，应该可以对模板的语法和含义都有所掌握。如果提出问题本身有困难，或许下面这个经典案例可以作为你思考的开始：

    1. 写一个泛型的数据结构：例如，线性表，数组，链表，二叉树；
    2. 写一个可以在不同数据结构、不同的元素类型上工作的泛型函数，例如求和；
- 当然和“设计模式”一样，模板在实际应用中，也会有一些固定的需求和解决方案。比较常见的场景包括：**泛型**（最基本的用法）、**通过类型获得相应的信息**（型别萃取）、**编译期间的计算**、**类型间的推导和变换**（从一个类型变换成另外一个类型，比如boost::function）。这些本文在以后的章节中会陆续介绍。
- 只不过在部分推导、部分指定的情况下，编译器对模板参数的顺序是有限制的：**先写需要指定的模板参数，再把能推导出来的模板参数放在后面。**

##### 1.3 整数作为Template参数
- 这里的整数比较宽泛，包括布尔，不同位数，有无符号的整数，甚至包括指针。
- 其中有一点要注意的是，**因为模板的匹配是在编译的时候完成的，所以实例化模板的时候所使用的参数，也必须要在编译期就能确定**

- **注意不能是浮点数**。当然，除了单纯的用作常数之外，整型参数还有一些其它的用途。这些“其它”用途最重要的一点是**让类型也可以像整数一样运算**。

#### 2 模板元编程基础

------

##### 2.1 编程，元编程，模板元编程

- 程序最根本的目的是什么？复现真实世界或人所构想的规律，减少重复工作的成本，或通过提升规模完成人所不能及之事。但是世间之事万千，有限的程序如何重现复杂的世界呢？

  答案是“抽象”。论及具体手段，无外乎“求同”与“存异”：概括一般规律，处理特殊情况。这也是软件工程所追求的目标。一般规律概括的越好，我们所付出的劳动也就越少。

- ```c++
  如何撰写更高级的C++程式？
  如何应付即使在很干净的设计中仍然像雪崩一样的不相干细节？
  如何构建可复用组件，使得每次在不同程式中应用组件时无需大动干戈？
  ```

- 元（meta）无论在中文还是英文里，都是个很“抽象（abstract）”的词。因为它的本意就是“抽象”。元编程，也可以说就是“编程的抽象”。用更好理解的说法，元编程意味着你撰写一段程序A，程序A会运行后生成另外一个程序B，程序B才是真正实现功能的程序。那么这个时候程序A可以称作程序B的元程序，撰写程序A的过程，就称之为“元编程”。

- 模板和宏的关系

  - 大多数情况模板是替换类型的，和宏差不多（宏只是基于文本的替换）
  - 模板可以运算的。
    - **根据类型分别提供不同的实现。**
      - 当然重载也可以用的。如果类型很多，重载比较繁琐。

##### 2.2 模板世界的If-Then-Else：类模板的特化与偏特化

- 根据类型执行代码；模板不是唯一的方法，重载，虚函数等等都是的。

  - 比如下边的C代码，常用的手法

    - ```c
      struct Variant
      {
          union
          {
              int x;
              float y;
          } data;
          uint32 typeId;
      };
      
      Variant addFloatOrMulInt(Variant const* a, Variant const* b)
      {
          Variant ret;
          assert(a->typeId == b->typeId);
          if (a->typeId == TYPE_INT)
          {
              ret.x = a->x * b->x;
          }
          else
          {
              ret.y = a->y + b->y;
          }
          return ret;
      }
      ```

    - ```c
      #define BIN_OP(type, a, op, b, result) (*(type *)(result)) = (*(type const *)(a)) op (*(type const*)(b))
      void doDiv(void* out, void const* data0, void const* data1, DATA_TYPE type)
      {
          if(type == TYPE_INT)
          {
              BIN_OP(int, data0, *, data1, out);
          }
          else
          {
              BIN_OP(float, data0, +, data1, out);
          }
      }
      ```

  - 但是模板与这些方法最大的区别并不在这里。**模板无论其参数或者是类型，它都是一个编译期分派的办法。编译期就能确定的东西既可以做类型检查，编译器也能进行优化，砍掉任何不必要的代码执行路径。**成也编译期，败也编译期。最严重的“缺点”，**就是你没办法根据用户输入或者别的什么在运行期间可能发生变化的量来决定它产生、或执行什么代码。**
    - 这点限制也粉碎了妄图用模板来包办工厂（Factory）甚至是反射的梦想。
    - 直到C++11/14，光靠模板你就是写不出依靠类名或者ID变量产生类型实例的代码。

  - 单看代码我们就能知道， `aVar` 和 `bVar` 都一定会是整数。所以如果有合适的机制，编译器就能知道此处的 `addFloatOrMulInt` 中只需要执行 `Int` 路径上的代码，而且编译器在此处也能单独为 `Int` 路径生成代码，**从而去掉那个不必要的 `if`。**

- **特化**（类）

  - 理解特化和偏特化。

  - 写模板的一般形式，实现一般用不到（**特化的不能匹配到的时候，调用一般形式**）

    - 然后根据最一般的模板，来特化从而实现不同的功能

  - **不过这里有一个问题要厘清一下。和继承不同，类模板的“原型”和它的特化类在实现上是没有关系的，并不是在类模板中写了 `ID` 这个Member，那所有的特化就必须要加入 `ID` 这个Member，或者特化就自动有了这个成员。完全没这回事。我们把类模板改成以下形式，或许能看的更清楚一点：**

    - ```c++
      template <typename T> class TypeToID
      {
      public:
          static int const NotID = -2;
      };
      
      template <> class TypeToID<float>
      {
      public:
          static int const ID = 1;
      };
      
      void PrintID()
      {
          cout << "ID of float: " << TypeToID<float>::ID << endl; // Print "1"
          cout << "NotID of float: " << TypeToID<float>::NotID << endl; // Error! TypeToID<float>使用的特化的类，这个类的实现没有NotID这个成员。
          cout << "ID of double: " << TypeToID<double>::ID << endl; // Error! TypeToID<double>是由模板类实例化出来的，它只有NotID，没有ID这个成员。
      }
      ```

    - 这样就明白了。**类模板和类模板的特化的作用，仅仅是指导编译器选择哪个编译，但是特化之间、特化和它原型的类模板之间，是分别独立实现的。**所以如果多个特化、或者特化和对应的类模板有着类似的内容，很不好意思，你得写上若干遍了。

    - C++有了模板后，能否既能匹配任意类型的指针，同时又保留了类型信息呢？答案是显然的。

##### 2.3 即用即推导

- 这一节我们将讲述模板一个非常重要的行为特点：那就是什么时候编译器会对模板进行推导，推导到什么程度。

  - ```c++
    template <typename T> struct X {};
    	
    template <typename T> struct Y
    {
        typedef X<T> ReboundType;				// 类型定义1
        typedef typename X<T>::MemberType MemberType;	// 类型定义2
        typedef UnknownType MemberType3;			// 类型定义3
    
        void foo()
        {
            X<T> instance0;
            typename X<T>::MemberType instance1;
            WTF instance2
            大王叫我来巡山 - + &
        }
    };
    ```

  - 把这段代码编译一下，类型定义3出错，其它的都没问题。不过到这里你应该会有几个问题：

    1. 不是`struct X<T>`的定义是空的吗？为什么在`struct Y`内的类型定义2使用了 `X<T>::MemberType` 编译器没有报错？
    2. 类型定义2中的`typename`是什么鬼？为什么类型定义1就不需要？
    3. 为什么类型定义3会导致编译错误？
    4. 为什么`void foo()`在MSVC下什么错误都没报？

    这时我们就需要请出C++11标准 —— 中的某些概念了。这是我们到目前为止第一次参阅标准。我希望能尽量减少直接参阅标准的次数，因此即便是极为复杂的模板匹配决议我都暂时没有引入标准中的描述。 然而，**Template引入的“双阶段名称查找（Two phase name lookup）”堪称是C++中最黑暗的角落 **—— 这是LLVM的团队自己在博客上说的 —— 因此在这里，我们还是有必要去了解标准中是如何规定的。

- **2.3.2 名称查找**

  - 名称查找/名称解析，是编译器的基石。对编译原理稍有了解的人，都知道“符号表”的存在即重要意义。考虑一段最基本的C代码：

  - ```c++
    int a = 0;
    int b;
    b = (a + 1) * 2;
    printf("Result: %d", b);
    ```

  - 在这段代码中，所有出现的符号可以分为以下几类：

    - `int`：类型标识符，代表整型；
    - `a`,`b`,`printf`：变量名或函数名；
    - `=`,`+`,`*`：运算符；
    - `,`,`;`,`(`,`)`：分隔符；

    那么，编译器怎么知道`int`就是整数类型，`b=(a+1)*2`中的`a`和`b`就是整型变量呢？**这就是名称查找/名称解析的作用**：它告诉编译器，这个标识符（identifer）是在哪里被声明或定义的，它究竟是什么意思。

  - 也正因为这个机制非常基础，所以它才会面临各种可能的情况，编译器也要想尽办法让它在大部分场合都表现的合理。比如我们常见的作用域规则，就是为了对付名称在不同代码块中传播、并且遇到重名要如何处理的问题。

  - 但是模板的引入，使得名称查找这一本来就不简单的基本问题变得更加复杂了。 考虑下面这个例子：

    - ```c++
      struct A  { int a; };
      struct AB { int a, b; };
      struct C  { int c; };
      
      template <typename T> foo(T& v0, C& v1){
          v0.a = 1;
          v1.a = 2;
          v1.c = 3;
      }
      ```

    - 简单分析上述代码很容易得到以下结论：

      1. 函数`foo`中的变量`v1`已经确定是`struct C`的实例，所以，`v1.a = 2;`会导致编译错误，`v1.c = 3;`是正确的代码；
      2. 对于变量`v0`来说，这个问题就变得很微妙。如果`v0`是`struct A`或者`struct AB`的实例，那么`foo`中的语句`v0.a = 1;`就是正确的。如果是`struct C`，那么这段代码就是错误的。

  - 因此在模板定义的地方进行语义分析，并不能**完全**得出代码是正确或者错误的结论，只有到了实例化阶段，确定了模板参数的类型后，才知道这段代码正确与否。令人高兴的是，在这一问题上，我们和C++标准委员会的见地一致，说明我们的C++水平已经和Herb Sutter不分伯仲了。既然我们和Herb Sutter水平差不多，那凭什么人家就吃香喝辣？下面我们来选几条标准看看服不服：

    - > **14.6 名称解析（Name resolution）**

      > **1)** 模板定义中能够出现以下三类名称：

      > - 模板名称、或模板实现中所定义的名称；
      > - 和模板参数有关的名称；
      > - 模板定义所在的定义域内能看到的名称。

      > …

      > **9)** … 如果名字查找和模板参数有关，那么查找会延期到模板参数全都确定的时候。 …

      > **10)** 如果（模板定义内出现的）名字和模板参数无关，那么在模板定义处，就应该找得到这个名字的声明。…

      > **14.6.2 依赖性名称（Dependent names）**

      > **1)** …（模板定义中的）表达式和类型可能会依赖于模板参数，并且模板参数会影响到名称查找的作用域 … 如果表达式中有操作数依赖于模板参数，那么整个表达式都依赖于模板参数，名称查找延期到**模板实例化时**进行。并且定义时和实例化时的上下文都会参与名称查找。（依赖性）表达式可以分为类型依赖（类型指模板参数的类型）或值依赖。

      > **14.6.2.2 类型依赖的表达式**

      > **2)** 如果成员函数所属的类型是和模板参数有关的，那么这个成员函数中的`this`就认为是类型依赖的。

      > **14.6.3 非依赖性名称（Non-dependent names）**

      > **1)** 非依赖性名称在**模板定义**时使用通常的名称查找规则进行名称查找。

    - 看一个例子：

      - ```c++
        int a;
        struct B { int v; }
        template <typename T> struct X {
            B b;                  // B 是第三类名字，b 是第一类
            T t;                  // T 是第二类
            X* anthor;            // X 这里代指 X<T>，第一类
            typedef int Y;        // int 是第三类
            Y y;                  // Y 是第一类
            C c;                  // C 什么都不是，编译错误。
            void foo() {
               b.v += y;          // b 是第一类，非依赖性名称
               b.v *= T::s_mem;   // T::s_mem 是第二类
                                  // s_mem的作用域由T决定
                                  // 依赖性名称，类型依赖
            }
        };
        ```

      - 所以，按照标准的意思，**名称查找会在模板定义和实例化时各做一次，分别处理非依赖性名称和依赖性名称的查找。这就是“两阶段名称查找”这一名词的由来。**只不过这个术语我也不知道是谁发明的，它并没有出现的标准上，但是频繁出现在StackOverflow和Blog上。

- **2.3.3 “多余的”typename关键字**

  - 对于用户来说，这其实是一个语法噪音。也就是说，其实就算没有它，语法上也说得过去。事实上，某些情况下MSVC的确会在标准需要的时候，不用写`typename`。但是标准中还是规定了形如 `T::MemberType` 这样的`qualified id` 在默认情况下不是一个类型，而是解释为`T`的一个成员变量`MemberType`，只有当`typename`修饰之后才能作为类型出现。

  - **简单来说，如果编译器能在出现的时候知道它的类型，那么就不需要`typename`，如果必须要到实例化的时候才能知道它是不是合法，那么定义的时候就把这个名称作为变量而不是类型。**

  - 在这里，我举几个例子帮助大家理解`typename`的用法，这几个例子已经足以涵盖日常使用

    - ```c++
      struct A;
      template <typename T> struct B;
      template <typename T> struct X {
          typedef X<T> _A; // 编译器当然知道 X<T> 是一个类型。
          typedef X    _B; // X 等价于 X<T> 的缩写
          typedef T    _C; // T 不是一个类型还玩毛
          
          // ！！！注意我要变形了！！！
          class Y {
              typedef X<T>     _D;          // X 的内部，既然外部高枕无忧，内部更不用说了
              typedef X<T>::Y  _E;          // 嗯，这里也没问题，编译器知道Y就是当前的类型，
                                            // 这里在VS2015上会有错，需要添加 typename，
                                            // Clang 上顺利通过。
              typedef typename X<T*>::Y _F; // 这个居然要加 typename！
                                            // 因为，X<T*>和X<T>不一样哦，
                                            // 它可能会在实例化的时候被别的偏特化给抢过去实现了。
          };
          
          typedef A _G;                   // 嗯，没问题，A在外面声明啦
          typedef B<T> _H;                // B<T>也是一个类型
          typedef typename B<T>::type _I; // 嗯，因为不知道B<T>::type的信息，
                                          // 所以需要typename
          typedef B<int>::type _J;        // B<int> 不依赖模板参数，
                                          // 所以编译器直接就实例化（instantiate）了
                                          // 但是这个时候，B并没有被实现，所以就出错了
      };
      ```



##### 2.4 本章小结

- **部分特化/偏特化** 和 **特化** 相当于是模板实例化过程中的`if-then-else`。这使得我们根据不同类型，选择不同实现的需求得以实现；
- 在 2.3.3 一节我们插入了C++模板中最难理解的内容之一：**名称查找**。名称查找是语义分析的一个环节，模板内书写的 **变量声明**、**typedef**、**类型名称** 甚至 **类模板中成员函数的实现** 都要符合名称查找的规矩才不会出错；
- C++编译器对语义的分析的原则是“大胆假设，小心求证”：在能求证的地方尽量求证 —— 比如两段式名称查找的第一阶段；**无法检查的地方假设你是正确的 —— 比如`typedef typename A<T>::MemberType _X;`在模板定义时因为`T`不明确不会轻易判定这个语句的死刑。**
- 从下一章开始，我们将进入元编程环节。我们将使用大量的示例，一方面帮助巩固大家学到的模板知识，一方面也会引导大家使用函数式思维去解决常见的问题。





#### 3 深入理解特化与偏特化

-----------

##### 3.1 正确的理解偏特化

- ###### **3.1.1 偏特化与函数重载的比较**

  - ```c++
    template <typename T, typename U> struct X            ;    // 0 
                                                               // 原型有两个类型参数
                                                               // 所以下面的这些偏特化的实参列表
                                                               // 也需要两个类型参数对应
    template <typename T>             struct X<T,  T  > {};    // 1
    template <typename T>             struct X<T*, T  > {};    // 2
    template <typename T>             struct X<T,  T* > {};    // 3
    template <typename U>             struct X<U,  int> {};    // 4
    template <typename U>             struct X<U*, int> {};    // 5
    template <typename U, typename T> struct X<U*, T* > {};    // 6
    template <typename U, typename T> struct X<U,  T* > {};    // 7
    
    template <typename T>             struct X<unique_ptr<T>, shared_ptr<T>>; // 8
    
    // 以下特化，分别对应哪个偏特化的实例？
    // 此时偏特化中的T或U分别是什么类型？
    
    X<float*,  int>      v0;                       
    X<double*, int>      v1;                       
    X<double,  double>   v2;                          
    X<float*,  double*>  v3;                           
    X<float*,  float*>   v4; //error                         
    X<double,  float*>   v5;                          
    X<int,     double*>  v6;                           
    X<int*,    int>      v7; //error                        
    X<double*, double>   v8;
    ```

  - > 令`T`是模板类型实参或者类型列表（如 *int, float, double* 这样的，`TT`是template-template实参（参见6.2节），`i`是模板的非类型参数（整数、指针等），则以下形式的形参都会参与匹配：

    > ```
    > T`,`cv-list T`,`T*`, `template-name <T>`, `T&`, `T&&
    > ```

    > ```
    > T [ integer-constant ]
    > ```

    > ```
    > type (T)`, `T()`, `T(T)
    > ```

    > ```
    > T type ::*`, `type T::*`, `T T::*
    > ```

    > ```
    > T (type ::*)()`, `type (T::*)()`, `type (type ::*)(T)`, `type (T::*)(T)`, `T (type ::*)(T)`, `T (T::*)()`, `T (T::*)(T)
    > ```

    > ```c++
    > type [i]`, `template-name <i>`, `TT<T>`, `TT<i>`, `TT<>
    > ```

  - 对于某些实例化，偏特化的选择并不是唯一的。比如v4的参数是`<float*, float*>`，能够匹配的就有三条规则，1，6和7。很显然，6还是比7好一些，因为能多匹配一个指针。但是1和6，就很难说清楚谁更好了。一个说明了两者类型相同；另外一个则说明了两者都是指针。所以在这里，编译器也没办法决定使用那个，只好爆出了编译器错误。

- **3.1.2 不定长的模板参数**

  - 有没有一种办法能够让例子`DoWork`像重载一样，支持对长度不一的参数列表分别偏特化/特化呢？

    答案当然是肯定的。

    - 首先，首先我们要让模板实例化时的模板参数统一到相同形式上。逆向思维一下，虽然两个类型参数我们很难缩成一个参数，但是我们可以通过添加额外的参数，把一个扩展成两个呀。

    - ```c++
      DoWork<int,   void> i;
      DoWork<float, void> f;
      DoWork<int,   int > ii;
      ```

    - 显而易见这个解决方案并不那么完美。首先，不管是偏特化还是用户实例化模板的时候，都需要多撰写好几个`void`，而且最长的那个参数越长，需要写的就越多；其次，如果我们的`DoWork`在程序维护的过程中新加入了一个参数列表更长的实例，那么最悲惨的事情就会发生 —— 原型、每一个偏特化、每一个实例化都要追加上`void`以凑齐新出现的实例所需要的参数数量。

    - 所幸模板参数也有一个和函数参数相同的特性：**默认实参**（Default Arguments）。

    - ```c++
      template <typename T0, typename T1 = void> struct DoWork;
      
      template <typename T> struct DoWork<T> {};
      template <>           struct DoWork<int> {};
      template <>           struct DoWork<float> {};
      template <>           struct DoWork<int, int> {};
      
      DoWork<int> i;
      DoWork<float> f;
      DoWork<double> d;
      DoWork<int, int> ii;
      ```

    - 默认实参的缺点：

      - 默认实参的位置只能放在后边，限定了参数的顺序

      - 其次，假设这段代码中有一个函数，它的参数使用了和类模板相同的参数列表类型

        - ```c++
          template <typename T0, typename T1 = void> struct X {
              static void call(T0 const& p0, T1 const& p1);        // 0
          };
          
          template <typename T0> struct X<T0> {
              static void call(T0 const& p0);                      // 1
          };
          
          void foo(){
              X<int>::call(5);                // 调用函数 1
              X<int, float>::call(5, 0.5f);   // 调用函数 0
          }
          ```

        - 那么，每加一个参数就要多写一个偏特化的形式，甚至还要重复编写一些可以共享的实现。

          不过不管怎么说，以长参数加默认参数的方式支持变长参数是可行的做法，**这也是C++98/03时代的唯一选择。**

  - 为了缓解这些问题，在C++11中，引入了变参模板（Variadic Template）。

    - ```c++
      template <typename... Ts, typename U> class X {};              // (1) error!
      template <typename... Ts>             class Y {};              // (2)
      template <typename... Ts, typename U> class Y<U, Ts...> {};    // (3)
      template <typename... Ts, typename U> class Y<Ts..., U> {};    // (4) error!
      ```

    - 为什么第(1)条语句会出错呢？(1)是**模板原型，模板实例化时，要以它为基础和实例化时的类型实参相匹配**。**因为C++的模板是自左向右匹配的，所以不定长参数只能结尾**。其他形式，无论写作`Ts, U`，或者是`Ts, V, Us,`，或者是`V, Ts, Us`都是不可取的。(4) 也存在同样的问题。

      但是，为什么(3)中， 模板参数和(1)相同，都是`typename... Ts, typename U`，但是编译器却并没有报错呢？

      答案在这一节的早些时候。(3)和(1)不同，它并不是模板的原型，它只是`Y`的一个偏特化。回顾我们在之前所提到的，**偏特化时，模板参数列表并不代表匹配顺序，它们只是为偏特化的模式提供的声明**，也就是说，它们的匹配顺序，只是按照`<U, Ts...>`来，而之前的参数只是告诉你`Ts`是一个类型列表，而`U`是一个类型，排名不分先后。

- **3.1.3 模板的默认实参**

  - 实际上，模板的默认参数**不仅仅可以是一个确定的类型，它还能是以其他类型为参数的一个类型表达式。**

  - 考虑下面的例子：我们要执行两个同类型变量的除法，它对浮点、整数和其他类型分别采取不同的措施。 对于浮点，执行内置除法；对于整数，要处理除零保护，防止引发异常；对于其他类型，执行一个叫做`CustomeDiv`的函数。

    - 第一步，我们先把浮点正确的写出来.

      - ```c++
        template <typename T, bool IsFloat = std::is_floating_point<T>::value> struct SafeDivide {
            static T Do(T lhs, T rhs) {
                return CustomDiv(lhs, rhs);
            }
        };
        
        template <typename T> struct SafeDivide<T, true>{     // 偏特化A
            static T Do(T lhs, T rhs){
                return lhs/rhs;
            }
        };
        
        template <typename T> struct SafeDivide<T, false>{   // 偏特化B
            static T Do(T lhs, T rhs){
                return lhs;
            }
        };
        ```

    - 嗯，这个时候我们要再把整型和其他类型纳入进来，无外乎就是加这么一个参数

      - ```c++
        template <
            typename T,
            bool IsFloat = std::is_floating_point<T>::value,
            bool IsIntegral = std::is_integral<T>::value
        > struct SafeDivide {
            static T Do(T lhs, T rhs) {
                return CustomDiv(lhs, rhs);
            }
        };
        
        template <typename T> struct SafeDivide<T, true, false>{    // 偏特化A
            static T Do(T lhs, T rhs){
                return lhs/rhs;
            }
        };
        
        template <typename T> struct SafeDivide<T, false, true>{   // 偏特化B
            static T Do(T lhs, T rhs){
                return rhs == 0 ? 0 : lhs/rhs;
            }
        };
        ```

    - 当然，这时也许你会注意到，`is_integral`，`is_floating_point`和其他类类型三者是互斥的，那能不能只使用一个条件量来进行分派呢？答案当然是可以的。**拓展性很好**
      - ```c++
        template <typename T, typename Enabled = std::true_type> struct SafeDivide {
            static T Do(T lhs, T rhs) {
                return CustomDiv(lhs, rhs);
            }
        };
        
        template <typename T> struct SafeDivide<
            T, typename std::is_floating_point<T>::type>{    // 偏特化A
            static T Do(T lhs, T rhs){
                return lhs/rhs;
            }
        };
        
        template <typename T> struct SafeDivide<
            T, typename std::is_integral<T>::type>{          // 偏特化B
            static T Do(T lhs, T rhs){
                return rhs == 0 ? 0 : lhs/rhs;
            }
        };
        ```

      - 我们借助这个例子，帮助大家理解一下这个结构是怎么工作的：

        1. 对`SafeDivide<int>`

        - **通过匹配类模板的泛化形式，计算默认实参，可以知道我们要匹配的模板实参是**`SafeDivide<int, true_type>`
        - 计算两个偏特化的形式的匹配：A得到`<int, false_type>`,和B得到 `<int, true_type>`
        - 最后偏特化B的匹配结果和模板实参一致，使用它。

        1. 针对`SafeDivide<complex<float>>`

        - **通过匹配类模板的泛化形式，可以知道我们要匹配的模板实参是**`SafeDivide<complex<float>, true_type>`
        - 计算两个偏特化形式的匹配：A和B均得到`SafeDivide<complex<float>, false_type>`
        - A和B都与模板实参无法匹配，所以使用原型，调用`CustomDiv`



##### 3.2 后悔药：SFINAE

- 它来自于 **Substitution failure is not an error** 的首字母缩写。这一句之乎者也般难懂的话，由之乎者 —— 啊，不，Substitution，Failure和Error三个词构成。

  我们从最简单的词“Error”开始理解。Error就是一般意义上的编译错误。一旦出现编译错误，大家都知道，编译器就会中止编译，并且停止接下来的代码生成和链接等后续活动。

  其次，我们再说“Failure”。很多时候光看字面意思，很多人会把 Failure 和 Error 等同起来。但是实际上Failure很多场合下只是一个中性词。比如我们看下面这个虚构的例子就知道这两者的区别了。

- **所谓substitution，就是将函数模板中的形参，替换成实参的过程。**概念很简洁但是实现却颇多细节，所以C++标准中对这一概念的解释比较拗口。它分别指出了以下几点：

  - 什么时候函数模板会发生实参 替代（Substitute） 形参的行为；
  - 什么样的行为被称作 Substitution；
  - 什么样的行为不可以被称作 Substitution Failure —— 他们叫SFINAE error。

  我们在此不再详述，有兴趣的同学可以参照[`这里`](http://en.cppreference.com/w/cpp/language/sfinae)，这是标准的一个精炼版本。

- 当你觉得需要写 `enable_if` 的时候，**首先要考虑到以下可能性：**

  - 重载（对模板函数）
  - 偏特化（对模板类而言）
  - 虚函数

  - 从上面这些例子可以看到，**SFINAE最主要的作用，是保证编译器在泛型函数、偏特化、及一般重载函数中遴选函数原型的候选列表时不被打断。**除此之外，它还有一个很重要的元编程作用就是实现部分的编译期自省和反射。



#### 4 空明流转的知乎专栏-template

-------------------

##### 4.1 C++ Template的选择特化

- ##### 根据不同的条件来选择不同的模板

  - ```cpp
    template <typename T, typename U> class Add
    {
        // 干点啥
    };
    ```

  - 根据T和U是否由继承关系，来选择不同的实现

    - 1. 用特化来做

         ```cpp
   template <typename T, typename U, bool Enabled = std::is_base_of<T, U>::value> class Add;  // 模板的泛化形式（原型）
         
         template <typename T, typename U>
         struct Add<T, U, true>
         {
            // Blah blah blah
         };
         
         template <typename T, typename U>
         struct Add<T, U, false>
         {
            // Blah blah blah
         };
         ```
      
      2. 利用继承来做
      
       ```cpp
         template <typename T, typename U>
         struct Add: public AddBase< std::is_base_of<T, U>::value >
         {
            // Blah blah blah
         };
       ```
      
      3. ```cpp
         template <typename T, typename U, typename BoolType = std::true_type> class Add;
         
         template <typename T, typename U>
         struct Add<T, U, std::integral_constant<bool, std::is_base_of<T, U>::value>>
         {
         };
         
         template <typename T, typename U>
         struct Add<T, U, std::integral_constant<bool, !std::is_base_of<T, U>::value> >
         {
         };
         
         Add<B, D> a;      // ??
         Add<int, float> b;    // ??
         ```
    
  - 

