def rankandsuit(cards):
    suit = {}
    rank = {}
    x = 0
    count1 = 1
    count2 = 1
    z = 0
    p = 0

    while x < len(cards):
        if cards[x][0] in rank:
            rank[cards[x][0]] = count1+z
            z+=1
        else:
            rank[cards[x][0]] = count1

        if cards[x][1] in suit:
            suit[cards[x][1]]= count2 + p
            p+=1

        else:
            suit[cards[x][1]] = count2
        x+=1

    return rank,suit



def pokerhand(cards):
    looper = 0
    newlist = rankandsuit(cards)
    while looper < len(newlist):
        if '3' in newlist[looper] or newlist[looper+1]:
            print("two pair or three of a kind")
