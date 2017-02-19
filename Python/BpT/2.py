import os

def printLogo ():
    os.system ('cls')
    print ("\n")

def getWord ():
    word = raw_input ("Enter word: ")
    if word.isalpha ():
        return word
    print ("Not a word!")
    quit ()

def printWord (word, letters):
    for letter in word:
        print ((letter if letter not in letters else "_") + " "),
    print ('\n')

def ifWon (word, letters):
    for l in letters:
        for w in word:
            if w == l:
                return
    os.system ('cls')
    printWord (word, letters)
    print ("You won!!")
    quit ()

def play ():
    printLogo ()
    word = getWord ().upper ()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lifes = 10
    while lifes:
        os.system ('cls')
        print (str (lifes) + " life(s) left\n")
        printWord (word, letters)
        letter = raw_input ("Letter: ").upper ()
        if letter not in word:
            lifes -= 1
        else:
            letters = letters.replace (letter, "")
        ifWon (word, letters)
    printLogo ()
    print ("You lost. :'(")
    print ("The word was " + word )
    
if __name__ == '__main__':
    play ()

