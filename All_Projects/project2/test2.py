# <Tanner Hobbs Hobbs131>
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the course.

import turtle
import random
import math

def initialboard():
    #draws initial board with initial starting tokens
    squareDrawer()
    numWrite()
    initialStamper()
    board = []
    for x in range(8):
        board.append(['unoccupied']*8)
    board[3][3] = 'white'
    board[3][4] = 'black'
    board[4][4] = 'white'
    board[4][3] = 'black'
    return board

def squareDrawer():
    # draws squares for graphical interface
    square = turtle.Turtle()
    square.speed(0)
    x = -280
    y = 190
    gridmaker = 0
    gridmaker2 = 0



    square.color('green')
    square.penup()


    while gridmaker2 < 8:

        square.sety(y)

        while gridmaker <  8:

            square.setx(x)


            square.pendown()
            square.begin_fill()

            for squarer in range(4):

                square.forward(50)
                square.left(90)
            square.penup()
            square.end_fill()
            x+=60
            gridmaker+=1

        y+=-60
        gridmaker2+=1
        gridmaker= 0
        x=-280

def numWrite():
    # adds graphical interface of numbers 0-7 for row and col
    writer = turtle.Turtle()
    numberwrite = 0
    numberwrite1= 0
    x = -260
    y = 250

    while numberwrite < 8:  # x-roow

        writer.penup()
        writer.setx(x)
        writer.sety(y)
        writer.pendown()
        writer.write(numberwrite)
        x+=60
        numberwrite+=1

    while numberwrite1 < 8: # y-row

        writer.penup()
        writer.setx(-300)
        writer.sety(y-45)
        writer.pendown()
        writer.write(numberwrite1)
        y-=60
        numberwrite1+=1

def converter(row,col):
    # converts row,col to xcor,ycor
    xcor = int(col)*60+-255
    ycor = 215-int(row)*60
    return xcor,ycor

def initialStamper():
    # creates initial starting conditions for black and white
    stamper = turtle.Turtle()
    stamper.penup()
    stamper.setx(-15)
    stamper.sety(35)
    stamper.pendown()
    stamper.shape("circle")
    stamper.shapesize(2,2)
    stamper.stamp()
    stamper.penup()
    stamper.setx(-75)
    stamper.sety(-25)
    stamper.pendown()
    stamper.stamp()
    stamper.color("white")
    stamper.penup()
    stamper.setx(-75)
    stamper.sety(35)
    stamper.pendown()
    stamper.stamp()
    stamper.penup()
    stamper.setx(-15)
    stamper.sety(-25)
    stamper.pendown()
    stamper.stamp()
    stamper.penup()

def stamper(row,col,color):
    #stamps color at given row and col
    xcor,ycor = converter(row,col)
    stamper1 = turtle.Turtle()
    stamper1.color(color)
    stamper1.penup()
    stamper1.setpos(xcor,ycor)
    stamper1.pendown()
    stamper1.shape("circle")
    stamper1.shapesize(2,2)

def isValidMove(board,row,col,color):
    # returns False if inputted row,col is occupied or not on screen.Returns list of squares(row,col) to stamp otherwise
    neighbors = [[1,1],[-1,1],[1,-1],[-1,0],[1,0],[-1,-1],[0,1],[0,-1]]
    flippedTokens = []
    row = int(row)
    col = int(col)

    if color == 'white':
        otherColor = 'black'
    elif color == 'black':
        otherColor= 'white'

    if not onScreen(row,col) or board[row][col] != 'unoccupied':
        return False

    flippedTokens.append([row,col])

    for rowCheck,colCheck in neighbors: # checks status of all possible neighbors

        rowNeighbor = row
        colNeighbor = col

        rowNeighbor+= rowCheck
        colNeighbor+= colCheck

        if onScreen(rowNeighbor,colNeighbor) and board[rowNeighbor][colNeighbor]== otherColor:
            # checks to see if the computer has a token next to ours
            rowNeighbor+=rowCheck
            colNeighbor+=colCheck

            if not onScreen(rowNeighbor,colNeighbor):
                #  check other directions if not on the screen
                continue

            while board[rowNeighbor][colNeighbor]== otherColor:
                # keep going down line until your color token is hit
                rowNeighbor+= rowCheck
                colNeighbor+= colCheck

                if not onScreen(rowNeighbor,colNeighbor):
                    break
            if not onScreen(rowNeighbor,colNeighbor):
                # our color token was not hit, so not valid move.
                continue

            if board[rowNeighbor][colNeighbor]== color:
                while True:
                    # go back to starting position appending each token to be flipped.
                    rowNeighbor-= rowCheck
                    colNeighbor-= colCheck

                    if rowNeighbor == row and colNeighbor == col:
                        break
                    flippedTokens.append([rowNeighbor,colNeighbor])


    if len(flippedTokens)== 1: # not a valid move as the row,col was already appended (explains len==1)
        return False
    return flippedTokens

def finalScore(board):
    # prints the final score at end of game
    white = 0
    black = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'white':
                white+=1
            elif board[row][col] == 'black':
                black+=1
    if white > black:
        print("White wins",white,"-",black)
    elif black > white:
        print("Black wins",black,"-",white)
    else:
        print("It's a tie!",black,"-",white) # prints who won the game and the final score

def onScreen(row,col):
    # determines and returns true if an inputted row and col is valid(on screen/board)
    if row>=0 and row <= 7 and col >=0 and col<=7:
        return True

def selectNextPlay(board):
    # returns random move (for computer) to be played out of valid moves
    color = 'white'
    availableMoves = getValidMoves(board,color)
    rowC,colC = availableMoves[random.randint(0,len(availableMoves)-1)]

    return rowC,colC

def getValidMoves(board,color):
    # goes through each [row,col] on board,appends to moves if it is a "valid" move
    moves = []

    for row in range(8):
        for col in range(8):
            if isValidMove(board,row,col,color) != False:
                moves.append([row,col])
    return moves

def flipper(board,row,col,color):
    #stamps color at given row,col and "flips" tokens in the line.
    flipped = isValidMove(board,row,col,color)

    if flipped == False: # if False, then it is not a valid move.
        return False
    for rowA,colA in flipped:
        stamper(rowA,colA,color)
        board[rowA][colA]= color

    return board

def main():
    newboard = initialboard()
    window = turtle.Screen()
    playerturn= True
    playerColor= 'black'
    compColor = 'white'
    window.delay(20) # slows down placement of tokens

    while True:
         # continues until no more valid moves
        if playerturn == True: # players move
            if getValidMoves(newboard,playerColor) == []:
                break
            print(getValidMoves(newboard,playerColor)) # for reviewing game
            rowinput,colinput = window.textinput("Othello Game", "Enter row,col").split(',')

            if isValidMove(newboard,rowinput,colinput,playerColor)!= False:
                newboard = flipper(newboard,rowinput,colinput,playerColor)
            else:
                continue
            playerturn = False


        else: # computers move
            if getValidMoves(newboard,compColor) == []:
                break
            row1,col1 = selectNextPlay(newboard)
            newboard = flipper(newboard,row1,col1,'white')
            playerturn = True

    finalScore(newboard)

if __name__ == '__main__':
    main()
