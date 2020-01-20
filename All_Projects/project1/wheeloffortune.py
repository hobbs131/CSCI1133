import random


def begingame(): # use begingame function to start the game
    allvowels1= []
    allconsonants=[]
    winnings = 0
    print ("Welcome to the Wheel of Fortune!")
    print()
    print ("The phrase is:")
    Phrasebank = open("phrasebank.txt").read().splitlines()
    x = random.randint(0,100)
    mylist1 =(['_'] * len(Phrasebank[x]))
    replacer = 0
    underlinePhrase = []
    print (Phrasebank[x])

    while replacer < len(Phrasebank[x]): # takes phrase and converts it to _
        if Phrasebank[x][replacer] != " ":
            underlinePhrase.append("_")
            replacer += 1

        else:
            underlinePhrase.append("" "")
            replacer += 1

    print (" ".join(underlinePhrase))
    print()

    if x <= 19:
        print ("The category is: Before and After")
    elif x > 19 and x <= 39:
        print ("The category is: Song Lyrics")
    elif x > 39 and x <= 59:
        print ("The category is: Around the House")
    elif x > 59 and x <= 79:
        print ("The category is: Food and Drink")
    elif x > 79 and x <= 99:
        print ("The category is: Same Name")

    print()
    print("Your current winnings are : $", winnings)
    print()

    spinner = input("Would you like to Spin The Wheel (type 'spin'), Buy a Vowel (type 'vowel'), or Solve the Puzzle (type 'solve')?")
    print()

    if spinner == 'spin':
        spinthewheel(Phrasebank[x],winnings,allconsonants,mylist1,allvowels1)



def spinthewheel(phrase,winnings,allconsonants,mylist1,allvowels1):
    loopexiter = 0
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'] # needs to account for uppers
    spin = ['$50', '$100', '$100', '$100', '$100', '$100', '$100', '$200', '$200', '$200', '$200', '$250', '$250', '$250', '$500', '$500', '$750', '$750', '$1000','$2000', '$5000', '$10000', 'Bankrupt', 'Bankrupt']
    valuespin = ['50','100','100','100','100','100','100','200', '200','200','200', '250', '250', '250', '500', '500','750','750', '1000', '2000', '5000', '10000']

    consonantTotal = 0
    comparer = 0

    while loopexiter == 0: # This loop exits out of spinthewheel function when input at end is not 'spin'

        liner = 0
        value = random.randint(0,23)
        print ("You've spun" , spin[value])


        if spin[value] == 'Bankrupt':
            winnings = 0
            print("You have gone bankrupt. Your turn is over. Please play again")


        else:
            consonant = input("Guess a consonant (use caps):")
            print()
            allconsonants.append(consonant)
            while comparer < len(phrase):
                if phrase[comparer] == consonant:
                    consonantTotal+=1
                    comparer+=1

                else:
                    comparer+=1
            if consonantTotal!= 0: # subtracts or adds to winnings depending on consonantTotal
                winnings = winnings + consonantTotal*int(valuespin[value])
            else:
                winnings = winnings - int(valuespin[value])

            while liner < len(phrase): # takes the phrase and appends the input consonant as it self, appends spaces as " " and appends anything else as underlines

                if phrase[liner] == consonant: # replaces _ in mylist with either the consonant or a space depending on what is in the phrase index.
                    mylist1[liner] = consonant
                    liner+=1
                elif phrase[liner] == ' ':
                    mylist1[liner] = ' '
                    liner+=1
                else:
                    liner+=1


            if consonantTotal != 0:

                print("Congratulations", consonant, "appears in the phrase", consonantTotal, "times!", "you've won $", consonantTotal*int(valuespin[value]))
                print()
            else:
                print (consonant, "is not in the phrase you've lost $",spin[value])

            print("The Phrase is:")
            print(" ".join(mylist1))
            print()
            print("Vowels Guessed: ", allvowels1)
            print("Consonants Guessed", allconsonants)
            print("Your current winnings are: $", winnings)

            spinner = input("Would you like to Spin the Wheel (type 'spin', Buy a Vowel (type 'vowel'), or Solve the Puzzle (type 'solve')?")

            if spinner == 'vowel':

                loopexiter+=1
                buyAVowel(phrase,winnings,allconsonants,mylist1, allvowels1)

            elif spinner == 'solve':
                loopexiter +=1
                solveThePuzzle(phrase,winnings,allconsonants,mylist1,allvowels1)



