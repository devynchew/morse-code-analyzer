import numpy as np

outputMorse = '...,---,..., ,.--,., ,-.,.,.,-.., ,....,.,.-..,.--.'
outputArr = outputMorse.split(',')

tempArr = []
for letter in outputArr:
    emptySpaces = 5 - len(letter)
    letter = letter[:0] + ' ' * emptySpaces + letter[0:]
    tempArr.append(letter)


newArr = []
for letter in tempArr:
    for char in letter:
        newArr.append(char)

newNpArr = np.array(newArr).reshape(-1,5)
print(newNpArr)
transposedNpArr = np.transpose(newNpArr)
print(transposedNpArr)
# for arr in newNpArr:
#     for char in arr:
