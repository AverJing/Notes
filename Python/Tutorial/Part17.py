'''
import socket

#create a socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect
s.connect(('www.baidu.com', 80))

# post data
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

# receive data
buffer = []
while True:
    #receive max 1k once
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#close connection
s.close()


header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('baidu.html', 'wb') as f:
    f.write(html)
'''

#with open('hello.txt', 'w') as f:
    #f.write("hello world!")
'''
f = open('hello.txt', 'w+')
f.write('Hello, world!')
f.close()
'''