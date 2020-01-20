
def vowelfinder(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    counter = 0
    while counter < len(word)- 1:
        if word[counter] in vowels:
            return counter
        else:
            counter+=1

def igpay(phrase):
    words = phrase.split(" ")
    x = 0
    while x < len(words)-1:
        if vowelfinder(words[x]) > 0:
            words[x] = words[x] + words[x][0:vowelfinder(words[x])]  + "ay"
            words.replace(words[x][0:vowelfinder(words[x]), ""]


        elif vowelfinder(words[x]) == 0:
            words[x] = words[x] + "way"

    print(words)
