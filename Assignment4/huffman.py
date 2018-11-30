#huffman coding
class LinkedList:
    #copied from book
    # The __Node class is used internally by the LinkedList class. It is
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name).
    class __Node:
        def __init__(self, item, next = None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        

        def setItem(self, item):
            self.item = item

        def setNext(self, next):
            self.next = next

        

    def __init__(self, contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item.
        # Its purpose is to eliminate special cases in the code below.
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")

    def insert(self, index, item):          
        cursor = self.first

        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()

            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self)) + " + " + str(type(other)))

        result = LinkedList()

        cursor = self.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        cursor = other.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        return result

    def __contains__(self, item):
        # This is left as an exercise for the reader.
        index = self.first
        while index != None:
            if index.item == item:
                return True
            index = index.next
        return False

    def __delitem__(self, index):
        # This is left as an exercise for the reader.
        current = -1
        x = self.first
        while current < index:
            prev = x
            x = x.next
            current += 1
            if current == index:
                prev.next = x.next
        self.numItems -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False

        cursor1 = self.first.getNext()
        cursor2 = other.first.getNext()
        while cursor1 != None:
            if cursor1.getItem() != cursor2.getItem():
                return False
            cursor1 = cursor1.getNext()
            cursor2 = cursor2.getNext()

        return True

    def __iter__(self):
        # This is left as an exercise for the reader.
        current = self.first.next
        while current is not None:
            yield current.item
            current = current.next

    def __len__(self):
        # This is left as an exercise for the reader.
        return self.numItems
    
    def discard(self):
        if self.numItems != 0:
            cur_node = self.first.next
            self.first.setNext(cur_node.next)
            self.numItems -= 1
        else:
            return None
        return cur_node.item 
    
    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1        
               
    

    
            

    def __str__(self):
        # This is left as an exercise for the reader.
        return str(list(self))

    def __repr__(self):
        # This is left as an exercise for the reader.
        return str(list(self))
    
class PriorityQueue:
    def __init__(self):
        self.items = LinkedList()
        self.frontIdx = 0
        self.codeLookUp = {}
        
    def __compress(self):
        newitems = LinkedList()
        for i in range(self.frontIdx, len(self.items)):
            newitems.append(self.items[i])

        self.items = newitems
        self.frontIdx = 0
    
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")

        
        item = self.items[self.frontIdx]
        del self.items[0]
        return item[0]               
        
    def enqueue(self, item, priority):      #after every enqueue we have to sort the items first due to the ascii value then
        def same_freq(i):                  #then by their priority, but in descending order to dequeue the "least" prioritized
            try:                            #
                return i[0].ord             #node(ch, freq)
            except:                         #node[0] = ch
                return 0                    #node[1] = freq
        
        def return_priority(i):
            return i[1]
    
        
    
        self.items.insert(0, (item, priority))          #insert at 
        self.items = sorted(self.items, key=same_freq)
        self.items = sorted(self.items, key=return_priority, reverse=True)         

    def front(self):
        if self.isEmpty():
            raise RuntimeError

        return self.items[self.frontIdx][0]

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def clear(self):
        self.items = []
        self.frontIdx = 0
        
class Node:
    def __init__(self, freq, char, left = None, right = None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        if self.char != None:           
            self.ord = ord(self.char)
        else:
            self.ord = 1/1000000           #chose smallest value for ord of spaces or None type objects
            
def huffman(phrase):            #want to return the root of the tree
    pq = PriorityQueue()        #high occurance = higher priority  
    frequencies = {}
    unique = []
    unique_frequences = []
    for char in phrase[::]:
        if char not in unique:
            unique.append(char)         #get list of unique characters 
    for ch in unique:
        count = phrase.count(ch)
        node = Node(count, ch)
        pq.enqueue(node, 1/count)           #node(item,priority)    
    while len(pq.items) > 1:            #one character means it is the root
        print(pq.items)
        left_child = pq.dequeue()
        right_child = pq.dequeue()
        print(pq.items)
        parent_freq = left_child.freq + right_child.freq
        parent_node = Node( parent_freq,None, left_child, right_child)
        pq.enqueue(parent_node, 1/parent_freq)
    
    return parent_node
def get_huffman_code(char, root):       #reading the tree to get the codes remember use an array and 2n
    if root.char == char:
        return ''
    else:
        if root.left:           #if left 
            huff_code = get_huffman_code(char, root.left)       #traversing left mean 0 to string
            if huff_code is not None:
                huff_code = '0' + huff_code
                return huff_code
        if root.right:
            huff_code = get_huffman_code(char, root.right)      #traversing right mean
            if huff_code is not None:
                huff_code = '1' + huff_code
                return huff_code
     
codes = {}
sent = 'asdf;k;lkjasdfk dasiirFFDg'
root = huffman(sent)
for ch in sent:
    codes[ch] = get_huffman_code(ch, root)
print(codes["d"])
