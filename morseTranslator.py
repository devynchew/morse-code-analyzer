import os.path
import re

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

def vertical(morseCode):
    letter = []
    finalList = []
    i = 0
    for char in morseCode:
        if char == ',':
            spacesNeeded = 5 - len(letter)
            j = 0
            while j != spacesNeeded:
                letter.insert(0,' ')
                j += 1
            finalList += letter
            letter = []
            i += 1
        elif i == (len(morseCode) - 1):
            letter += char
            spacesNeeded = 5 - len(letter)
            j = 0
            while j != spacesNeeded:
                letter.insert(0,' ')
                j += 1
            finalList += letter
            letter = []
            i += 1
        else:
            letter += char
            i += 1

    print(finalList)
    print(len(finalList))
    list = []
    biggerList = []
    for index, char in enumerate(finalList):
        print(index,char)
        if index % 5 == 0:
            if index != 0 or index == (len(finalList) - 1):
                biggerList.append(list)
                list = []
        else:
            list.append(char)
    print(biggerList)



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


# outputMorse = encodeMorse("eng.txt")
# print(outputMorse)

# outputEnglish = decodeMorse("morse.txt")
# print(outputEnglish)

def getSpecificInt(prompt): # function to get input value between 1 and 4
    errorMsg = "Please enter a number between 1 and 4."
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(errorMsg)
            continue # continue skips the current iteration
        if value < 1:
            print(errorMsg)
            continue
        if value > 4:
            print(errorMsg)
            continue
        else:
            # we got a valid value, exit the loop
            break
    return value

def getSpecificLetter(prompt): # function to get input value of either 'v' or 'h'
    errorMsg = "\nPlease enter either 'h' or 'v'."
    while True:
        try:
            value = input(prompt).lower()
        except ValueError:
            print(errorMsg)
            continue
        if value != 'h' and value != 'v': # if value is neither 'h' nor 'v'
            print(errorMsg)
            continue
        else:
            # we got a valid value, exit the loop
            break
    return value

def getSpecificText(prompt): # function to get upper case text
    errorMsg = "\nPlease enter valid text."
    while True:
        try:
            value = (input(prompt)).upper()
        except ValueError:
            print(errorMsg)
            continue
        if not all(x.isalnum() or x.isspace() for x in value): # only accept alphabets, numbers and spaces
            print(errorMsg)
            continue
        else:
            # we got a valid value, exit the loop
            break
    return value
    
def getInputFile(prompt):
    errorMsg = "\nPlease enter a valid morse txt file."
    while True:
        try:
            value = input(prompt)
        except:
            print(errorMsg)
            continue
        if not os.path.isfile(value): # check if file exist
            print(errorMsg)
            continue
        else:
            # we got a valid value, exit the loop
            break
    return value

def getOutputFile(prompt):
    errorMsg = "\nPlease enter a valid output file name."
    while True:
        try:
            value = input(prompt)
        except:
            print(errorMsg)
            continue
        if not all(x.isalnum() or x.isspace() or x not in('\\','/',':','*','?','"','<','>','|') for x in value): # check if output file name is valid 
            print(errorMsg)
            continue
        else:
            # we got a valid value, exit the loop
            break
    return value + '.txt'


def userInterface():
    userInput4 = False
    printingMode = 'horizontal'
    while not userInput4:
        print(f"*****************************************************************************\n\
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
        choice = getSpecificInt("Enter choice: ")

        if choice == 1: # change printing mode
            userInputPrint = getSpecificLetter(f"Current print mode is {printingMode}\n\n\
Enter 'h' for horizontal or 'v' for vertical, then press enter: ")
            
            if userInputPrint == 'v':
                printingMode = 'vertical'
                print("The print mode has been changed to vertical")
            else:
                printingMode = 'horizontal'
                print("The print mode has been changed to horizontal")

            input("Please Enter, to continue....")
        elif choice == 2: # convert text to morse code
            text = getSpecificText("Please type text you want to convert to morse code: \n")
            outputMorse = encodeMorse(text)
            print(outputMorse)
            # outputMorse = vertical(outputMorse)
            # print(outputMorse)

            input("\nPlease Enter, to continue....")
        elif choice == 3: # Analyze morse code
            inputFile = getInputFile("Please enter input file: ")
            # outputFile = getOutputFile("Please enter output file: ")
            text = open(inputFile, "r").read() # read the morse file
            decodedMorseText = decodeMorse(text)
            print(f"\n>>>Analysis and sorting started: \n\n*** Decoded Morse Text\n{decodedMorseText}")
            
            # Creating an empty dictionary
            freq = {}
            for item in decodedMorseText.split():
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1

            print(f"Freq: {freq}")
            for key, value in freq.items():
                print (f"{key}: {value}")
            uniqueFreq = list(freq.keys()) # create a list of unique words
            print(f"Unique freq: {uniqueFreq}")

            textList = decodedMorseText.split('\n')
            for index, item in enumerate(textList):
                textList[index] = item.split(" ")
    
            print(textList)
            mainPosition = [] # list of tuples in a list
            for uniqueWord in uniqueFreq: # for each unique word, go through the text line by line, record the position of each match and append it to mainPosition
                position = []
                for lineNumber,line in enumerate(textList):
                    for index, word in enumerate(line):
                        if word == uniqueWord:
                            positionTuple = (lineNumber,index)
                            position.append(positionTuple)
                mainPosition.append(position)
            print(mainPosition)

                        

            # for lineNumber,line in enumerate(textList):
            #     occurrences = [m.start() for m in re.finditer('SOS', line)]
            #     print(occurrences)
            #     if occurrences:
            #         for occurrence in occurrences:
            #             print('Found `SOS` at character %d on line %d' % (occurrence, lineNumber + 1))


        elif choice == 4:
            userInput4 = True
        else:
            print("Please enter a valid option.")

userInterface()
