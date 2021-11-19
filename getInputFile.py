from getUserInput import getUserInput
import os.path

class getInputFile(getUserInput):
    def getInput(self):
        while True:
            try:
                value = input(self.prompt)
            except:
                print(self.errorMsg)
                continue
            if not os.path.isfile(value): # check if file exist
                print(self.errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value