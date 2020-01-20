# Tanner Hobbs Hobbs131

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course

# Graders note: all exam and extra credit tasks completed.


from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

class LaserBeam(RawTurtle):
    def __init__(self,canvas,x,y,direction,dx,dy):
        super().__init__(canvas)
        self.penup()
        self.goto(x,y)
        self.setheading(direction)
        xval = math.cos(math.radians(direction))
        yval = math.sin(math.radians(direction))
        self.color("Green")
        self.lifespan = 200

       # SOH-CAH-TOA used to derive substitute expressions for dx and dy.
       # dx^2+dy^2 = d^2, so mult.dx/dy by 2 to get 2d, or twice speed of tiny.
       # +xval/yval to allow shooting when not moving.
        self.__dx = (xval*math.sqrt(dx*dx+dy*dy)) * 2 + xval
        self.__dy = (yval*math.sqrt(dx*dx+dy*dy)) * 2 + yval

        self.shape("laser")

    # Accessor methods for lifespan,dx,dy,and radius.
    def getLifeSpan(self):
        return self.lifespan

    def getDX(self):
        return self.__dx

    def getDY(self):
        return self.__dy

    def getRadius(self):
        return 4

    # Moves laser partially, depleting lifespan by 1.
    def moveLaser(self):
            screen = self.getscreen()
            x = self.xcor()
            y = self.ycor()
            x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
            y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
            self.lifespan = self.lifespan - 1
            self.goto(x,y)

class Ghost(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y,size):
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.__size = size
        if self.__size==3:
            self.shape("blueghost.gif")
        elif self.__size==2:
            self.shape("pinkghost.gif")

    #Moves the ghost from its current position to a new position
    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)

    #returns the apprximate "radius" of the Ghost object
    def getRadius(self):
        return self.__size * 10 - 5

    #set methods are mutator methods
    def setDX(self,dx):

        self.__dx = dx

    def setDY(self,dy):
        self.__dy = dy

    #get methods are accessor methods
    def getDX(self):

        return self.__dx

    def getDY(self):
        return self.__dy



class FlyingTurtle(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y, size):
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.color("purple")
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.__size = size
        self.shape("turtle")

    #set methods are mutator methods
    def setDX(self,dx):

        self.__dx = dx

    def setDY(self,dy):
        self.__dy = dy

    #get methods are accessor methods
    def getDX(self):

        return self.__dx

    def getDY(self):
        return self.__dy


    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)

    def turboBoost(self):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))

        # correct boost implementation
        # turtle angle is in first quadrant
        if x > 0 and y >0:
            self.__dx = abs(self.__dx) + x
            self.__dy = abs(self.__dy) + y

        # turtle angle is in second quadrant
        elif x < 0 and y > 0:
            self.__dx = -abs(self.__dx) + x
            self.__dy = abs(self.__dy)+ y

        # turtle angle is in third quadrant
        elif x < 0 and y < 0:
            self.__dx = -abs(self.__dx) + x
            self.__dy = -abs(self.__dy) + y

        # turtle angle is in fourth quadrant
        else:
            self.__dx = abs(self.__dx) + x
            self.__dy = -abs(self.__dy) + y


    def stopTurtle(self):
        angle = self.heading()
        self.__dx = 0
        self.__dy = 0

    def getRadius(self):
        return 2

