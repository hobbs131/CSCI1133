def earthquakes():
    fileobj = open("all_day.csv", "r")
    mylist=[]
    count = []
    x = 0

    for line in fileobj:
        mylist.append(line.split(','))
    while x < len(mylist):
        print(mylist[x][4],mylist[x][13].replace('"',""))
        x+=1
