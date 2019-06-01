##### 记录学习过程中查看的文档

- 关于一些宏的用处 [文档](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/index.html)
  
- 在虚幻引擎中进行编程时，可使用标准 C++ 类、函数和变量。可使用标准 C++ 语法对它们进行定义。然而，`UCLASS()`、`UFUNCTION()` 和 `UPROPERTY()` 宏可使虚幻引擎识别新的类、函数和变量。例如，以 `UPROPERTY()` 宏作为声明序言的变量可被引擎执行垃圾回收，也可在虚幻编辑器中显示和编辑。此外还有 `UINTERFACE()` 和 `USTRUCT()` 宏，以及用于指定 [类](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/Classes/Specifiers/index.html) 、[函数](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/Functions/Specifiers/index.html) 、[属性](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/Properties/Specifiers/index.html) 、接口或[结构体](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/Structs/Specifiers/index.html) 在虚幻引擎和虚幻编辑器中行为的每个宏关键词。
  
- UE中的Log使用，[链接](https://wiki.unrealengine.com/Logs,_Printing_Messages_To_Yourself_During_Runtime#Log_a_Float)

  - 形式上类似printf，通过占位符，进行输出
  - 输出字符串的时候，注意*号

- UPROPERTY的使用，[链接](<http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/Properties/index.html>)

  - 用来定义属性，以及该属性的修饰符。

    ```cpp
    UPROPERTY([specifier, specifier, ...], [meta(key=value, key=value, ...)])
    Type VariableName;
    ```

- UCLASS的使用，[链接](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Objects/index.html) 

  - UCLASS 包含定义类的一套属性和函数。这些是本地代码可用的普通 C++ 函数和变量，但被虚幻引擎特有的元数据所标记，它们在对象系统中的行为也因此受到控制。
  
- UFUNCTION，[链接](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/Functions/index.html)

  - ```c++
    UFUNCTION([specifier, specifier, ...], [meta(key=value, key=value, ...)])
    ReturnType FunctionName([Parameter, Parameter, ...])
    ```

  - 行为和C++函数相同。然而 `UFunctions` 在一些地方存在不同。例如，它们可从 [蓝图可视化脚本编辑](http://api.unrealengine.com/CHN/Engine/Blueprints/index.html) 系统中被调用或覆写。