def main():

    # Start by creating a RawTurtle object for the window.
    firstwindow = tkinter.Tk()
    firstwindow.title("Turtle Saves the World!")
    canvas = ScrolledCanvas(firstwindow,600,600,600,600)
    canvas.pack(side = tkinter.LEFT)
    t = RawTurtle(canvas)
    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("blueghost.gif")
    screen.register_shape("pinkghost.gif")
    screen.register_shape("laser",((-2,-4),(-2,4),(2,4),(2,-4)))
    frame = tkinter.Frame(firstwindow)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    scoreVal = tkinter.StringVar()
    scoreVal.set("0")
    scoreTitle = tkinter.Label(frame,text="Score")
    scoreTitle.pack()
    scoreFrame = tkinter.Frame(frame,height=2, bd=1, relief=tkinter.SUNKEN)
    scoreFrame.pack()
    score = tkinter.Label(scoreFrame,height=2,width=20,textvariable=scoreVal,fg= "Yellow",bg="black")
    score.pack()
    livesTitle = tkinter.Label(frame, text="Extra Lives Remaining")
    livesTitle.pack()
    livesFrame = tkinter.Frame(frame,height=30,width=60,relief=tkinter.SUNKEN)
    livesFrame.pack()
    livesCanvas = ScrolledCanvas(livesFrame,150,40,150,40)
    livesCanvas.pack()
    livesTurtle = RawTurtle(livesCanvas)
    livesTurtle.ht()
    livesScreen = livesTurtle.getscreen()
    life1 = FlyingTurtle(livesCanvas,0,0,-35,0,0)
    life2 = FlyingTurtle(livesCanvas,0,0,0,0,0)
    life3 = FlyingTurtle(livesCanvas,0,0,35,0,0)
    lives = [life1, life2, life3]
    t.ht()
    screen.tracer(10)

    #Tiny Turtle!
    flyingturtle = FlyingTurtle(canvas,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY,3)

    #A list to keep track of all the ghosts
    ghosts = []

    #Create some ghosts and randomly place them around the screen
    for numofghosts in range(6):
        dx = random.random()*6  - 4
        dy = random.random()*6  - 4
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        ghost = Ghost(canvas,dx,dy,x,y,3)

        ghosts.append(ghost)

    # A list to keep track of pink ghosts
    pinkGhosts = []

    # create 12 pink ghosts, hide them from the screen.
    for numofpinkghosts in range(12):
        dx = (random.random()*6 - 4)
        dy = (random.random()*6 - 4)
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        pinkGhost = Ghost(canvas,dx,dy,x,y,2)
        pinkGhost.ht()
        pinkGhosts.append(pinkGhost)

    # List to keep track of lasers that are 'alive'
    lasersInPlay = []

    # Lists for implementation of task 10
    revealedGhosts = []
    hitPinkGhosts = []
    fractureMultiplier = [-1]


    def play():
        #start counting time for the play function
        ##LEAVE THIS AT BEGINNING OF play()

        start = datetime.datetime.now()
        deadLasers = []

        # if you have lives remaining when you hit all pink ghosts, then you win
        if len(hitPinkGhosts)== 12 and len(lives) != 0:
            tkinter.messagebox.showinfo("You win!!","You saved the world!")
            return

        # if you lose all lives, you lose the game.
        if len(lives) == 0:
            tkinter.messagebox.showinfo("You Lost...","Sadly, you did not save the world.")
            return

        # Move the turtle
        flyingturtle.move()

        # Check status of each ghost
        for each_ghost in ghosts:

            # If the ghost collides with tiny, 'delete' the ghost, 'spawn' two pink ones and lose a life.
            if intersect(flyingturtle,each_ghost):
                flyingturtle.stopTurtle()
                tkinter.messagebox.showinfo("Uh-Oh!","You Lost a Life!")
                lives.pop(0).ht()
                each_ghost.ht()
                ghosts.remove(each_ghost)

                # Spawns 'fractured' pink ghosts.
                for twopinkghosts in range(2):

                    # Two pink ghosts set at same speed 90 deg. to left and right of direction of ghost.
                    pinkGhosts[len(revealedGhosts)].setDX(each_ghost.getDY()*fractureMultiplier[0])
                    pinkGhosts[len(revealedGhosts)].setDY(each_ghost.getDX()*fractureMultiplier[0]*-1)

                    # Sets position of pink ghosts 10 (x,y) units in opposite direction of ghosts movement
                    # to avoid collision off spawn.
                    pinkGhosts[len(revealedGhosts)].setpos(each_ghost.xcor()+-10*each_ghost.getDX(),each_ghost.ycor()+-10*each_ghost.getDY())
                    pinkGhosts[len(revealedGhosts)].st()

                    # Uses length of revealedGhosts as a way to iterate through pinkGhosts.
                    revealedGhosts.append(pinkGhosts[len(revealedGhosts)])

                    # Set fractureMultiplier to spawn other pink ghost 90 deg.
                    # From ghost and 180 deg from existing pink ghost.
                    fractureMultiplier[0] = 1

                # Reset value once both pink ghosts have spawned.
                fractureMultiplier[0] = -1

        # If a pink ghost is visible on screen and collided with
        # That ghost is 'deleted' and a life is lost.
        for each_ghost in pinkGhosts:

            if each_ghost.isvisible():

                if intersect(flyingturtle,each_ghost):
                    flyingturtle.stopTurtle()
                    tkinter.messagebox.showinfo("Uh-Oh!","You Lost a Life!")
                    lives.pop(0).ht()
                    each_ghost.ht()
                    hitPinkGhosts.append(each_ghost)

        # Move laser if it interesects with the ghost, 'delete' laser and ghost
        for each_laser in lasersInPlay:

            # Continues until lifespan is depleted.
            while each_laser.getLifeSpan() != 0:
                each_laser.moveLaser()

                # Checks to see if laser obj. intersects any ghost in play.
                for each_ghost in ghosts:

                    # 'Deletes' ghost and laser upon intersection and updates score.
                    if intersect(each_laser,each_ghost):
                        each_laser.lifespan = 0
                        each_laser.goto(-screenMinX*2,-screenMinY*2)
                        each_laser.ht()
                        scoreval = int(scoreVal.get()) + 20
                        scoreVal.set(str(scoreval))
                        ghosts.remove(each_ghost)
                        each_ghost.ht()

                        # Using same logic as when collided with, if a laser hits a ghost, two pink ghosts are 'spawned' in its place.
                        for twopinkghosts in range(2):
                            pinkGhosts[len(revealedGhosts)].setDX(each_ghost.getDY()*fractureMultiplier[0])
                            pinkGhosts[len(revealedGhosts)].setDY(each_ghost.getDX()*fractureMultiplier[0]*-1)
                            pinkGhosts[len(revealedGhosts)].setpos(each_ghost.xcor(),each_ghost.ycor())
                            pinkGhosts[len(revealedGhosts)].st()
                            revealedGhosts.append(pinkGhosts[len(revealedGhosts)])
                            fractureMultiplier[0] = 1
                        fractureMultiplier[0] = -1

                # Checks to see if laser obj. intersects any pink ghost in play
                for each_pink_ghost in pinkGhosts:

                    # If ghost is visible on screen and hit by laser, 'delete' ghost and laser and update score.
                    if each_pink_ghost.isvisible():
                        if intersect(each_laser,each_pink_ghost):
                            each_laser.lifespan = 0
                            each_laser.goto(-screenMinX*2,-screenMinY*2)
                            each_laser.ht()
                            scoreval = int(scoreVal.get()) + 30
                            scoreVal.set(str(scoreval))
                            hitPinkGhosts.append(each_pink_ghost)
                            each_pink_ghost.ht()

            # Whether or not a ghost is hit, laser is added to Deadlasers, removed from lasersInPlay, and hidden.
            deadLasers.append(each_laser)
            lasersInPlay.remove(each_laser)
            each_laser.goto(-screenMinX*2,-screenMinY*2)
            each_laser.ht()

        #Move the ghosts
        for each_ghost in ghosts:
                each_ghost.move()

        # Move the pink ghosts
        for each_ghost in pinkGhosts:
                each_ghost.move()


        #stop counting time for the play function
        ##LEAVE THIS AT END OF ALL CODE IN play()
        end = datetime.datetime.now()
        duration = end - start

        millis = duration.microseconds / 1000.0

        # Set the timer to go off again
        screen.ontimer(play,int(10-millis))


    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play, 5)

    #Turn turtle 7 degrees to the left
    def turnLeft():
        flyingturtle.setheading(flyingturtle.heading()+7)

    #Turn turtle 7 degrees to right
    def turnRight():
        flyingturtle.setheading(flyingturtle.heading()-7)

    #turboBoost turtle
    def forward():
        flyingturtle.turboBoost()

    #stop Turtle
    def stop():
        flyingturtle.stopTurtle()

    # Fire laser
    def fireLaser():
        laser = LaserBeam(canvas,flyingturtle.xcor(),flyingturtle.ycor(),flyingturtle.heading(),flyingturtle.getDX(),flyingturtle.getDY())
        lasersInPlay.append(laser)

    # Checks to see if two obj. have intersected
    def intersect(obj1, obj2):
        if math.sqrt((obj2.xcor()-obj1.xcor())**2+(obj2.ycor()-obj1.ycor())**2) <= obj1.getRadius()+obj2.getRadius():
            return True

    #Call functions above when pressing relevant keys
    screen.onkeypress(turnLeft,"Left")
    screen.onkeypress(forward,"Up")
    screen.onkeypress(stop, "Down")
    screen.onkeypress(turnRight, "Right")
    screen.onkeypress(fireLaser,"")
    screen.listen()
    tkinter.mainloop()

if __name__ == "__main__":
    main()
