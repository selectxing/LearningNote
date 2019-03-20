import turtle as t
import time

t.setup(1500, 1400, 0, 0) #画布大小、位置。参数说明：width,height,startx,starty
t.pensize(30) #画笔宽度。别名：turtle.width()
t.pencolor("green") #画笔颜色。参数可选颜色字符串、RGB小数值、整数值
t.seth(-40) #画笔行进方向

'''
t.circle(50, 270, steps=10)
t.lt(90)
t.fd(100)
'''

#太阳花
def drawSunFlower():
    t.color("red", "yellow")
    t.speed(10)
    t.begin_fill()
    for _ in range(50):
        t.forward(200)
        t.left(170)
    end_fill()
    time.sleep(1)

#小蟒蛇
def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        t.circle(rad, angle)
        t.circle(-rad, angle)
    t.circle(rad, angle/2)
    t.forward(rad/2)  # 直线前进
    t.circle(neckrad, 180)
    t.forward(rad/4)

#drawSunFlower()
drawSnake(70, 80, 2, 15)

t.done()