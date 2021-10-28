import turtle
import random
#正方形
from typing import Any, Union

i = 0
j = 0
m = 20
x = 50
y = 10
# while i < 4:
#     turtle.forward(x)
#     turtle.right(90)
#     i += 1

# turtle.pendown()
# while j < 5:
#     turtle.forward(int(x+20))
#     turtle.right(90)
#     turtle.forward(int(y+10))
#     turtle.right(90)
#     turtle.forward(int(x+40))
#     turtle.right(90)
#     turtle.forward(int(y+20))
#     turtle.right(90)
#     x += 40
#     y += 10
#     j += 1

#正方形
turtle.goto(x, 0)
turtle.goto(x, -x)
turtle.goto(0, -x)
turtle.goto(0, 0)

while j < 3:
    mycololist = ['yellow','red','pink','orange','blue']#颜色列表
    randindex = random.randrange(len(mycololist)) #设置随机索引值
    #turtle.begin_fill() #颜色填充
    turtle.color(mycololist[randindex]) #随机赋值给笔画
    turtle.penup()
    turtle.goto(70+m, 10)
    turtle.pendown()
    turtle.goto(70+m, -60-y)
    turtle.goto(-20-m, -60-y)
    turtle.goto(-20-m, 0)
    turtle.goto(-20-m, 10)
    turtle.goto(70+m, 10)
    #turtle.end_fill() #颜色填充
    m += 20
    j += 1
    y += 10

turtle.done()