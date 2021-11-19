class getUserInput: # parent class
    def __init__(self, prompt, errorMsg): 
        self.prompt = prompt
        self.errorMsg = errorMsg

    def getInput(self): # abstract function
        raise NotImplementedError("Subclass must implement abstract method")