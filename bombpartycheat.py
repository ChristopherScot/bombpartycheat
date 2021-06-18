from random import randint
import pyperclip
import sys
path = 'C:\\Users\Martin\Documents\\bombpartycheat\\top10000'
wordlistone = open(path)
stringone = wordlistone.read()
def complexity(word):
    points = 0
    letters = ['w','k','j','q','b','g']
    for letter in letters:
        if letter in word:
            points = points + 1
    if len(word) >5: points = points + 1
    if len(word) >8: points = points + 1
    if len(word) >12: points = points + 1
    # print (f"word: {word} points: {points}")
    return points

while True:
    arrayOfWords = []
    letters = input("Please enter part of a word: ")
    for word in stringone.splitlines():
        if letters in word:
            arrayOfWords.append(word)
    matchingWord = max(arrayOfWords, key=complexity)
    # matchingWord = arrayOfWords[randint(0,len(arrayOfWords))]
    pyperclip.copy(matchingWord)
    print (matchingWord)
