import turtle

def mouseInput(x,y):
    print(x,',',y)
def main():
    myturtle = turtle.Turtle()
    scr = myturtle.getscreen()
    scr.onclick(mouseInput)
    scr.listen()
