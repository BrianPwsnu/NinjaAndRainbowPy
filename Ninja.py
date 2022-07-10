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
#import turtle
#from turtle import*

#turtle.title("rainbow spiral")
#speed(50)
#bgcolor("black")
#r,g,b=255,0,0

#for i in range(255*2):
#    colormode(255)
#    if i<255//3:
#        g+=3
#    elif i<255*2//3:
#        r-=3
#    elif i<255:
#       b+=3
#    elif i<255*4//3:
#        g-=3
#    elif i<255*5//3:
#        r+=3
#    else:
#        b-=3
#    fd(50+i)
#    rt(91)
#    pencolor(r,g,b)

#done()

# |Python program to swap two numbers|
#a = input('Enter value of a: ')
#b = input('Enter value of b: ')

#print('\nOriginal Values \n a=',a,'\n b=',b)

#a,b = b,a

#print('\nAfter Swapping\n a=',a,'\n b=',b)

# |draw heart|
# Import turtle package
#import turtle

# Creating a turtle object(pen)
#pen = turtle.Turtle()


# Defining a method to draw curve
#def curve():
#    for i in range(200):
        # Defining step by step curve motion
#        pen.right(1)
#        pen.forward(1)


# Defining method to draw a full heart
#def heart():
    # Set the fill color to red
#    pen.fillcolor('red')

    # Start filling the color
#    pen.begin_fill()

    # Draw the left line
#    pen.left(140)
#    pen.forward(113)

    # Draw the left curve
#    curve()
#    pen.left(120)

    # Draw the right curve
#    curve()

    # Draw the right line
#    pen.forward(112)

    # Ending the filling of the color
#    pen.end_fill()


# Defining method to write text
#def txt():
    # Move turtle to air
#    pen.up()

    # Move turtle to a given position
#    pen.setpos(-68, 95)

    # Move the turtle to the ground
#    pen.down()

    # Set the text color to lightgreen
#    pen.color('lightgreen')

    # Write the specified text in
    # specified font style and size
#    pen.write("GeeksForGeeks", font=(
#        "Verdana", 12, "bold"))


# Draw a heart
#heart()

# Write text
#txt()

# To hide turtle
#pen.ht()

# |draw logo batman|
import turtle

#initialize method
bat = turtle.Turtle()

#size of pointer and pen
bat.turtlesize(1, 1, 1)
bat.pensize(3)

#screen info
wn = turtle.Screen()
wn.bgcolor("gray")
wn.title("BATMAN")

#colour
bat.color("blue", "black")


#begin filling color
bat.begin_fill()

#turn1
bat.left(90)   # turn pointer direction to left of 90'
bat.circle(50, 85) #draw circle of radius = 50 and 85'
bat.circle(15, 110)
bat.right(180)

#turn 2
bat.circle(30, 150)
bat.right(5)
bat.forward(10) #draw forward line of 10 units

#turn 3
bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)

#turn 4
bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

#turn5
bat.forward(30)
bat.left(55)
bat.forward(10)

#reverse

#turn 5
bat.forward(10)
bat.left(55)
bat.forward(30)

#turn 4
bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)

#turn 3
bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)

#turn 2
bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)

#turn 1
bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)

#end color filling
bat.end_fill()

#end the turtle method
turtle.done()