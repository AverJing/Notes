### 关于C++编程导学的总结 [文档](https://docs.unrealengine.com/en-US/Programming/Tutorials/index.html)

------------------

> 详细内容可以参考 Statup.md

#### C++编程导学之变量，计时器和事件

- 使用**计时器**延迟或者重复执行代码
  - 涉及到**UTextRenderComponent， FTimerHandle组件**
  - 通过**GetWorldTimerManager()**激活或者清除计时器。关于计数器可以参考 [1](https://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Timers/index.html)  [2](http://api.unrealengine.com/CHN/Gameplay/HowTo/UseTimers/Blueprints/index.html)
- 将变量和函数传递给虚幻编辑器
  - **UPROPERT(), UFUNCTION()**
  - 关于UFUNCTION中的修饰符，**`BlueprintCallable`，`BlueprintImplementableEvent` ，`BlueprintNativeEvent` **
  - 在蓝图中重写已经在C++中实现的函数
    - 可以添加对**父函数的调用**

#### C++编程导学之第一人称射击游戏

- 第一部分设置项目中，学到的知识
  - PIE名词；另存为关卡；并设置项目中默认加载的关卡
  - **什么是GameMode？**通过GameMode输出信息，利用GEngine
- 第二部分实现角色中
  - 建立一个新角色，并扩展为蓝图
  - 设置轴映射，记得wsad和对应的x和y轴正方向对应
  - 角色移动，移动函数是**根据Controller或者对应轴的旋转方向并沿着该方向进行位移**。
  - 控制摄像机移动时，可通过绑定Character基类中自带的AddControllerYaw（Pitch）Input
  - Character中内置了角色跳跃，只用控制bPressedJump变量就行。
- 第三部分，实现发射物
  - ProjectileCompoent和其他组件（比如发射的物体）的绑定
  - Fire的实现
    - 如何生成发射物，需要哪些参数？
      - 发射物的类（包含其运动组件及其配置以及碰撞处理等等），生成的位置，运动的方向，**FActorSpawnParameters**包含一系列参数（比如产生新的Actor归属于谁，谁控制生成的Actor产生伤害等等）
    - 为了得到生成的位置和运动方向，需要先获取摄像机（实际是Controller的Rotation和眼睛的位置）的位置和Rotation，再把偏移量转换到和相同眼睛的方向下。
    - 注意发射物都是在**当前世界内产生的**
    - **指针使用时，记得判断是否null**
  - AActor中内置生命周期（InitialLifeSpan），**关于碰撞设置内容不熟悉**
  - OnHit函数的实现，碰撞发生时，被碰撞的物体也应该施加一定的运动。
  - HUD类，来渲染纹理。
    - 设置FCanvasTileItem，如要绘制图形的左上角的位置 ，纹理数据，Item的颜色
    - 试着去看看实现，只是发现它将4个顶点坐标以及纹理坐标保存下来，并且根据这四个生成两个三角形。**再往下，怎么绘制的，不知如何下手？应该要去找shader？**
- 第四部分，角色动画
  - 导入动画时候，要有对应的骨骼。故在导入fbx模型时候，要让虚幻自动（自动？）生成其对应的骨骼。
  - 事件图表设置Jumping和Runing状态
  - 动画状态机


#### C++编程导学之组件和碰撞
- 创建一系列的组件（粒子系统组件，球体组件，静态网格物体组件，相机组件，弹簧臂组件），注意弹簧臂组件为相机组件提供了可以附加的特殊的插槽。掌握将此Pawn设置为默认控制玩家。
- 利用了ConstructHelper来创建资源（网格，粒子系统）
- 如何移动？
	- 判断Pawn是否为空，移动的物体是否为空， 是否应该跳过此次更新
	- 先从Pawn中获取移动的方向向量
	- SafeMoveUpdatedComponent移动物体，记录碰撞结果，如果碰撞了，使用SlideAlongSurface移动。	 	
	- 疑问？如何生成相关的HIt信息的？如何沿着边缘移动的？（沿着某个平面移动的向量，根据两个向量的点积及其几何意义，找到一个在另一个的投影，再做向量减法就可以找到限定再某个平面位移的向量）
- 将Pawn和移动组件绑定，使用自定义移动组件的时候，需要覆盖GetMovementComponent。



#### C++编程导学之游戏控制的摄像机
- 放置摄像机的方式
  - 直接找到一个摄像机actor，拖拽到场景中
  - 或者，先拖拽一个立方体，在在此立方体上添加摄像机组件