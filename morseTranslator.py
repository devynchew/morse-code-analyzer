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

def encodeMorse(file):
    f = open(file, "r")
    text = f.read()
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


def decodeMorse(file):
    f = open(file, "r")
    text = f.read()
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
        choice = input("Enter choice: ")
        if choice.isnumeric(): # if user input is a number, convert to integer
            choice = int(choice)

        if choice == 1:
            userInputPrint = input(f"Current print mode is {printingMode}\n\n\
Enter 'h' for horizontal or 'v' for vertical, then press enter: ")
            if userInputPrint.isalpha(): # user input an alphabet
                userInputPrint = userInputPrint.lower()
                if userInputPrint == 'v':
                    printingMode = 'vertical'
                    print("The print mode has been changed to vertical")
                elif userInputPrint == 'h':
                    printingMode = 'horizontal'
                    print("The print mode has been changed to horizontal")
                else:
                    print("Please enter a valid input.")
            else:
                print("Please enter a valid input.")
            input("Please Enter, to con1tinue....")
        elif choice == 2:
            break
        elif choice == 3:
            break
        elif choice == 4:
            userInput4 = True
        else:
            print("Please enter a valid option.")

userInterface()
