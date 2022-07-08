# |Ninja Design With Python|
#import turtle

#ninja = turtle.Turtle()

#ninja.speed(80)

#for i in range(180):
#    ninja.forward(100)
#    ninja.right(30)
#    ninja.forward(20)
#    ninja.left(60)
#    ninja.forward(50)
#    ninja.right(30)

#    ninja.penup()
#    ninja.setposition(0, 0)
#    ninja.pendown()

#    ninja.right(2)

#turtle.done()

# |Rain Bow Spiral With Python|
import turtle
from turtle import*

turtle.title("rainbow spiral")
speed(50)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(50+i)
    rt(91)
    pencolor(r,g,b)

done()