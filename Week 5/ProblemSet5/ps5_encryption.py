# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#

def buildCoder(shift):
    alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')
    cipher = {}

    for highLow in range(2):
        for l in range(0, 26):
            plainLetter = alphabet[highLow][l]
            x = shift+l-26
            if l+shift < 26: x = shift+l
            cipherLetter = alphabet[highLow][x]
            cipher[plainLetter] = cipherLetter
    return cipher

def applyCoder(text, coder):    
    cipherText = list(text)
    for index in range(len(text)):
        if text[index] in coder.keys():
            cipherLetter = coder[text[index]]
        else:
            cipherLetter = text[index]
        cipherText[index] = cipherLetter
    cipherText = ''.join(cipherText)
    return cipherText

def applyShift(text, shift):
    cipherText = applyCoder(text, buildCoder(shift))
    return cipherText


#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    mostWordsAtK = [0,0]
    for k in range(26):
        mostWords = 0
        plainText = applyShift(text, k)
        decodedWordList = plainText.split(" ")
        for wordIndex in range(len(decodedWordList)):
            if isWord(wordList, decodedWordList[wordIndex]):
                mostWords += 1
        if mostWords > mostWordsAtK[0]: mostWordsAtK = [mostWords, k]
    return mostWordsAtK[1]

def decryptStory():
    wordList = loadWords()
    cipherText = getStoryString()
    shift = findBestShift(wordList, cipherText)
    plainText = applyShift(cipherText, shift)
    return plainText

#
# Build data structures used for entire session and run encryption
#
'''
if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
'''
#wordList = loadWords()
