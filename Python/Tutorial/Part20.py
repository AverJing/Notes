'''
# WSGI
def application(environ, start_response):
    start_response('200 OK',  [('Context-Type', 'text/html')])
    return ['<h1>hello, %s!</h1>' %(environ['PATH_INFO'][1:] or 'web')]
    #body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    #return [body.encode('utf-8')]

from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000')

# 开始监听HTTP请求：
httpd.serve_forever()
'''

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='admin' and  request.form['password'] == 'password':
        return '<h3>Hello, Admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
