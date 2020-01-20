def matrix(n):
    mylist= []
    x = 0
    y = 0
    if n > 0:
        while x < n:
            mylist.append(0)
            x+=1
        while y < n:
            mylist[y]= 1
            print(mylist)
            mylist[y] = 0
            y+=1
    else:
        print('Order cannot be negative')
