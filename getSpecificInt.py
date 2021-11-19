from getUserInput import getUserInput

class getSpecificInt(getUserInput): # getSpecificInt is a getUserInput
    def getInput(self):
        while True:
            try:
                value = int(input(self.prompt))
            except ValueError:
                print(self.errorMsg)
                continue # continue skips the current iteration
            if value < 1:
                print(self.errorMsg)
                continue
            if value > 4:
                print(self.errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value