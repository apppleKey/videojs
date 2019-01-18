from  turtle import *

#海龟绘图

# 画笔宽(4)
width(4)
# 前进200
forward(200)
# 右转(90度)
right(90)

pencolor('red')
forward(200)
right(90)

pencolor('pink')
forward(200)
right(90)

pencolor('blue')
forward(200)
right(90)

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
speed('fastest')
# 循环喂狗,调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()