from Node import Node

class Word(Node):
    def __init__(self,word,freq,x,y):
        self.word = word
        self.freq = freq
        self.x = x
        self.y = y
        super().__init__()

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.freq == otherNode.freq

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'Word' and 'NoneType'")
        if self.freq > otherNode.freq: # highest freq goes first
            return True
        elif self.freq == otherNode.freq: # same freq
            if self.x < otherNode.x: # lower line number goes first
                return True
            elif self.x > otherNode.x:
                return False
            else:
                return self.y < otherNode.y 

    def __str__(self):
        s= f'{self.word}'
        return s