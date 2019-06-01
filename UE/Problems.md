#### 问题汇总

- #####Q1  虚幻默认场景中的Sky Sphere，如果把它删除以后，如何在重新找回？
  
  - 在ContentBrower中右下角“视图选项”中，选择显示“引擎内容”，找到BP_Sky_Sphere，拖拽到场景中，但是你会发现场景是黑的，为什么？双击打开蓝图设置，在Create Dynamic Material Instance中找到Source Material找到名为M_Sky_Panning_Clouds2的材质。还要在属性-默认-Directional Light Actor中选择Light Source（定向光照）。
  
- ##### Q2 [2.8 为角色添加第一人称模型](http://api.unrealengine.com/CHN/Programming/Tutorials/FirstPersonShooter/2/8/index.html)

  - **此处存在bug**，在C++代码构造函数中更改CastShadow，SetOnlyOwnerSee，SetOwnerNoSee属性后，在基于该C++代码产生的蓝图类中，并不会收到影响。[参考](https://answers.unrealengine.com/questions/541909/getmesh-setownernosee.html)
    - 法1：更改代码后，再重新基于C++代码生成蓝图类
    - 法2：直接再蓝图类中找到相应的属性更改
    - 法3：在BeginPlay中更改响应的属性。

