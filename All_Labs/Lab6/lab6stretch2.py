import random
def matrix(n,x):
    mylist= []
    x = 0
    y = 0
    if n > 0:
        while x < n:
            mylist.append(0)
            x+=1
        while y < n:

            mylist[random.randint(0, n-1)]= x
            print(mylist)
            y+=1
    else:
        print('Order cannot be negative')
