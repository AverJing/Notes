### C++编程导学 [文档](https://docs.unrealengine.com/en-US/Programming/Tutorials/VariablesTimersEvents/index.html)

#### C++编程导学之变量，计时器和事件 [链接](https://docs.unrealengine.com/en-US/Programming/Tutorials/VariablesTimersEvents)

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

  - 更新时间的函数

    - ```c++
      void ACountdown::AdvanceTimer()
      {
          --CountdownTime;
          UpdateTimerDisplay();
          if (CountdownTime < 1)
          {
              //We're done counting down, so stop running the timer.
              GetWorldTimerManager().ClearTimer(CountdownTimerHandle);
              CountdownHasFinished();
          }
      }
      
      void ACountdown::CountdownHasFinished()
      {
          //Change to a special readout
          CountdownText->SetText(TEXT("GO!"));
      }
      ```

  - 激活计时器

    - ```c++
      GetWorldTimerManager().SetTimer(CountdownTimerHandle, this, &ACountdown::AdvanceTimer, 1.0f, true);
      ```

- 教程2：[将变量和函数公开到编辑器](https://docs.unrealengine.com/en-us/Programming/Tutorials/VariablesTimersEvents/2)

  - UPROPERTY和UFUNCTION，具体参数参考教程

- 教程3：[用蓝图延展和覆盖C++](https://docs.unrealengine.com/en-us/Programming/Tutorials/VariablesTimersEvents/3)

  - 建立蓝图类，并在Content Browser中找到刚才建立的蓝图类，右键选择编辑。
  - 在EventGraph中添加event（在CountdownC++代码中暴露的函数CountdownHasFinished），添加**Spawn Emitter At Location**节点，位置通过**Get Actor Location**设置，并且选择P_Explosion特效。
  - 注意结束时字体显示的是“0”而不是“GO”，因为蓝图类完全取代了C++代码，如果想要调用，在**Countdown Has Finished**右键选择**Add call to parent function**。

- 教程4：涉及到迁移工具，默认设备性能分析，GPU性能分析，安卓设备  [链接](https://docs.unrealengine.com/en-us/Programming/Tutorials/VariablesTimersEvents/4)



#### C++编程导学之第一人称射击游戏教程 [链接](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/index.html)

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

         - 返回 **Cast To Character** 节点，再次从 **As Character** 引脚连出引线。选择 **Get Velocity** 节点。
         - 如角色不为站立状态，其速度矢量的长度将大于零。因此，从 **Return Value** 矢量输出引脚连出引线并选择 **Vector Length**，将此节点添加到图表。
         - 并且设置IsRuning的值

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

#### C++编程导学之组件和碰撞 [链接](http://api.unrealengine.com/CHN/Programming/Tutorials/Components/)

1. **创建并附加组件**

   - 创建Pawn类

   - 我们现在可以打开 `CollidingPawn.cpp` 并编辑构造函数， **ACollidingPawn::ACollidingPawn** ，通过生成多种有用的 **Components（组件）** 并将它们在层次结构中排列的方式来添加代码。 我们会创建一个 **Sphere Component（球体组件）** 来与物理世界进行互动，使用 **Static Mesh Component（静态网格物体组件）** 来代表碰撞的形状（相当于物体实体），创建一个可以随意开关的 **Particle System Component（粒子系统组件）** ，以及我们可以用来附加 **Camera Component（相机组件）** 的 **Spring Arm Component（弹簧臂组件）** 来控制游戏中的透视图。

   - 将Pawn设置为默认玩家控制

     - ```c++
       // 控制默认玩家
           AutoPossessPlayer = EAutoReceiveInput::Player0;
       ```

   - **注意，粒子系统组件是附属在静态网格上边的.也可以附属在SphereComponent上，区别呢？**

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

     - **注意**：与我们目前看到的其他 **组件** 不同的是，不需要将该组件连接到我们自己的组件层级。这是因为其他组件都属于 **场景组件** 类型，本质上需要有物理位置。但 **移动控制器** 不是场景组件，不需要表示物理对象，因此存在于某个物理位置的概念或者能够在物理上连接到另一个组件的概念不适用于这类组件。

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

6. 自由发挥

   - 创建一个自动沿其分类进行轨道移动的组件
     - 此处创建一个ArrowComponent，附属到RootComponent中，即可。
     - **注意在构造函数中创建，如果更改其属性，没有效果。见Problem中的Q2**



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

- 拓展

  - 将摄像机附加到移动Actor上来创建摇臂或移动车镜头。
  - 使用一个[数组](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/TArrays/index.html) 变量来存储摄像机，而不是CameraOne和CameraTwo，这样您就可以遍历任意数量摄像机的序列，而不是仅仅两个。
  - 不要使用[Actor](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Actors/index.html) 指针来存储摄像机，而是创建一个[结构](http://api.unrealengine.com/CHN/Programming/UnrealArchitecture/Reference/Structs/index.html) 来保持指针以及在更改视图之前的时间，并将时间混合到新视图中。


##### C++编程导学之玩家控制的摄像机 [链接](http://api.unrealengine.com/CHN/Programming/Tutorials/PlayerCamera/index.html)

- 1. [附加相机到Pawn](http://api.unrealengine.com/CHN/Programming/Tutorials/PlayerCamera/1/index.html) 

  - 创建一个全新的Pawn，添加**CameraComponent** 和**SpringArmComponent** 组件。并且设置相关参数

    - ```c++
      protected:
          UPROPERTY(EditAnywhere)
          USpringArmComponent* OurCameraSpringArm;
          UCameraComponent* OurCamera;
      ```

      ```c++
      //创建组件
      RootComponent = CreateDefaultSubobject<USceneComponent>(TEXT("RootComponent"));
      OurCameraSpringArm = CreateDefaultSubobject<USpringArmComponent>(TEXT("CameraSpringArm"));
      OurCameraSpringArm->AttachTo(RootComponent);
      OurCameraSpringArm->SetRelativeLocationAndRotation(FVector(0.0f, 0.0f, 50.0f), FRotator(-60.0f, 0.0f, 0.0f));
      OurCameraSpringArm->TargetArmLength = 400.f;
      OurCameraSpringArm->bEnableCameraLag = true;
      OurCameraSpringArm->CameraLagSpeed = 3.0f;
      ```

      ```c++
      OurCamera = CreateDefaultSubobject<UCameraComponent>(TEXT("GameCamera"));
      OurCamera->AttachTo(OurCameraSpringArm, USpringArmComponent::SocketName);
      ```

  - 设置Pawn为默认受控。可以添加这段代码来自动生成本地玩家。

    - ```c++
      //控制默认玩家
      AutoPossessPlayer = EAutoReceiveInput::Player0;
      ```

- 2. [配置输入以控制相机](http://api.unrealengine.com/CHN/Programming/Tutorials/PlayerCamera/2/index.html)

  - 项目设置中，设置**动作以及坐标轴映射**。

- 3. [利用C++代码对输入进行响应](http://api.unrealengine.com/CHN/Programming/Tutorials/PlayerCamera/3/index.html)

  - 变量：记录移动和鼠标的二维向量，以及放大或者缩小的系数，是否放大的bool值。

    - ```c++
      //输入变量
      FVector2D MovementInput;
      FVector2D CameraInput;
      float ZoomFactor;
      bool bZoomingIn;
      ```

  - 输入函数

    - ```c++
      // 输入函数
      void APawnWithCamera::MoveForward(float AxisValue)
      {
          MovementInput.X = FMath::Clamp<float>(AxisValue, -1.0f, 1.0f);
      }
      
      void APawnWithCamera::MoveRight(float AxisValue)
      {
          MovementInput.Y = FMath::Clamp<float>(AxisValue, -1.0f, 1.0f);
      }
      
      void APawnWithCamera::PitchCamera(float AxisValue)
      {
          CameraInput.Y = AxisValue;
      }
      
      void APawnWithCamera::YawCamera(float AxisValue)
      {
          CameraInput.X = AxisValue;
      }
      
      void APawnWithCamera::ZoomIn()
      {
          bZoomingIn = true;
      }
      
      void APawnWithCamera::ZoomOut()
      {
          bZoomingIn = false;
      }
      ```

  - 对输入函数进行绑定处理

    - ```c++
      // 绑定事件到"ZoomIn"
      InputComponent->BindAction("ZoomIn", IE_Pressed, this, &APawnWithCamera::ZoomIn);
      InputComponent->BindAction("ZoomIn", IE_Released, this, &APawnWithCamera::ZoomOut);
      
      //为四条轴绑定对每帧的处理
      InputComponent->BindAxis("MoveForward", this, &APawnWithCamera::MoveForward);
      InputComponent->BindAxis("MoveRight", this, &APawnWithCamera::MoveRight);
      InputComponent->BindAxis("CameraPitch", this, &APawnWithCamera::PitchCamera);
      InputComponent->BindAxis("CameraYaw", this, &APawnWithCamera::YawCamera);
      ```

  - 对每一帧进行更新。

    - ```c++
      //如果按下了放大按钮则放大，否则就缩小
      {
          if (bZoomingIn)
          {
              ZoomFactor += DeltaTime / 0.5f;         //Zoom in over half a second
          }
          else
          {
              ZoomFactor -= DeltaTime / 0.25f;        //Zoom out over a quarter of a second
          }
          ZoomFactor = FMath::Clamp<float>(ZoomFactor, 0.0f, 1.0f);
          // 基于ZoomFactor来混合相机的视域和弹簧臂的长度
          OurCamera->FieldOfView = FMath::Lerp<float>(90.0f, 60.0f, ZoomFactor);
          OurCameraSpringArm->TargetArmLength = FMath::Lerp<float>(400.0f, 300.0f, ZoomFactor);
      }
      ```

      ```c++
      //旋转actor的偏转，这样将会旋转相机，因为相机附着于actor
      {
          FRotator NewRotation = GetActorRotation();
          NewRotation.Yaw += CameraInput.X;
          SetActorRotation(NewRotation);
      }
      
      // 旋转相机的倾斜，但对其进行限制，这样我们将总是向下看
      {
          FRotator NewRotation = OurCameraSpringArm->GetComponentRotation();
          NewRotation.Pitch = FMath::Clamp(NewRotation.Pitch + CameraInput.Y, -80.0f, -15.0f);
          OurCameraSpringArm->SetWorldRotation(NewRotation);
      }
      ```

      ```c++
      // 基于"MoveX"和 "MoveY"坐标轴来处理移动
      {
          if (!MovementInput.IsZero())
          {
              // 把移动输入坐标轴的值每秒缩放100个单位
              MovementInput = MovementInput.SafeNormal() * 100.0f;
              FVector NewLocation = GetActorLocation();
              NewLocation += GetActorForwardVector() * MovementInput.X * DeltaTime;
              NewLocation += GetActorRightVector() * MovementInput.Y * DeltaTime;
              SetActorLocation(NewLocation);
          }
      }
      ```

- 4. [自己动手](http://api.unrealengine.com/CHN/Programming/Tutorials/PlayerCamera/4/index.html)

  - 向玩家提供一个运行键，按住它将增加 **Pawn的** 运动速度。
  - 尝试不同的方式混合自动型和输入驱动型的摄像机运动。这是一个非常深奥的游戏开发领域，有很大的探索空间！
  - 增加、减少或消除 **弹簧组件（Spring Component）** 的滞后，以便更好地理解滞后对摄像机整体感觉的影响程度。
  - 实现少量的周期性运动，可能稍微随机化或者使用 **曲线（Curve）** 资源，以为您的摄像机创建一种手持的感觉。
  - 为您的 **摄像机（Camera）** 提供一定程度的自动旋转，以便摄像机会逐渐移到玩家的移动对象后面，并朝向玩家移动的方向。

