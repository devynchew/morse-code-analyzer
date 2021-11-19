from getUserInput import getUserInput

class getOutputFile(getUserInput):
    def getInput(self):
        while True:
            try:
                value = input(self.prompt)
            except:
                print(self.errorMsg)
                continue
            if not all(x.isalnum() or x.isspace() or x not in('\\','/',':','*','?','"','<','>','|') for x in value): # check if output file name is valid 
                print(self.errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value + '.txt'