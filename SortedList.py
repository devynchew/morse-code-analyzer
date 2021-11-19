
class SortedList:
    def __init__(self):
        self.headNode = None # Worder to the first Node
        self.currentNode = None
        self.length = 0
        
    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode # self.headNode now stores the address of newNode instead of oldHeadNode
        self.headNode.nextNode = oldHeadNode # newNode.nextNode now stores the address of oldHeadNode instead of None

    def insert(self, newNode):
        self.length += 1

        # If list is currently empty (boundary case ie dont happen very often)
        if self.headNode == None:
            self.headNode = newNode
            return # terminate function, anything below will not execute
            
        # Check if it is going to be new head (boundary case)
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        # Check it is going to be inserted between any pair of Nodes (left,right)
        leftNode = self.headNode # temporary variable leftNode Words to first guy
        rightNode = self.headNode.nextNode # temporary variable leftNode Words to second guy

        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        
        # Once we reach here it must be added at the tail
        # because newNode is larger than all other Nodes
        leftNode.nextNode = newNode

    def __str__(self):
        # We start at the head
        output =""
        node= self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = node.__str__()
                firstNode = False
            else:
                output += (' ' + node.__str__())
            node= node.nextNode
        return output
