import os

def printLogo ():
    os.system('cls')
    print ("\n")

def getWord ():
    word = raw_input("Enter word: ")
    if word.isalpha ():
        return word
    print ("Not a word!")
    quit ()

def printWord (word, letters):
    for letter in word:
        print ((letter if letter not in letters else "_") + " "),
    print ('\n')

def play (word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lifes = 10
    while lifes:
        os.system('cls')
        print (str(lifes) + " life(s) left\n")
        printWord (word, letters)
        letter = raw_input ("Letter: ").upper ()
        if letter not in word:
            lifes -= 1
        else:
            letters = letters.replace(letter, "")
    
    printLogo ()
        

if __name__ == '__main__':
    printLogo ()
    word = getWord (). upper ()
    play (word)


# win?
