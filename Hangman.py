"""
Chengjie (Dylan) Yang
B00809764
Introduction to Python Programming course
Winter 2021-2022

Hangman Game

Documentation:

loadWordTxtFile:
    Returns a list of words using inFile
    wordlist is a list of strings

words.txt
    These are a list of randomly generated words that I used https://randomwordgenerator.com/c to generate
    The default pack included 50 words that are all less than 8 characters.

chooseWord:
    Returns a word from wordlist at random. 
    random is imported

isWordGuessed:
    userGuess: a string, the word the player is guessing
    guessedSoFar: a list, all the letters that have been guessed so far
    returns: true or false, True if all the letters of userGuess are in guessedSoFar

getGuessedWord:
    userGuess: a string, the word the player is guessing
    guessedSoFar: a list, all the letters that have been guessed so far
    returns: a string, that will be what is guessed before and what is not guessed with underscores _

getLettersLeft
    guessedSoFar:  a list, all the letters that have been guessed so far
    returns: a string, that will be all the letters that haven't been guessed yet.

main:
    param:
        userGuess: this will the word user will be guessing.
At the start we will let the player know how long the word and the avaiable letters.

"""
import random

wordfileName = "words.txt"

def loadWordTxtFile():
    print("Loading all words from the file")

    inFile = open(wordfileName, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("Words Succesfully loaded")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)
wordlist = loadWordTxtFile()

def isWordGuessed(userGuess, guessedSoFar):
    c=0
    for i in guessedSoFar:
        if i in userGuess:
            c+=1
    if c==len(userGuess):
        return True
    else:
        return False


def getGuessedWord(userGuess, guessedSoFar):
    s=[]
    for i in userGuess:
        if i in guessedSoFar:
            s.append(i)
    ans=''
    for i in userGuess:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getLettersLeft(guessedSoFar):

    import string
    ans=list(string.ascii_lowercase)
    for i in guessedSoFar:
        ans.remove(i)
    return ''.join(ans)

def main(userGuess):
    print("Lets play Hangman!")
    print("My word is ",len(userGuess),"letters long.")
    
    global guessedSoFar
    mistakeCounts=0
    guessedSoFar=[]
    
    while 8 - mistakeCounts > 0:
        
        if isWordGuessed(userGuess, guessedSoFar):
            print("-=+=-")
            print("You won!")
            break
            
        else:
            print("-=+=-")
            print("You have",8-mistakeCounts,"guesses left.")
            print("Your avaiable letters are:",getLettersLeft(guessedSoFar))
            guess=str(input("Your turn to guess a letter!")).lower()
            
            if guess in guessedSoFar:
                print("Letter already guessed!",getGuessedWord(userGuess,guessedSoFar))
                
            elif guess in userGuess and guess not in guessedSoFar:
                guessedSoFar.append(guess)
                print("You guessed right!",getGuessedWord(userGuess,guessedSoFar))
                
            else:
                guessedSoFar.append(guess)
                mistakeCounts += 1
                print("I dont have that letter in my word!",getGuessedWord(userGuess,guessedSoFar))
                
        if 8 - mistakeCounts == 0:
            print("-=+=-")
            print("You dont have any more guesses!!")
            break
        
        else:
            continue


userGuess = chooseWord(wordlist).lower()
main(userGuess)