def roundit(x):
    xi = int(x)

    if x > 0:
        if abs(x-xi) > .5:
            print (xi+1)

        if abs(x-xi) < .5:
            print (xi)

        if abs(x-xi) == .5:
            print (xi+1)

    if x < 0:

        if abs(x-xi) > .5:
            print (xi-1)

        if abs(x-xi) < .5:
            print (xi)

        if abs(x-xi) == .5:
            print (xi-1)
