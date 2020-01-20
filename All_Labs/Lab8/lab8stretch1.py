import turtle
import random

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

def printer():
    x = 0
    while x < 20:
        print (fibonacci(x))
        x+=1

def tree(trunklength):
    y = random.randint(15,45)
    x = random.randint(12,18)
    z= random.randint(0,20)
    if trunklength < 5:
        return
    else:
        turtle.forward(trunklength)
        turtle.right(y)
        tree(trunklength-x)
        turtle.left(y+z)
        tree(trunklength-x)
        turtle.right(z)
        turtle.backward(trunklength)
