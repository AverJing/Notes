##### 编辑器基本快捷操作

- 鼠标右键调整摄像机视角，左键位移，Q和E垂直上下位移，WASD略。F聚焦某个物体，此时ALT+鼠标左键可以360°观察物体。END键将物体落地。

##### 虚幻项目目录结构([来源](https://zhuanlan.zhihu.com/p/22814098))

- Binaries,存放编译生成的结果二进制文件.该目录可以gitignore,反正每次都会生成。
- Config,配置文件
- Content,最常用到, 所有的资源和蓝图等都放在该目录下
- DerivedDataCache：“DDC”，存储着引擎针对平台特化后的资源版本。比如同一个图片，针对不同的平台有不同的适合格式，这个时候就可以在不动原始的uasset的基础上，比较轻易的再生成不同格式资源版本。gitignore。
- Intermediate：中间文件（gitignore），存放着一些临时生成的文件。有：
  - Build的中间文件，.obj和预编译头等
  - UHT预处理生成的.generated.h/.cpp文件
  - VS.vcxproj项目文件，可通过.uproject文件生成编译生成的Shader文件。
  - AssetRegistryCache：Asset Registry系统的缓存文件，Asset Registry可以简单理解为一个索引了所有uasset资源头信息的注册表。CachedAssetRegistry.bin文件也是如此。
- Saved：存储自动保存文件，其他配置文件，日志文件，引擎崩溃日志，硬件信息，烘培信息数据等。gitignore
- Source：代码文件。

##### 虚幻4的命名规则([官方文档](http://api.unrealengine.com/CHN/Programming/Development/CodingStandard/))

- 命名规则:

  - 注意类名有额外的大写字母前缀,如FSkin是一个类,而Skin是该类的实例化

  - 模版类以T作为前缀，比如TArray,TMap,TSet UObject派生类都以U前缀

  - AActor派生类都以A前缀

  - SWidget派生类都以S前缀

  - 抽象接口以I前缀

  - 枚举以E开头

  - bool变量以b前缀，如bPendingDestruction

  - 其他的大部分以F开头，如FString,FName

  - typedef的以原型名前缀为准，如typedef TArray<FMyType> FArrayOfMyTypes;

  - 在编辑器里和C#里，类型名是去掉前缀过的

  - UHT在工作的时候需要你提供正确的前缀，所以虽然说是约定，但你也得必须遵守。（编译系统怎么用到那些前缀，后续再讨论）

  - ###### 函数命名用动词,如果有返回值名字要清晰知道返回值的含义.

