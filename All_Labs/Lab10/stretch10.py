def csv():
    fileobj = open("abbrev.txt", "r")
    a = 0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    l=0
    m=0
    n=0
    o=0
    p=0
    q=0
    r=0
    s=0
    t=0
    u=0
    v=0
    w=0
    x=0
    y=0
    z=0

    counter = []

    for line in fileobj:
        for ch in line:
            if ch == 'a':
                a+=1
            elif ch == 'A':
                a+=1
            elif ch == 'b':
                b+=1
            elif ch == 'B':
                b+=1
            elif ch == 'C':
                c+=1
            elif ch == 'c':
                c+=1
            elif ch == 'D':
                d+=1
            elif ch == 'd':
                d+=1
            elif ch == 'E':
                e+=1
            elif ch == 'e':
                e+=1
            elif ch == 'F':
                f+=1
            elif ch == 'f':
                f+=1
            elif ch == 'G':
                g+=1
            elif ch == 'g':
                g+=1
            elif ch == 'H':
                h+=1
            elif ch == 'h':
                h+=1
            elif ch == 'I':
                i+=1
            elif ch == 'i':
                i+=1
            elif ch == 'J':
                j+=1
            elif ch == 'j':
                j+=1
            elif ch == 'k':
                k+=1
            elif ch == 'K':
                k+=1
            elif ch == 'L':
                l+=1
            elif ch == 'l':
                l+=1
            elif ch == 'M':
                m+=1
            elif ch == 'm':
                m+=1
            elif ch == 'N':
                n+=1
            elif ch == 'n':
                n+=1
            elif ch == 'O':
                o+=1
            elif ch == 'o':
                o+=1
            elif ch == 'P':
                p+=1
            elif ch == 'p':
                p+=1
            elif ch == 'Q':
                q+=1
            elif ch == 'q':
                q+=1
            elif ch == 'R':
                r+=1
            elif ch == 'r':
                r+=1
            elif ch == 'S':
                s+=1
            elif ch == 's':
                s+=1
            elif ch == 'T':
                t+=1
            elif ch == 't':
                t+=1
            elif ch == 'U':
                u+=1
            elif ch == 'u':
                u+=1
            elif ch == 'V':
                v+=1
            elif ch == 'v':
                v+=1
            elif ch == 'W':
                w+=1
            elif ch == 'w':
                w+=1
            elif ch == 'X':
                x+=1
            elif ch == 'x':
                x+=1
            elif ch == 'Y':
                y+=1
            elif ch == 'y':
                y+=1
            elif ch == 'Z':
                z+=1
            elif ch == 'z':
                z+=1

    counter.append(a)
    counter.append(b)
    counter.append(c)
    counter.append(d)
    counter.append(e)
    counter.append(f)
    counter.append(g)
    counter.append(h)
    counter.append(i)
    counter.append(j)
    counter.append(k)
    counter.append(l)
    counter.append(m)
    counter.append(n)
    counter.append(o)
    counter.append(p)
    counter.append(q)
    counter.append(r)
    counter.append(s)
    counter.append(t)
    counter.append(u)
    counter.append(v)
    counter.append(w)
    counter.append(x)
    counter.append(y)
    counter.append(z)
    print(counter)
