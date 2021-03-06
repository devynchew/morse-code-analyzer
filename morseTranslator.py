import numpy as np
from SortedList import SortedList
from Word import Word
from getInputFile import getInputFile
from getOutputFile import getOutputFile
from getSpecificInt import getSpecificInt
from getSpecificLetter import getSpecificLetter
from getSpecificText import getSpecificText

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

# function to print morse code vertically
def vertical(morseCode):
    outputArr = morseCode.split(',') # split the morseCode string into a list where each item represents one letter/space

    # finding the max length of letter in the morse code to determine how many empty spaces to add in front of each letter
    max_len = -1
    for letter in outputArr:
        if len(letter) > max_len:
            max_len = len(letter)
            longestStr = letter

    # adding empty spaces in front of each letter until its length equals to max length of letter
    tempArr = []
    for letter in outputArr:
        emptySpaces = len(longestStr) - len(letter)
        letter = letter[:0] + ' ' * emptySpaces + letter[0:]
        tempArr.append(letter)

    # breaking down the list further until each morse character is an individual item in a list
    newArr = []
    for letter in tempArr:
        for char in letter:
            newArr.append(char)

    # converting the list into a numpy array, reshaping it and then transposing to get a shape identical to the one shown for vertical printing
    newNpArr = np.array(newArr).reshape(-1,len(longestStr))
    transposedNpArr = np.transpose(newNpArr)

    # printing morse code vertically
    for arr in transposedNpArr:
        lineStr = ''
        for char in arr:
            lineStr += char
        print(lineStr)

# function to convert text to morse code
def encodeMorse(text):
    str = ''
    i = 0
    for letter in text:
        if letter != ' ':
            if letter.isalnum():
                if i == len(text) - 1:
                    str += MORSE_CODE_DICT[letter]
                else:
                    str += MORSE_CODE_DICT[letter] + ','
            else:
                str += letter
        else:
            str += ' ,'
        i += 1
    return str

# function to convert morse code to text
def decodeMorse(text):
    morsetext = ''
    translated = ''
    i = 0

    for char in text:
        if char != ',':
            if char != ' ':
                if char != '\n':
                    morsetext += char
                else: # char is a new line
                    translated += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morsetext)] + '\n'
                    morsetext = ''
            else: # char is a space
                translated += ' '
        else: # char is a comma
            if morsetext != '':
                translated += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morsetext)]
                morsetext = ''
        i += 1
    translated += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morsetext)]
    return translated

def getStopWords(file):
    stopwordsFile = open(file, "r")
    stopwordsList = []
    for line in stopwordsFile:
        stripped_line = line.strip()
        stopwordsList.append(stripped_line.upper())
    return stopwordsList

