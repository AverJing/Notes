# 第一个Django应用

## 环境搭建

由于我Python环境使用的是[Anaconda](https://github.com/pypa/virtualenv/issues/1139)，故系统路径一定要设置好。某些包是在Lib下的，记得配置，比如pip。

## Part01： 请求与响应
- 1. 新建项目
VS中直接新建空的Django项目，可以参考微软官方[文档](https://docs.microsoft.com/zh-cn/visualstudio/python/learn-django-in-visual-studio-step-05-django-authentication?view=vs-2017)。或者
$ django-admin startproject mysite
 <img src="01.jpg" style="zoom: 100%" div align="center">

- 2. 启动开发服务器
$ python manage.py runserver
Django提供了一个用于开发的web服务器，使你无需配置一个类似Ngnix的线上服务器，就能让站点运行起来。
Django的开发服务器具有自动重载功能，当你的代码有修改，每隔一段时间服务器将自动更新。

- 3. 创建应用
$ python manage.py startapp polls
VS中也提供GUI操作。

- 4. 编写第一个视图
在polls/views.py中编写视图。为了调用该视图，我们还需要配置相应路由，在polls/urls.py中更改。
接下来，需要在主urls中添加urlpattern条目。
此处作者给出url的参数解释。

## Part02： 模型与后台管理
- 1. 数据库安装
先暂时使用默认的SQlite。可在settings中修改。
 <img src="02.jpg" style="zoom: 100%" div align="center">

- 2. 创建模型
Django通过自定义Python类的形式来定义具体的模型，每个模型的物理存在方式就是一个Python的类Class，每个模型代表数据库中的一张表，每个类的实例代表数据表中的一行数据，类中的每个变量代表数据表中的一列字段。Django通过模型，将Python代码和数据库操作结合起来，实现对SQL查询语言的封装。也就是说，你可以不会管理数据库，可以不会SQL语言，你同样能通过Python的代码进行数据库的操作。Django通过ORM对数据库进行操作，奉行代码优先的理念，将Python程序员和数据库管理员进行分工解耦。

- 3. 启用模型
创建模型，Django会做两件事：创建该app对应的数据库表结构；为Question和Choice对象创建基于Python的数据库访问API。
将polls加入INSTALLED_APPS（# mysite/settings.py）。
$ python manage.py makemigrations polls
通过运行makemigrations命令，相当于告诉Django你对模型有改动，并且你想把这些改动保存为一个“迁移(migration)”。（migrations是Django保存模型修改记录的文件，这些文件保存在磁盘上。在例子中，它就是polls/migrations/0001_initial.py，你可以打开它看看，里面保存的都是人类可读并且可编辑的内容，方便你随时手动修改。）
接下来有一个叫做migrate的命令将对数据库执行真正的迁移动作。$ python manage.py migrate

- 4. 使用模型的API
尝试使用Django提供的数据库访问API，可以进入Python的shell，输入$ python manage.py shell。
大概命令如下：
	Question.objects.all()；注意查看廖雪峰老师定制类，可以实现类的自定义输出。
	save方法。
	Question.objects.filter(id=1)
	Question.objects.filter(question_text__startswith='What')
	Question.objects.get(pub_date__year=current_year)
	Question.objects.get(pk=1)，pk代表主键
	q = Question.objects.get(pk=1)；q.choice_set.create(choice_text='Not much', votes=0)
	# API会自动进行连表操作，通过双下划线分割关系对象。连表操作可以无限多级，一层一层的连接。
	核心部分，详细信息看教程。

- 5. admin后台管理站点
	- 1. 创建管理员用户
		$ python manage.py createsuperuser
	- 2. 启动开发服务器。
		访问admin/，为了站点的安全，修改其中admin.site.urls对应的正则表达式
	- 3. 进入admin站点
		当前只有两个可编辑的内容：groups和users。它们是django.contrib.auth模块提供的身份认证框架。
	- 4. 在admin中注册投票应用
		在polls/admin.py文件，加入admin.site.register(Question)
