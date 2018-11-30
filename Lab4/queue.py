
    
   
class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next
        self.previous = None
    def getItem(self):
        return self.item
    
    def getNext(self):
        return self.next
    
    def setItem(self, item):
        self.item = item
        
    def setNext(self,next):
        self.next = next
class Queue:
        def __init__(self):
            self.first = None
            self.last = None
            self.numItems = 0
        def enqueue(self, item):
            new_node = Node(item)
            if self.last != None:
                self.last.getNext = new_node
            else:
                self.first = new_node
            self.last = new_node
            self.numItems +=1
                
        
        def dequeue(self):
            cur_node = self.first
            if cur_node != None:
                self.first = cur_node.getNext()
            else:
                print("empty queue")
        
        def front(self):
            return self.front.item
        def isEmpty(self):
            if self.first == None and self.last == None:
                return True
            else:
                return False
            
def main():
    q = queue()
    q.enqueue("User01")
    q.enqueue("User02")  
    q.front()
    q.isEmpty()
if __name__ == "__main__":
    main()
    
       
 