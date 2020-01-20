def wordlist(prose):
    a = prose.replace(',', '')
    b = a.replace(';', '')
    c = b.replace('.', '')
    x = 0
    y = 1
    splitphrase = c.split(" ")

    while x < len(splitphrase)-2:
        while y < len(splitphrase)-1:
            if splitphrase[x] == splitphrase[y]:
                splitphrase.replace(splitphrase[y], '')
                y+=1
            else:
                y+=1
            x+=1
            y = x + 1
    print(splitphrase)


def charNumber(char):

    mylist2 = ['A','B','C']
    mylist3 = ['D','E','F']
    mylist4 = ['G','H','I']
    mylist5 = ['J','K','L']
    mylist6 = ['M','N','O']
    mylist7 = ['P','Q','R','S']
    mylist8 = ['T','U','V']
    mylist9 = ['W','X','Y','Z']

    if char in mylist2:
        return 2
    elif char in mylist3:
        return 3
    elif char in mylist4:
        return 4
    elif char in mylist5:
        return 5
    elif char in mylist6:
        return 6
    elif char in mylist8:
        return 8
    elif char in mylist9:
        return 9
    else:
        return


def teltranslate():
    mylist = []
    numbers = ['0','1','2','3','4','5','6','7','8','9', '-']
    phrase = input("Enter a telephone number: ")
    for x in phrase:
        if x not in numbers:
            phrase.replace(x,charNumber(x))

    print(phrase)
