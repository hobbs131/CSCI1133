import random
import math

def diceroll():
    dice = random.randint(1,6)
    return dice

def diceroll2():
    dice1 = random.randint(1,6)
    return dice1

def main():
    #y2= outcome()
    #print (y2)
    print("hi")

def outcome():
    count = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    total9 = 0
    total10= 0
    total11 = 0
    total12 = 0

    while (count < 10000):
        x = diceroll()
        y = diceroll2()

        if (x + y== 2):
            total2 += 1
        if (x + y == 3):
            total3 += 1
        if (x + y== 4):
            total4 += 1
        if (x + y== 5):
            total5 += 1
        if (x + y== 6):
            total6 += 1
        if (x + y== 7):
            total7 += 1
        if (x + y== 8):
            total8 += 1
        if (x + y== 9):
            total9 += 1
        if (x + y== 10):
            total10 += 1
        if (x + y== 11):
            total11 += 1
        if (x + y== 12):
            total12 += 1
        count+= 1
    alist = [total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]
    return alist

    if __name__ == '__main__':
        main()
