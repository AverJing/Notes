## Web开发

### HTTP协议简介

- HTML是一种用来定义网页的文本，会HTML，就可以编写网页；

- HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。

  `Elements`显示网页的结构，`Network`显示浏览器和服务器的通信。我们点`Network`，确保第一个小红灯亮着，Chrome就会记录所有浏览器和服务器之间的通信。

  `200`表示一个成功的响应，后面的`OK`是说明。失败的响应有`404 Not Found`：网页不存在，`500 Internal Server Error`：服务器内部出错。

  `Content-Type`指示响应的内容，这里是`text/html`表示HTML网页。请注意，浏览器就是依靠`Content-Type`来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠URL来判断响应的内容，所以，即使URL是`http://example.com/abc.jpg`，它也不一定就是图片。

  HTTP协议同时具备极强的扩展性，虽然浏览器请求的是`http://www.sina.com.cn/`的首页，但是新浪在HTML中可以链入其他服务器的资源，比如`<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">`，从而将请求压力分散到各个服务器上，并且，一个站点可以链接到其他站点，无数个站点互相链接起来，就形成了World Wide Web，简称WWW。

- HTTP格式

  每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。

  当遇到连续两个`\r\n`时，Header部分结束，后面的数据全部是Body。

- HTML简介

  HTML文档就是一系列的Tag组成，最外层的Tag是`<html>`。规范的HTML也包含`<head>...</head>`和`<body>...</body>`（注意不要和HTTP的Header、Body搞混了），由于HTML是富文档模型，所以，还有一系列的Tag用来表示链接、图片、表格、表单等等。

- CSS简介

  CSS是Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现。

- JS简介

  JavaScript是为了让HTML具有交互性而作为脚本语言添加的，JavaScript既可以内嵌到HTML中，也可以从外部链接到HTML中。如果我们希望当用户点击标题时把标题变成红色，就必须通过JavaScript来实现。

### WSGI（Web Server Gateway Interface）接口

1. 浏览器发送一个HTTP请求；

2. 服务器收到请求，生成一个HTML文档；

3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器；

4. 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

   Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

### 使用Web框架

​	有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

​	在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过`request.form['name']`来获取表单的内容。

​	Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等。

​	包含变量`{{ name }}`的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。

​	Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。