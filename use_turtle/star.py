from turtle import *


def draw_start(x, y):
    pu()
    goto(x, y)
    pd()
    seth(0)  # set heading: 0
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 250, 50):
    draw_start(x, 0)
done()
