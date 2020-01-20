def mysplit(stringarg,delimiter):
    y = stringarg
    for x in y:
        if x == delimiter:
            stringarg.replace(x,',')

    return (y)
