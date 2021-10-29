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
        if not all(x.isalpha() or x.isspace() for x in value):
            print(errorMsg)
            continue
        else:
            # we got a valid value, exit the loop
            break
    return value
    


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
        2. Convert Morse Code To Text\n\
        3. Analyze Morse Code Message\n\
        4. Exit\n")
        choice = getSpecificInt("Enter choice: ")

        if choice == 1:
            userInputPrint = getSpecificLetter(f"Current print mode is {printingMode}\n\n\
Enter 'h' for horizontal or 'v' for vertical, then press enter: ")
            
            if userInputPrint == 'v':
                printingMode = 'vertical'
                print("The print mode has been changed to vertical")
            else:
                printingMode = 'horizontal'
                print("The print mode has been changed to horizontal")

            input("Please Enter, to continue....")
        elif choice == 2:
            text = getSpecificText("Please type text you want to convert to morse code: \n")
            outputMorse = encodeMorse(text)
            print(outputMorse)

            input("\nPlease Enter, to continue....")
        elif choice == 3:
            break
        elif choice == 4:
            userInput4 = True
        else:
            print("Please enter a valid option.")

userInterface()
