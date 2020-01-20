def power(a,n):

    if n == 0:
        return 1

    else:
        return a*power(a,n-1)

def series(n):  ## doesnt account for 1.

    if n <= 1:
        return 0
    else:
        return n**(n-1)/(n-1)+ series(n-1)

def numdigits(n):

    if n < 10 and n >= 0 or n > -10 and n <= 0:
        return 1
    else:
        return 1 + numdigits(n/10)