def writeToFile(file,content):
    # Open the file in append & read mode ('a+')
    with open(file, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(content)

def userInterface():
    userInput4 = False
    printingMode = 'horizontal'
    while not userInput4:
        print(f"    *****************************************************************************\n\
    * ST1507 DSAA: MorseCode Message Analyzer                                   *\n\
    *___________________________________________________________________________*\n\
    *                                                                           *\n\
    *    - Done by: Devyn Chew (2026578)                                        *\n\
    *    - Class DAAA/2B/04                                                     *\n\
    *****************************************************************************\n\
    \n\n\n\
    Please select your choice ('1','2','3','4'):\n\
        1. Change Printing Mode\n\
        2. Convert Text to Morse Code\n\
        3. Analyze Morse Code Message\n\
        4. Exit\n")
        # get user choice
        intClass = getSpecificInt("Enter choice: ", "Please enter a number between 1 and 4.")
        choice = intClass.getInput()

        if choice == 1: # change printing mode
            letterClass =  getSpecificLetter(f"Current print mode is {printingMode}\n\n\
Enter 'h' for horizontal or 'v' for vertical, then press enter: ", "\nPlease enter either 'h' or 'v'.")
            userInputPrint = letterClass.getInput()
            
            if userInputPrint == 'v':
                printingMode = 'vertical'
                print(f"The print mode has been changed to {printingMode}")
            else:
                printingMode = 'horizontal'
                print(f"The print mode has been changed to {printingMode}")

            input("Please Enter, to continue....")
        elif choice == 2: # convert text to morse code
            textClass = getSpecificText("Please type text you want to convert to morse code: \n", "\nPlease enter valid text.")
            text = textClass.getInput()

            outputMorse = encodeMorse(text) # encode text to morse code
            if printingMode == 'horizontal':
                print(outputMorse) # morse code prints horizontally by default
            else:
                vertical(outputMorse)

            input("\nPlease Enter, to continue....")
        elif choice == 3: # Analyze morse code and generate report
            inputFileClass = getInputFile("Please enter input file: ", "\nPlease enter a valid morse txt file.") # get input file
            inputFile = inputFileClass.getInput()

            outputFileClass = getOutputFile("Please enter output file: ", "\nPlease enter a valid output file name.") # get output file
            outputFile = outputFileClass.getInput()

            text = open(inputFile, "r").read() # read the morse file
            decodedMorseText = decodeMorse(text) # convert morse code to text

            writeToFile(outputFile,f"*** Decoded Morse Text\n{decodedMorseText}")

            print(f"\n>>>Analysis and sorting started: \n\n*** Decoded Morse Text\n{decodedMorseText}")
            # Start making the report
            # Create a dictionary of unique words as keys and frequency as value
            freq = {}
            for item in decodedMorseText.split():
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1

            sortedFreq = sorted(freq.items(), key=lambda x: (-x[1], len(x[0]), x[0])) # create a list of tuples of (Word:Freq)
            
            sortedFreqWords = [] # create a list of unique words
            for item in sortedFreq:
                sortedFreqWords.append(item[0])

            # create a list where each item represents a new line of decoded morse text
            textList = decodedMorseText.split('\n')
            for index, item in enumerate(textList):
                textList[index] = item.split(" ")

            # list of tuples in a list where each list represents the positions of each unique word in decoded morse text
            mainPosition = [] 
            for uniqueWord in sortedFreqWords: # for each unique word, go through the text line by line, record the position of each match and append it to mainPosition
                position = []
                for lineNumber,line in enumerate(textList):
                    for index, word in enumerate(line):
                        if word == uniqueWord:
                            positionTuple = (lineNumber,index)
                            position.append(positionTuple)
                mainPosition.append(position)

            # printing out the middle bulk of the report
            arrLength = 0 # counter that handles when a new frequency gets printed
            for index, item in enumerate(mainPosition):
                if len(item) != arrLength:
                    print(f"\n*** Morse Words with frequency=> {len(item)}")
                    writeToFile(outputFile, f"\n*** Morse Words with frequency=> {len(item)}")
                print(encodeMorse(sortedFreqWords[index]))
                writeToFile(outputFile, f"{encodeMorse(sortedFreqWords[index])}")
                print(f"[{sortedFreqWords[index]}] ({len(item)}) {item}")
                writeToFile(outputFile, f"[{sortedFreqWords[index]}] ({len(item)}) {item}")

                arrLength = len(item)

            # prepare a list of essential words for sorting
            essMessageListSorted = []
            for index, item in enumerate(mainPosition):
                newList = []
                newList.extend((sortedFreqWords[index], len(item), item[0]))
                essMessageListSorted.append(newList)
            print(essMessageListSorted)

            # get a list of stopwords
            stopwordsList = getStopWords('stopwords.txt')
            # remove all stopwords from essential word list
            essMessageList = [x for x in essMessageListSorted if x[0] not in stopwordsList]

            # sort essential message with our sorted list class
            l = SortedList() # class to sort essential message
            
            # inserting the word, frequency and position of the word for sorting
            for word in essMessageList:
                l.insert(Word(word[0], word[1], word[2][0], word[2][1]))

            print(f'\nEssential Message\n{l}')
            writeToFile(outputFile, f"\nEssential Message\n{l}")

        elif choice == 4: # Exit the program
            userInput4 = True
        else: 
            print("Please enter a valid option.")

userInterface() # run the main program
