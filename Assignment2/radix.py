class Queue: 
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, items):
        self.items.append(items) #add item to the beginning
    
    def dequeue(self):
        return self.items.pop() # remove last item
    
    def peek(self):
        return self.items[len(self.items)-1] #First in line
    
    def size(self):
        return len(self.items)
    def __iter__(self):
        return self
    def next(self):
        if self.lista: #since empty lists are Falsey
            return self.lista.pop(0)
        raise StopIteration    
def get_max_length(lst):            #get the max length
    if lst != []:
        max_len = 0
        for word in lst:
            if len(word) > max_len:
                max_len = len(word)
        return max_len
    else:
        print("This is a blank list!")
def pad_words(lst, max_l, eq_lst = []):                 #pad words with ""
    for word in lst:
        if len(word) < max_l:
            spaces = [ " " * (max_l - len(word))]       #finds how many "" are needed
            eq_lst.append(word + "".join(spaces))
        else:
            eq_lst.append(word)
    return eq_lst
def charAt(s,i):        #returns the character at i if not returns a blank and s is the string
    if len(s) - 1 < i:
        return ""
    return s[i]


   
def radixsort(unsort_lst,random = None):
    max_len = get_max_length(unsort_lst)
    eq_lst = pad_words(unsort_lst, max_len)
    mainQueue = Queue()
    #list_queues = [Queue()] * 127
    list_queues = []
    for bins in range(0,128):
            list_queues.append(Queue())    
    for i in eq_lst:
        mainQueue.enqueue(i)                    #add all the strings to the main queue
    #print(mainQueue.items)   
    #final_lst = get_buckets(unsort_lst)         #gets the characters we will be needing
    index = max_len - 1
    while index >= 0: 
        while mainQueue.isEmpty() == False:
            word = mainQueue.dequeue()
            letter = word[index]
            place = ord(letter)
            list_queues[place].enqueue(word)
        for bins in list_queues:
            while bins.size() != 0:
                n_val = bins.dequeue()
                mainQueue.enqueue(n_val)
        index -= 1
    fin_q = Queue()
    for item in mainQueue.items:
        fin_i = item.replace(" ","")
        fin_q.enqueue(fin_i)
    return fin_q.items   
un = '10', '9', '8', '7', '6', '5'
print(radixsort(un))
    

    

        
