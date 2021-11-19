import numpy as np

outputMorse = '...,---,..., ,.--,., ,-.,.,.,-.., ,....,.,.-..,.--.'
outputArr = outputMorse.split(',')
print(outputArr)

# finding the longest string in this list
max_len = -1
for letter in outputArr:
    if len(letter) > max_len:
        max_len = len(letter)
        longestStr = letter
print(longestStr)

tempArr = []
for letter in outputArr:
    emptySpaces = len(longestStr) - len(letter)
    letter = letter[:0] + ' ' * emptySpaces + letter[0:]
    tempArr.append(letter)


newArr = []
for letter in tempArr:
    for char in letter:
        newArr.append(char)
print(newArr)
newNpArr = np.array(newArr).reshape(-1,len(longestStr))
print(newNpArr)
transposedNpArr = np.transpose(newNpArr)
print(transposedNpArr)


for arr in transposedNpArr:
    lineStr = ''
    for char in arr:
        lineStr += char
    print(lineStr)