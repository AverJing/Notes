#### 问题汇总

- 虚幻默认场景中的Sky Sphere，如果把它删除以后，如何在重新找回？
  - 在ContentBrower中右下角“视图选项”中，选择显示“引擎内容”，找到BP_Sky_Sphere，拖拽到场景中，但是你会发现场景是黑的，为什么？双击打开蓝图设置，在Create Dynamic Material Instance中找到Source Material找到名为M_Sky_Panning_Clouds2的材质。还要在属性-默认-Directional Light Actor中选择Light Source（定向光照）。

