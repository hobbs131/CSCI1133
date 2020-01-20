def earthquakes():
    fileobj = open("all_day.csv", "r")
    mylist=[]
    count = 0

    for line in fileobj:
        mylist.append(line)
    x = str(mylist[0])
    newx = x.split(',')
    newx[len(newx)-1]= 'magSource'

    while count < len(newx):
        print(count, newx[count])
        count+=1
