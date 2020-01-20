import math

def emul(a,b):
    total = 0
    if (a < 0 and b < 0):
        a = a * -1
        b = b * -1
    while (b != 0):
        if (b%2 != 0):
            total += a
            a = a * 2
            b = b // 2
        elif (b%2==0):
            a = a * 2
            b = b // 2
        if a < 0 or b < 0:
            print (total)
        else:
            print (total)