def buyAVowel(phrase, winnings, allconsonants,mylist1,allvowels1):

    vowelTotal = 0
    comparer1= 0
    loopexiter1 = 0
    while loopexiter1 == 0:
        liner1 = 0
        if winnings >= 250:
            vowel = input("Okay! $250 will be deducted from your winnings. Which vowel would you like to buy (A,E,I,O,U)? (use caps): ")
            allvowels1.append(vowel)
            while comparer1 < len(phrase):

                if phrase[comparer1] == vowel:
                    vowelTotal+=1
                    comparer1+=1
                else:
                    comparer1+=1

        else:
            print ("You do not have enough money to buy a vowel")

        if vowelTotal!= 0: # subtracts 250 from winnings
            print ("Congratulations", vowel, "appears in the phrase", vowelTotal, "times!")
            print()
            winnings-= 250
        else:
            print (vowel, "is not in the phrase")
            winnings-=250

        while liner1 < len(phrase): # takes the phrase and appends the input consonant as it self, appends spaces as " " and appends anything else as underlines

            if phrase[liner1] == vowel: # replaces _ in mylist1 with either the consonant, vowel or a space depending on what is in the phrase index.
                mylist1[liner1] = vowel
                liner1+=1
            elif phrase[liner1] == ' ':
                mylist1[liner1] = ' '
                liner1+=1

            elif phrase[liner1] in allconsonants:
                mylist1[liner1] = phrase[liner1]
                liner1+=1

            else:
                liner1+=1


        print("The Phrase is:")
        print()
        print(" ".join(mylist1))
        print("Vowels Guessed: ", allvowels1)
        print("Consonants Guessed", allconsonants)
        print("Your current winnings are: $", winnings)
        print()

        spinner1 = input("Would you like to Spin The Wheel (type 'spin'), Buy a Vowel (type 'vowel'), or Solve the Puzzle (type 'solve')?")
        if spinner1 == 'solve':
            loopexiter1 += 1
            solveThePuzzle(phrase,winnings,allconsonants,mylist1,allvowels1)
        elif spinner1 == 'spin':
            loopexiter1 +=1
            spinthewheel(phrase,winnings,allconsonants,mylist1,allvowels1)
        else:
            loopexiter1 = 0





def solveThePuzzle(phrase,winnings,allconsonants,mylist1,allvowels1):
    loopexiter2= 0

    while loopexiter2 == 0:
        guess = input("What's your guess (be sure to enter your guess with single spaces!)?: ")
        if guess.upper() == phrase:
            print (" Correct, you have won the game! You are walking away with $",winnings)
            loopexiter2 += 1
        else:

            print("Sorry, that guess was incorrect! Your winnings will start over at $0.")

            winnings = 0

            print("The Phrase is:")
            print(" ".join(mylist1))
            print("Vowels Guessed: ", allvowels1)
            print("Consonants Guessed", allconsonants)
            print("Your current winnings are: $", winnings)

            spinner2 = input("Would you like to Spin The Wheel (type 'spin') or Solve the Puzzle (type 'solve')? (You can't buy a vowel as your winnings are $0)")
            if spinner2 == 'solve':
                loopexiter2 = 0
            elif spinner2 == 'vowel':
                loopexiter2 += 1
                buyAVowel(phrase,winnings,allconsonants,mylist1,allvowels1)
            elif spinner2 == 'spin':
                loopexiter2 += 1
                spinthewheel(phrase,winnings,allconsonants,mylist1,allvowels1)
