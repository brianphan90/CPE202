 
class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next
        
    def getItem(self):
        return self.item
    
    def getNext(self):
        return self.next
    
    def setItem(self, item):
        self.item = item
        
    def setNext(self,next):
        self.next = next
class Stack:   
    def __init__(self):
        
        self.first = None
        self.last = self.first
        self.numItems = 0
    
    def pop(self): #makes a new node
        if self.numItems == 0:
            raise ValueError("empty stack")
        cur_node = self.first.getItem()
        self.first = self.head.getNext()
        return cur_node
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.first
        self.first = new_node
    def top(self):
        top_node = self.first.getNext()
        return top_node
    def isempty(self):
        if self.first.getNext() == None:
            return True
        else:
            return False
def main():
    stack = Stack()
    stack.push("test")
    stack.top()
    stack.isempty()
    stack.pop()
if __name__ == "__main__":
    main()
