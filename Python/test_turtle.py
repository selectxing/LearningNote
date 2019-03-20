import turtle as t
import time


t.circle(50, 270, steps=10)
t.lt(90)
t.fd(100)


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
t.setup(1500, 1400, 0, 0)
t.pensize(30)  # 画笔尺寸
t.pencolor("green")
t.seth(-40)    # 前进的方向
drawSnake(70, 80, 2, 15)

t.done()