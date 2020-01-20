def counter():
    file = input("Enter the filename: ")
    fileobj = open(file, "r")
    defcount = 0
    forcount = 0
    ifcount = 0
    incount = 0
    returncount = 0

    for newline in fileobj:
        line=newline.split(" ")
        defcount+=line.count("def")
        forcount+=line.count("for")
        ifcount+=line.count("if")
        incount+=line.count("in")
        returncount+=line.count("return")

    keywords = {"def": defcount, "for":forcount, "if": ifcount, "in": incount,  "return": returncount}


    return keywords

def zipf():
    new={}
    file= input("input filename:")
    fileobj= open(file,"r")
    for line in fileobj:
        newline = line.split(" ")
        for x in newline:
            new[x] = 
