import turtle

def Amount(n,count):

    while (n >= count):
        Squares()
        count = count + 1

def Drawsquare():

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)



def Squares():
        Drawsquare()
        turtle.left(36)
        
