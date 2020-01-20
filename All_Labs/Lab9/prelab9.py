def makeDictionary(names,scores):
    namesandscores = {}
    x = 0
    while x < len(names):
        namesandscores[names[x]] = scores[x]
        x+=1
    scoreDict = namesandscores
    print(scoreDict)

def getScore(name,dictionary):
    if name in dictionary:
        print (dictionary[name])

    else:
        print ("sorry name is not in dictionary")
        return -1
