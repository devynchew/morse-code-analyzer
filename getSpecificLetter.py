from getUserInput import getUserInput

class getSpecificLetter(getUserInput):
    def getInput(self):
        while True:
            try:
                value = input(self.prompt).lower()
            except ValueError:
                print(self.errorMsg)
                continue
            if value != 'h' and value != 'v': # if value is neither 'h' nor 'v'
                print(self.errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value