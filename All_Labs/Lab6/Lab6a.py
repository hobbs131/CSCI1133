import turtle

def showmatrix(m):
    myturtle= turtle.Turtle()
    screen = myturtle.getscreen()
    screen.tracer(0)
    outerlist = 0
    xposition = 0
    yposition = 0
    innerlist = 0
    myturtle.setx(xposition)
    myturtle.sety(yposition)

    while outerlist <= len(m):
        xposition = 0
        while innerlist <= len(m):
            if  m[outerlist][innerlist]!= 0:
                myturtle.dot()
                xposition += 15
                myturtle.setx(xposition)
                innerlist+= 1


            outerlist+=1
            ypostion+= 15
            myturtle.sety(yposition)
    update()
