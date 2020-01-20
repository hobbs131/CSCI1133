def choose(n,k):
    if k==0 or k==n:
        return 1
    else:
        return choose(n-1,k-1)+choose(n-1,k)
def outputter():
    x = int(input('Enter n: '))
    y = int(input('Enter k: '))
    print(choose(x,y))