- 现代C++语法

  - static_assert,override,final,nullptr
  - 不建议使用auto,除非在必须的情况,如:
  - 推断lambda变量类型
  	- 迭代器类型过于冗长,降低可读性的时候
  	- 模板代码中,类型表达式无法清楚表达时候
  - 范围for
  - lambda和匿名函数
    - 长度最好不要超过两条语句
    - 对于大型匿名函数或者延迟执行来说,倾向使用显示捕获.倾向使用显式返回类型.
  - 强类型的enum class,解释看[这里](https://blog.csdn.net/sanoseiichirou/article/details/50180533)
    - 原来的enum问题: 向整性的隐式转换
    - 无法指定底层所使用的数据类型
    - enum的作用域,**大括号并没有将枚举成员的可见域限制在大括号内，导致enum成员曝露到了上一级作用域(块语句)中。** 可以利用命名空间解决.
  - 移动语义
  - 默认成员初始化
    - 需要重新编译依赖文件才能修改默认设置。
    - 引擎的补丁中无法修改标头，此格式将限制修复的类型。
    - 无法以此方式初始化所有对象，例如基类、UObject子对象、前置声明类型的指针、构造函数参数的推断值、多步骤初始化成员等。
    - 标头中含有一些初始器，其余则在.cpp文件的构造函数中，可能会影响可读性和可维护性。

##### 基础概念

- 在UE4中，几乎所有的对象都继承于UObject（跟Java,C#一样），UObject为它们提供了基础的垃圾回收，反射，元数据，序列化等，相应的，就有各种"UClass"的派生们定义了属性和行为的数据。
- 在UE中，3D世界是由Actors构建起来的，而Actor又拥有各种Component，之后又有各种Controller可以控制Actor（Pawn）的行为。在UE4中，你也可以为一个Actor添加一个蓝图或者C++ Component,然后实现它来直接组织逻辑。 UE4也支持各种插件。

##### 编译系统

UE4支持众多平台，包括Windows,IOS，Android等，因此UE4为了方便你配置各个平台的参数和编译选项，简化编译流程,UE4实现了自己的一套**编译系统**，否则我们就得接受各个平台再单独配置一套项目之苦了。
这套工具的编译流程结果，简单来说，就是你在VS里的运行，背后会运行UE4的一些命令行工具来完成编译，其他最重要的两个组件：

- UnrealBuildTool（UBT，C#）：UE4的自定义工具，来编译UE4的逐个模块并处理依赖等。我们编写的Target.cs，Build.cs都是为这个工具服务的。
- UnrealHeaderTool （UHT，C++）：UE4的C++代码解析生成工具，我们在代码里写的那些宏UCLASS等和#include "*.generated.h"都为UHT提供了信息来生成相应的C++反射代码。

一般来说，UBT会先调用UHT会先负责解析一遍C++代码，生成相应其他代码。然后开始调用平台特定的编译工具(VisualStudio,LLVM)来编译各个模块。最后启动Editor或者是Game.

##### UE4术语(文档[链接](http://api.unrealengine.com/CHN/GettingStarted/Terminology/))

- Project项目 
  - 一个项目会经常被与其关联的`.uproject`文件所引用，但它们是两个互相并存的独立文件。`.uproject`是一个用于创建、打开或保存文件的参考文件，而项目则包含与其关联的所有文件和文件夹。
- Object对象
  - 在虚幻引擎中，最基础的构建单元叫做 **Object**，它包含了很多游戏资源必需的 **幕后** 功能。虚幻引擎4中几乎所有的东西都是继承自Object（或从中获取部分功能）。在C++中，`UObject` 是所有Object的基类，实现了诸如垃圾回收、开放变量给编辑器的元数据（UProperty），以及存盘和读盘时的序列化功能。
- Class类
  - **类（Class）** 用于定义在创建虚幻引擎游戏中使用的特定Actor或对象的行为和属性。类具有层级性，这意味着某个类从其父类（衍生或派生出该类的类）获得信息，然后再将信息传递给子项。类可用C++代码或蓝图创建。
- Actors
  - 可放入关卡中的对象都是 **Actor**。Actor是支持三维转换（如平移、旋转和缩放）的泛型类。可通过游戏进程代码（C++或蓝图）创建（生成）及销毁Actor。在C++中，AActor是所有Actor的基本类。
- Component组件
  - **组件（Component）** 是可添加到Actor的一项功能。组件不可独立存在，但在将其添加到Actor后，该Actor便可以访问并可以使用该组件所提供的功能。
- Pawn人形体
  - **Pawn** 是Actor的一个子类，充当游戏中的化身或假面，例如游戏中的角色。Pawn可以由玩家或游戏AI以非玩家角色（NPC）的形式控制。
- **Character 角色**
  - **角色（Character）** 是Pawn Actor的子类，旨在用作玩家角色。角色子类包括碰撞设置、双足运动的输入绑定，以及由玩家控制的运动附加代码。
- **PlayerController 玩家控制器**
  - **玩家控制器（PlayerController）** 类用于在游戏中获取玩家输入并将其转换为交互，每个游戏中至少有一个玩家控制器。玩家控制器通常拥有一个Pawn或角色作为游戏中玩家的代表。
- Level关卡
  - **level** （关卡）是用户定义的游戏区域。 我们主要通过放置、变换及编辑Actor的属性来创建、查看及修改关卡。 在虚幻编辑器中，每个关卡都被保存为单独的.umap文件，所以它们有时也被称为“地图”。
- Wolrd世界
  - **世界场景（World）** 中包含载入的关卡列表。它可处理关卡流送和动态Actor的生成（创建）。
- **AIController 人工智能控制器**, **Brush 画刷**, **GameMode 游戏模式**, **GameState 游戏状态**, **PlayerState 玩家状态**

##### 文档Quick Start小练手([链接](https://docs.unrealengine.com/en-us/Programming/QuickStart?utm_source=launcher&utm_medium=ue&utm_campaign=uelearn))

- 创建一个C++类，选择创建Actor类。并编写代码，实现物体沿z轴方向上下移动
- 可以通过VS19编译或者在UE Editor中编译。
- 在Content Browser C++类中找刚才生成的Actor类。
- 尝试：
  - 利用UPROPERTY暴露物体上下移动的强度。可能需要参考[教程](https://docs.unrealengine.com/en-US/Programming/Tutorials/VariablesTimersEvents)
  - 添加粒子效果
  - 添加X轴和(或)Y轴的周期性位移，再用0.6到1.4的值和DeltaTime相乘。

##### C++编程导学之游戏控制的摄像机 [链接](https://docs.unrealengine.com/en-us/Programming/Tutorials/AutoCamera)

- 创建摄像机

  1. 通过Mode（左上角），选择camera，直接创建。
  2. 或者先创建一个Cube，在添加camera组件

- 创建控制摄像机的C++类
  ```cpp
  const float TimeBetweenCameraChanges = 2.0f;
  const float SmoothBlendTime = 0.75f;
  TimeToNextCameraChange -= DeltaTime;
  if (TimeToNextCameraChange <= 0.0f)
  {
      TimeToNextCameraChange += TimeBetweenCameraChanges;
  
      // Find the actor that handles control for the local player.
      APlayerController* OurPlayerController = UGameplayStatics::GetPlayerController(this, 0);
      if (OurPlayerController)
      {
          if ((OurPlayerController->GetViewTarget() != CameraOne) && (CameraOne != nullptr))
          {
              // Cut instantly to camera one.
              OurPlayerController->SetViewTarget(CameraOne);
          }
          else if ((OurPlayerController->GetViewTarget() != CameraTwo) && (CameraTwo != nullptr))
          {
              // Blend smoothly to camera two.
              OurPlayerController->SetViewTargetWithBlend(CameraTwo, SmoothBlendTime);
          }
      }
  }
  ```
  
- 将上边创建的C++类放置在世界中。再绑定摄像机。

##### C++编程导学之组件和碰撞 [链接](http://api.unrealengine.com/CHN/Programming/Tutorials/Components/)

1. **创建并附加组件**

   - 创建Pawn类
   - 我们现在可以打开 `CollidingPawn.cpp` 并编辑构造函数， **ACollidingPawn::ACollidingPawn** ，通过生成多种有用的 **Components（组件）** 并将它们在层次结构中排列的方式来添加代码。 我们会创建一个 **Sphere Component（球体组件）** 来与物理世界进行互动，使用 **Static Mesh Component（静态网格物体组件）** 来代表碰撞的形状（相当于物体实体），创建一个可以随意开关的 **Particle System Component（粒子系统组件）** ，以及我们可以用来附加 **Camera Component（相机组件）** 的 **Spring Arm Component（弹簧臂组件）** 来控制游戏中的透视图。

   - 注意，粒子系统组件是附属在静态网格上边的.也可以附属在SphereComponent上，区别呢？

2. 配置输入并创建Pawn的移动组件

   - 在该处，我们选择左侧的 **Engine（引擎）** 部分的 **Input（输入）** 选项。 我们需要 **Action Mapping（动作映射）** 来设置粒子系统的切换，两个 **Axis Mappings（轴映射）** 来移动 **Pawn** ，以及一个 **Axis Mapping（轴映射）** 来旋转 **Pawn** 。
   - 创建一个 **Movement Component（移动组件）** 来让它为我们管理移动。 在这个教程中，我们会扩展 **Pawn Movement Component（Pawn移动组件）** 类。 我们首先选择 **File（文件）** 下拉菜单中的 **Add Code to Project（添加代码到项目）** 命令。

3. 编写**Pawn移动组件**行为的代码

   - 我们需要编写的是 **TickComponent** 函数（类似于 **Actor的** **Tick** 函数），以告知如何移动每一帧。在CollidingPawnMovementComponent.h中，我们需要覆盖类定义中的TickComponent

     ```cpp
     void UCollidingPawnMovementComponent::TickComponent(float DeltaTime, enum ELevelTick TickType, FActorComponentTickFunction *ThisTickFunction)
     {
         Super::TickComponent(DeltaTime, TickType, ThisTickFunction);
     
         // 确保一切有效，然后我们能够移动。
         if (!PawnOwner || !UpdatedComponent || ShouldSkipUpdate(DeltaTime))
         {
             return;
         }
     
         // 获取（然后清除）我们在ACollidingPawn::Tick中设置的移动矢量
         FVector DesiredMovementThisFrame = ConsumeInputVector().GetClampedToMaxSize(1.0f) * DeltaTime * 150.0f;
         if (!DesiredMovementThisFrame.IsNearlyZero())
         {
             FHitResult Hit;
             SafeMoveUpdatedComponent(DesiredMovementThisFrame, UpdatedComponent->GetComponentRotation(), true, Hit);
     
             // 如果撞到某个东西，则尝试沿着滑动
             if (Hit.IsValidBlockingHit())
             {
                 SlideAlongSurface(DesiredMovementThisFrame, 1.f - Hit.Time, Hit.Normal, Hit);
             }
         }
     };
     ```
	  
	- 该TickComponent函数利用 **UPawnMovementComponent** 类提供的一些功能强大的功能。
	
	  **ConsumeInputVector** 报告并清除我们用来存储移动输入的内置变量的值。
	
	  **SafeMoveUpdatedComponent** 使用 **虚幻引擎** 物理来移动Pawn移动组件，同时考虑固体障碍物的存在。
	
	  **SlideAlongSurface** 处理在移动导致碰撞时，沿着碰撞表面（如墙壁和坡道）平滑移动所涉及的计算和物理，而不仅仅是停在原位并靠着墙壁或粘附在坡道上。
	
	  Pawn移动组件中包含更多值得尝试的功能，但本教程不需要使用这些功能。而其他一些类，如 **浮动Pawn移动**、**旁观者Pawn移动** 或 **角色移动组件**，可能会提供更多有用示例和想法。
	
4. 结合使用Pawn和组件

   - 为了使用自定义 **Pawn移动组件**，我们首先需要向 **Pawn** 类添加一个变量来进行跟踪。在CollidingPawn.h中的类定义底部，在添加了“OurParticleSystem”变量的附近位置，应该添加：

     ```cpp
     class UCollidingPawnMovementComponent* OurMovementComponent;
     ```

   - 创建Pawn移动组件并将其与Pawn关联起来是十分简单的操作。在 **ACollidingPawn::ACollidingPawn** 底部，可以添加下面的代码：

     ```cpp
     // 创建移动组件实例，并告诉它更新根。
     OurMovementComponent = CreateDefaultSubobject<UCollidingPawnMovementComponent>(TEXT("CustomMovementComponent"));
     OurMovementComponent->UpdatedComponent = RootComponent;
     ```

   - Pawn调用了一个函数 **GetMovementComponent**，这个函数用来使引擎中的其他类能够访问Pawn当前正在使用的Pawn移动组件。

   - 设置好新Pawn移动组件后，创建代码来处理Pawn将接收的输入。

     ```cpp
     void MoveForward(float AxisValue);
     void MoveRight(float AxisValue);
     void Turn(float AxisValue);
     void ParticleToggle();
     
     ////pitch=y, yaw=z, roll=x
     ```

   - 接下来就是将函数与输入事件绑定。重写SetupPlayerInputComponent

     ```cpp
     InputComponent->BindAction("ParticleToggle", IE_Pressed, this, &ACollidingPawn::ParticleToggle);
     
     InputComponent->BindAxis("MoveForward", this, &ACollidingPawn::MoveForward);
     InputComponent->BindAxis("MoveRight", this, &ACollidingPawn::MoveRight);
     InputComponent->BindAxis("Turn", this, &ACollidingPawn::Turn);
     ```

5. 运行。

##### C++编程导学之第一人称射击游戏教程 [链接](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/index.html)

#### 总结

- 第一部分设置项目中，学到的知识
  - PIE名词；另存为关卡；并设置项目中默认加载的关卡
  - 什么是GameMode？通过GameMode输出信息，利用GEngine
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
  - 导入动画时候，要有对应的骨骼。故在导入fbx模型时候，要让虚幻自动（？）生成其对应的骨骼。
  - 事件图表设置Jumping和Runing状态
  - 动画状态机

1. 设置项目

   - [1.1 创建一个项目](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/1/1/index.html)

     - PIE（Play In Editor）
     - 在File菜单中，将当前关卡保存名为FPSMap的地图
     - 在Project Setting中，Map&Modes中将Editor start map设置为FPSMap。

   - [1.2 在VS中打开项目](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/1/2/index.html)

     - 在File菜单中，找到打开VS。
     - 虚幻会自动生成项目名+GameModeBase的代码。**Game Mode 定义游戏的规则和胜利条件。Game Mode 还将设置用于部分基础游戏性框架类型（包括 Pawn、玩家控制器和 HUD）的默认类。**

   - [1.3 添加日志消息](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/1/3/index.html)

     - 找到 名字为  项目名+GameModeBase的h和cpp文件

     - 覆盖AGameModeBase中的StartPlay，显示日志信息

     - ```c++
       GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Hello World, this is FPSGameMode!"));
       ```

   - [1.4 编译游戏](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/1/4/index.html)

     - 您可能会存在疑问：PIE 模式中日志消息为什么没显示在屏幕上？**不显示日志消息的原因是编辑器在开发的现阶段 仍在使用默认 `Game Mode`。**
     - 创建一个基于自定义游戏模式的蓝图

   - [1.5 设置默认游戏模式](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/1/5/index.html)

     - 在 **Edit** 菜单中点击 **Project Settings**。
     - 在 **Project Settings** 标签左侧的 **Project** 标题下点击 **Maps & Modes**。
     - 在 **Default GameMode** 下拉菜单中选择 **刚才创建的GameMode**。

2. 实现角色

   - [2.1 制作新角色](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/1/index.html)

     - File菜单中新建C++类，选择Character，名字为FPSCharacter
     - 在BeginPlay函数中通过GEgine输出调试信息。
     - 将C++类拓展为蓝图类，[参考](http://api.unrealengine.com/CHN/Gameplay/ClassCreation/CodeAndBlueprints/index.html)
     - 在map&mode中，更改default pawn class选择。

   - [2.2 设置轴映射](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/2/index.html)

     - 在 **Project Settings** 标签左侧的 **Engine** 标题下点击 **Input**。
     - 在 **Bindings** 下点击 **Axis Mappings** 旁的加号。
     - 注意x和y轴的方向，W:1,S:-1  D:1,A:-1

   - [2.3 实现移动函数](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/3/index.html)

     - `InputComponent` 是定义如何处理输入数据的组件。`InputComponent` 可附加到需要接收输入的 actor。设置“移动”绑定

       ```c++
       // 调用后将功能绑定到输入
       void AFPSCharacter::SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent)
       {
           Super::SetupPlayerInputComponent(PlayerInputComponent);
       
           // 设置“移动”绑定。
           PlayerInputComponent->BindAxis("MoveForward", this, &AFPSCharacter::MoveForward);
           PlayerInputComponent->BindAxis("MoveRight", this, &AFPSCharacter::MoveRight);
       }
       ```

     - 添加右移函数

       ```c++
       void AFPSCharacter::MoveRight(float Value)
       {
           // 明确哪个方向是“向右”，并记录玩家试图向此方向移动。
           FVector Direction = FRotationMatrix(Controller->GetControlRotation()).GetScaledAxis(EAxis::Y);
           AddMovementInput(Direction, Value);
       }
       ```

     - 测试角色移动

   - [2.4 鼠标摄像机控制](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/4/index.html)

     - 相机移动原理，[参考](https://learnopengl-cn.github.io/01%20Getting%20started/09%20Camera/)
     - 鼠标控制相机只涉及到 Yaw（左右）和Pitch（上下）。
     - character基类中有两个函数来更新状态AddControllerYawInput和AddControllerPitchInput。
     - **在Input中设置Mouse x（鼠标左右移动控制Yaw）-scale为1；Mouse y（鼠标上下移动控制Pitch）-scale为-1.**

   - [2.5 实现角色跳跃](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/5/index.html)

     - 在Input中找到Action Mappings，添加Jump

     - Character基类支持内置的角色跳跃。只要与bPressedJump变量绑定就行。

     - ```c++
       // 设置“动作”绑定。
       PlayerInputComponent->BindAction("Jump", IE_Pressed, this, &AFPSCharacter::StartJump);
       PlayerInputComponent->BindAction("Jump", IE_Released, this, &AFPSCharacter::StopJump);
       ```

   - [2.6 为角色添加模型](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/6/index.html)

     - FBX import

     - 在角色蓝图Character中设置Mesh，Skeletal Mesh设置为刚才导入的骨骼

     - 调整Z 轴 **Location** 设为“-88.0”，使其与 `CapsuleComponent` 对齐。

     - ###### 建议将 `SkeletalMeshComponent` 放置在 `CapsuleComponent` 中，朝向 `ArrowComponent` 面对的相同方向，确保角色在世界场景中正常移动。

   - [2.7 更改摄像机视图](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/7/index.html)

     - 添加Camera组件
     - 并将其附加到胶囊体组件（注意要包含胶囊体的头文件，否则会报错）SetupAttachment
     - 将摄像机放置在眼睛上方不远处 ；**用pawn来控制摄像机旋转。bUsePawnControlRotation **

   - [2.8 为角色添加第一人称模型](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/8/index.html)

     - **此处存在bug**，在C++代码构造函数中更改CastShadow，SetOnlyOwnerSee，SetOwnerNoSee属性后，在基于该C++代码产生的蓝图类中，并不会收到影响。[参考](https://answers.unrealengine.com/questions/541909/getmesh-setownernosee.html)
       - 法1：更改代码后，再重新基于C++代码生成蓝图类
       - 法2：直接再蓝图类中找到相应的属性更改
       - 法3：在BeginPlay中更改响应的属性。
       
     - 添加第一人称角色模型，
     
       ```c++
       // 第一人称模型（手臂），仅对拥有玩家可见。
       UPROPERTY(VisibleDefaultsOnly, Category = Mesh)
       USkeletalMeshComponent* FPSMesh;
       ```
     
     - 配置
     
       ```c++
       // 为拥有玩家创建一个第一人称模型组件。
       FPSMesh = CreateDefaultSubobject<USkeletalMeshComponent>(TEXT("FirstPersonMesh"));
       // 该模型仅对拥有玩家可见。
       FPSMesh->SetOnlyOwnerSee(true);
       // 将 FPS 模型添加到 FPS 摄像机。
       FPSMesh->SetupAttachment(FPSCameraComponent);
       // 禁用部分环境阴影，保留单一模型存在的假象。
       FPSMesh->bCastDynamicShadow = false;
       FPSMesh->CastShadow = false;
       ```
     
     - 在角色蓝图中，设置FPSMesh，并且调整位置。

3. 实现发射物

   - [3.1 为游戏添加发射物](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/3/1/index.html)

     - 添加开火动作映射

     - 添加发射物类（一个Actor类）

       - 添加一个Sphere组件

       - ```c++
         // 使用球体代表简单碰撞。
         CollisionComponent = CreateDefaultSubobject<USphereComponent>(TEXT("SphereComponent"));
         // 设置球体的碰撞半径。
         CollisionComponent->InitSphereRadius(15.0f);
         // 将碰撞组件设为根组件。
         RootComponent = CollisionComponent;
         ```

       - 添加发射物运动组件，UProjectileMovementComponent

       - ```c++
         // 使用此组件驱动该发射物的运动。
         ProjectileMovementComponent = CreateDefaultSubobject<UProjectileMovementComponent>(TEXT("ProjectileMovementComponent"));
         ProjectileMovementComponent->SetUpdatedComponent(CollisionComponent);
         ProjectileMovementComponent->InitialSpeed = 3000.0f;
         ProjectileMovementComponent->MaxSpeed = 3000.0f;
         ProjectileMovementComponent->bRotationFollowsVelocity = true;
         ProjectileMovementComponent->bShouldBounce = true;
         ProjectileMovementComponent->Bounciness = 0.3f;
         ```

       - 设置发射物的初速度

       - ```c++
         // 在发射方向上设置发射物初速度的函数。
         void AFPSProjectile::FireInDirection(const FVector& ShootDirection)
         {
             ProjectileMovementComponent->Velocity = ShootDirection * ProjectileMovementComponent->InitialSpeed;
         }
         ```

     - 绑定开火输入操作

       - 在FPSCharacter中添加Fire函数（内容为空，后边实现）

     - 定义发射物的生成位置

       - 在何处生成发射物？

       - ```c++
         // 从摄像机位置的枪口偏移。
         UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = Gameplay)
         FVector MuzzleOffset;
         ```

       - 发射物类（FPSCharacter及其派生蓝图类了解生成何种发射物）

       - ```c++
         // 生成的发射物类。
         UPROPERTY(EditDefaultsOnly, Category = Projectile)
         TSubclassOf<class AFPSProjectile> ProjectileClass;
         ```

   - [3.2 实现射击](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/3/2/index.html)
   
     - **Fire函数的实现**
       - 先获取摄像机的位置（根据PawnLocation并移动到眼前BaseEyeHeight）和旋转（GetViewRotation）
       - 将MuzzleOffset变化到世界空间，其实就是将偏移量施加和摄像机一样的旋转变化。
       - 将准星稍微上抬（注意Pitch=y，上下变换；yaw=z(circle) roll=x(Tilting your head)）
       - 获取World指针
       - 根据位置，旋转，以及SpawnParams创建AFPSProjectile组件。
       - 此处涉及到了**四元数的旋转变换以及将四元数转化为方向向量**
     - 导入Sphere模型，并且创建蓝图（父类是FPSProjectile）
       - 添加static mesh，设置缩放比，并且在Collision Presets中选择No Collision
     - 在FPSCharacter蓝图中，设置Projectile class。
   
   - [3.3 设置发射物的碰撞和生命周期](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/3/3/index.html)
   
     - AActor中有生命周期，**InitialLifeSpan**
   
     - 编辑发射物的碰撞设置
   
       - 在项目设置中，找到Collision，选择新建碰撞通道，Default Respond设置为block。
   
     - 使用新碰撞通道的设置
   
       - ```c++
         CollisionComponent->BodyInstance.SetCollisionProfileName(TEXT("Projectile"));
         ```
   
   - [3.4 使发射物和世界场景形成交互](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/3/4/index.html)
   
     - 疑惑，碰撞事件的响应函数的参数问题？
     
       - 对OtherComponent施加一个在碰撞点处沿着发射物速度方向的位移。
     
     - 注册碰撞函数
     
       - ```c++
         CollisionComponent->OnComponentHit.AddDynamic(this, &AFPSProjectile::OnHit);
         ```
     
     - 测试发射物碰撞
     
   - [3.5 在视口中添加准星](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/3/5/index.html)
   
     - 导入准星资源（一个贴图）
     - 添加一个HUD类，用来绘制准星纹理。
       - UTexture2D保存对应的纹理
       - FCanvasTileItem保存要绘制纹理的位置，内容，以及颜色等等。
       - 混合模式设置为Translucent
       - 最后调用Canvas->DrawItem
   
4. 添加角色动画

   - [4.1 设置角色动画](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/4/1/index.html)

     - 注意此处的动画，只是两个手臂的动画。**在导入HeroFPP.fbx文件时，记得让虚幻自动生成其骨骼。**

     - 导入动画时，骨骼选择HeroFPP_Skeleton（在导入fbx文件时，由虚幻生成（不确定））。

     - ##### 创建动画蓝图

       - 将 **AnimInstance** 选为父类，并将 **/Game/HeroFPP_Skeleton** 选为目标骨架
       - 将新动画蓝图命名为“Arms_AnimBP”
       - 打开该蓝图，添加两个bool变量

   - [4.2 设置事件图表](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/4/2/index.html)

     - ##### 更新状态变量

       - 使用 **Event Blueprint Update Animation** 节点可在动画更新时对状态变量进行更新，使它们固定与游戏状态同步。 

       - **Try Get Pawn Owner** 添加该节点

       - 从输出引脚连出引线，并在 **快捷菜单** 中选择 **Cast to Character**。

       - 从 **As Character** 输出引脚连出引线并选择 **Get Character Movement**。

       - 从 **Character Movement** 输出引脚连出引线并选择 **Get Movement Mode**。

       - 从 **Movement Mode** 输出引脚连出引线并选择 **Equal (Enum)**。
       
       - ##### 确定角色是否处于下落状态
       
         - ​	将 **Equal (Enum)** 节点上的下拉值设为 **Falling**。
         - 并且设置IsFalling的值
       
       - ##### 确定角色是否处于奔跑状态
         - 	返回 **Cast To Character** 节点，再次从 **As Character** 引脚连出引线。选择 **Get Velocity** 节点。
         - 	如角色不为站立状态，其速度矢量的长度将大于零。因此，从 **Return Value** 矢量输出引脚连出引线并选择 **Vector Length**，将此节点添加到图表。
         - 	并且设置IsRuning的值
     
   - [4.3 添加动画状态机](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/4/3/index.html)
   
     - 在 **我的蓝图** 面板中双击 **AnimGraph** 将其打开。
     - 右键点击图表，在 **情境菜单** 中选择 **状态机 > 添加新状态机...**。
     - 在 **我的蓝图** 面板中右键单击 **新状态机** 并将其命名为“Arms State Machine”。
     - 将“Arms State Machine”节点上的输出执行引脚与 **Final Animation Pose** 节点上的 **Result** 输入执行引脚相连。
     - 双击“Arms State Machine”节点打开其图表进行编辑。
   
   - [4.4 添加动画转换状态](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/4/4/index.html)
   
     - 进入编辑界面（双击“Arms State Machine”节点打开其图表进行编辑）
   
     - 选择添加状态，命名为Idle。
   
     - 双击Idle，在图表区域中单击右键，然后在 **快捷菜单** 中搜索“Idle”。点击 **Play FPP_Idle** 插入该节点。
   
     - 其他几个类似。
   
     - ##### 添加待机到奔跑的转换（从Idle到Run）
   
       - 从 **Idle** 连接引线到 **Run**，创建转换。
       - 双击转换对其进行编辑。
       - 住 Ctrl 键点击 **My Blueprint** 标签中的 **IsRunning**，拖入图表创建一个 **Get Is Running** 节点。
       - 将 **Get Is Running** 节点的输出引脚和 **Result** 节点上的 **Can Enter Transition** 输入引脚连接起来。
       - 从**Run**到**Idle**，则只需要吧IsRuning取反就行。
   
     - ##### 添加待机到跳跃开始的转换
     
       - IsFalling为true，则状态开始变换
     
     - ##### 添加奔跑到跳跃开始的转换
       - IsFalling为true，则状态开始变换
     
     - ##### 添加跳跃开始到跳跃循环的转换
     
       - 搜索并选择 **TimeRemaining for 'FPP_JumpStart'** 节点。获取动画剩余时间（有待验证）
       - 小于0.1时，状态开始变换
     
     - ##### 添加跳跃循环到跳跃结束的转换
     
       - IsFalling为false，则状态开始变换
     
     - ##### 添加跳跃结束到待机的转换
       - 搜索并选择 **TimeRemaining for 'FPP_JumpEnd'** 节点。
     
   - [4.5 关联动画和角色蓝图](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/4/5/index.html)
   
     - 关闭 **Arms_AnimBP** 动画蓝图前进行编译和保存。
     - 前往 **Content Browser** 中的 **Blueprints** 文件夹，打开 **BP_FPSCharacter** 蓝图。
     - 在 **Components** 标签中选择 **FPSMesh**。
     - 将 **FPSMesh** 的 **AnimationBlueprint** 设为刚创建的 **Arms_AnimBP** 动画蓝图。
     - 在 **Defaults** 模式中时，将 **FPSMesh** transform 的 **Location** 改为 {50, -15, -150}，**Rotation** 改为 {0, 25, 350}。

##### C++编程导学之玩家输入和Pawns [链接](http://api.unrealengine.com/CHN/Programming/Tutorials/PlayerInput/index.html)

1. 设置项目
   - ✓ 设置新项目
   - ✓ 在 Visual Studio 中打开项目
   - ✓ 为项目添加日志消息
   - ✓ 编译首个 C++ 类
   - ✓ 设置默认游戏模式

##### C++编程导学之变量，计时器和事件 [链接](https://docs.unrealengine.com/en-US/Programming/Tutorials/VariablesTimersEvents)

- 本节目的是
  1. 将C++代码中的变量和函数传递给虚幻编辑器
  2. 使用计时器延迟或者重复执行代码
  3. Actor之间使用事件交互
  
- ###### 注意在虚幻编辑器中设置的值，将在构造函数调用之后更新。

- 教程1：[创建一个使用计时器的Actor](https://docs.unrealengine.com/en-us/Programming/Tutorials/VariablesTimersEvents/1)

    - 涉及到的变量和声明
    
    ```cpp
    int32 CountdownTime;
    class UTextRenderComponent* CountdownText;
void UpdateTimerDisplay();
    
  void AdvanceTimer();
  void CountdownHasFinished();
  FTimerHandle CountdownTimerHandle;
  ```
  
  - 计时器的初始化
  
    ```cpp
    ACountdown::ACountdown()
    {
        // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
        PrimaryActorTick.bCanEverTick = false;
        CountdownText = CreateDefaultSubobject<UTextRenderComponent>(TEXT("CountdownNumber"));
        CountdownText->SetHorizontalAlignment(EHTA_Center);
        CountdownText->SetWorldSize(150.0f);
        RootComponent = CountdownText;
        CountdownTime = 3;
    }
    ```
  
- 教程2：[将变量和函数公开到编辑器](https://docs.unrealengine.com/en-us/Programming/Tutorials/VariablesTimersEvents/2)

    - UPROPERTY和UFUNCTION，具体参数参考教程

- 教程3：[用蓝图延展和覆盖C++](https://docs.unrealengine.com/en-us/Programming/Tutorials/VariablesTimersEvents/3)

    - 建立蓝图类，并在Content Browser中找到刚才建立的蓝图类，右键选择编辑。
    - 在EventGraph中添加event（在CountdownC++代码中暴露的函数CountdownHasFinished），添加**Spawn Emitter At Location**节点，位置通过**Get Actor Location**设置，并且选择P_Explosion特效。
    - 注意结束时字体显示的是“0”而不是“GO”，因为蓝图类完全取代了C++代码，如果想要调用，在**Countdown Has Finished**右键选择**Add call to parent function**。
    
- 教程4：涉及到迁移工具，默认设备性能分析，GPU性能分析，安卓设备  [链接](https://docs.unrealengine.com/en-us/Programming/Tutorials/VariablesTimersEvents/4)

##### HelloWorld小练手

- 新建关卡后，在编辑-项目设置-地图和模式-Default map中设置默认的关卡
- 每一个组件都是一个AActor，在C++中用GetOwner获取当前actor实例指针。在该例子中使用的是门，可以设置其旋转属性，以达到开关门的效果。
- 更改默认的Pawn在项目设置中，map&mode更改默认游戏模式，选择自定义的Pawn
- 添加聚光源，当在该光源内部放置物体，重量超过25KG，出发机关。碰撞检测用的是triggerVolume(使用蓝图获取的，UPROPERTY(EditAnywhere)),使用GetOverlappingActors获取当前在triggerVolume中的Actor对象,然后再获取每个Actor的重量FindComponentByClass<UPrimitiveComponent>()->GetMass()。当重量达到25KG，开门，如果时间超过1S，关门。
- 为了简单添加开门的渐变效果，将门改为蓝图类。
  - 通过 DECLARE_DYNAMIC_MULTICAST_DELEGATE(FDoorEvent);，声明FDoorEvent事件
  - 通过UPROPERTY(BlueprintAssignable)，告诉蓝图有该事件。
  - 在蓝图中，设置时间轴，设置旋转角度等等。
  - 在C++代码中使用Broadcast激活该事件。
- defaultPawn是虚幻自动生成的游戏角色,使用GetWorld()->GetFirstPlayerController()->GetPawn()获取。
- 实现抓取物体
  - 首先在引擎中，项目设置，找到输入，设置Action Mappings，设置好动作对应的按键。
  - 在DefaultPawn蓝图类中添加PhysicsHandle用来抓取物体。通过GetOwner()->FindComponentByClass<UPhysicsHandleComponent>()获取
  - 输入，通过GetOwner()->FindComponentByClass<UInputComponent>()获取。并且绑定回调方法InputComponennt->BindAction("Grab", IE_Pressed, this, &UGrabber::Grab);
  - GetWorld()->GetFirstPlayerController()->GetPlayerViewPoint获取当前主角的位置以及方向，用来后边的碰撞检测,LineTraceSingleByObjectType来检测碰撞。
  - 如果主角和物体发生了碰撞，通过GrabComponentAtLocationWithRotation来移动物体。SetTargetLocation用来设置物体的位置。

##### 插件 [文档](http://www.52vr.com/extDoc/ue4/CHN/Programming/Plugins/index.html)

- 插件的代码，可以在引擎目录Plugins文件夹找到。

##### 虚幻崩溃

- 1、找到项目目录
  2、删除多余文件，只留下Config、Content、(Debug)、Source、.uproject
- 右键生成sln解决方案，如果要指定VS版本，看[此处](https://gameinstitute.qq.com/community/detail/121783)

- 日志错误如下：解决方案 ： [链接1](https://answers.unrealengine.com/questions/179003/lighting-build-failing-array-index-out-of-bounds.html) [链接2](https://answers.unrealengine.com/questions/758236/all-my-plugins-nodes-get-call-unknown-function-err.html?childToView=759426#answer-759426)
  <img src="01.jpg" style="zoom:80%">