freq = {'SOS': 2, 'OUR': 1, 'SHIP': 1, 'IS': 1, 'SINKING': 1, 'PLEASE': 1, 'HELP': 1}

sortedValues = sorted(freq.values(), reverse=True) # sort values from high to low
print(sortedValues)
sortedDict = {}

for i in sortedValues:
    for word in freq.keys():
        if freq[word] == i: # if freq of word equal to freq in sortedValues
            sortedDict[word] = freq[word]

print(sortedDict)

sortedLength = freq.keys()
print(sortedLength)