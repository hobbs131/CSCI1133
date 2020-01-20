import turtle



import random
count=0

def Drunkwalk():
    x= random.randint(1,4)

    if (x == 1):
        turtle.left(0)
        turtle.forward(20)

    if (x == 2):
        turtle.left(90)
        turtle.forward(20)

    if (x == 3):
        turtle.left(180)
        turtle.forward(20)

    if (x == 4):
        turtle.left(270)
        turtle.forward(20)


while abs(turtle.xcor()) !=450 and abs(turtle.ycor()) != 400:
    Drunkwalk()
    count= count + 1
    print (count*20)
