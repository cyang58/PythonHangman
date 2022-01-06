# pythonHangman
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
