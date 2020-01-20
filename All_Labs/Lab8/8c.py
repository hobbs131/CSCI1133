def letterfrequency(string1):
    string=string1.lower()
    a= string.count('a')
    b= string.count('b')
    c=string.count('c')
    d=string.count('d')
    e=string.count('e')
    f=string.count('f')
    g=string.count('g')
    h=string.count('h')
    i=string.count('i')
    j=string.count('j')
    k=string.count('k')
    l=string.count('l')
    m=string.count('m')
    n=string.count('n')
    o=string.count('o')
    p=string.count('p')
    q=string.count('q')
    r=string.count('r')
    s=string.count('s')
    t=string.count('t')
    u=string.count('u')
    v=string.count('v')
    w=string.count('w')
    x=string.count('x')
    y=string.count('y')
    z=string.count('z')
    dictionary1 = {'a': a, 'b':b,'c':c, 'd':d, 'e': e, 'f': f, 'g': g,  'h': h,'i': i, 'j': j, 'k': k, 'l': l, 'm': m, 'n': n, 'o': o, 'p': p, 'q': q, 'r': r, 's': s, 't': t, 'u': u,'v': v, 'w': w, 'x': x,'y':y, 'z':z}
    return dictionary1
def main():
    x = input("enter a string:")
    y = letterfrequency(x)
    new = {}
    print(y)

    for lol,cash in y.items():
        new[cash]=lol
    print(new)
