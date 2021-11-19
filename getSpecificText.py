from getUserInput import getUserInput

class getSpecificText(getUserInput):
    def getInput(self):
        while True:
            try:
                value = (input(self.prompt)).upper()
            except ValueError:
                print(self.errorMsg)
                continue
            if not all(x.isalnum() or x.isspace() for x in value): # only accept alphabets, numbers and spaces
                print(self.errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value