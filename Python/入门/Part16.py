'''
#https://stackoverflow.com/questions/52902627/e1101module-turtle-has-no-forward-member
from turtle import Turtle, mainloop, done

t = Turtle()
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(200)
    t.left(130)
    if abs(t.pos()) < 1:#回到原点
        break
t.end_fill()
done()
'''

'''
# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
'''

'''
from turtle import *

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()
'''

'''
from turtle import *

colormode(255)

lt(90)

width(10)

r,g,b=0,0,0

pencolor(r,g,b)

l = 120
s = 45
lv = 10

pu()
bk(l)
pd()
fd(l)


def draw_tree(l, level):
    global r,g,b
    w = width()

    width(w*3/4)

    r+=1
    g+=2
    b+=3
    pencolor(r%200,g%200,b%200)

    l *=  3/4

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level+1)

    bk(l)#回来的时候还会继续画图吗？  是否考虑先抬笔？
    rt(2*s)
    fd(l)

    if level < lv:
        draw_tree(l,level+1)
    bk(l)
    lt(s)

    width(w)


speed("fastest")
draw_tree(l,4)

done()
'''

'''
from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t,t,t)
    pensize(n/4)
    fd(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n-1, d)
        left(b+c)
        tree(n-1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n,n,n)
        circle(2)
        left(90)
    pu()
    bk(l)

bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
#tracer(0,0)
left(90)
pu()
bk(300)
tree(13,100)
done()
'''

from turtle import *
from random import *
from math import *

def tree(n, l):
    pd() # 下笔
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
    forward(l) # 画树枝


    if n > 0:
        b = random() * 15 + 10 # 右分支偏转角度
        c = random() * 15 + 10 # 左分支偏转角度
        d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        tree(n - 1, d)
        # 左转一定角度，画左分支
        left(b + c)
        tree(n - 1, d)

        # 转回来
        right(c)
    else:
        # 画叶子
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n*0.8, n*0.8)
        circle(3)
        left(90)

        # 添加0.3倍的飘落叶子
        if(random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)


            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
            circle(2)
            left(90)
            pu()

            #返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)

    pu()
    backward(l)# 退回

bgcolor(0.5, 0.5, 0.5) # 背景色
ht() # 隐藏turtle
speed(0) # 速度，1-10渐进，0最快
tracer(0, 0)
pu() # 抬笔
backward(100)
left(90) # 左转90度
pu() # 抬笔
backward(300) # 后退300
tree(12, 100) # 递归7层
done()

