import random


def csv():
    file = input('Enter name of file: ')
    fileobj = open(file, 'w')
    x = 1
    record = ''
    while x <= 1000:
        record+= str(x) + ' '
        record+= str(random.randint(-1000,1000))
        fileobj.write(record)
        fileobj.write('\n')
        record = ''
        x+=1
    fileobj.close()
