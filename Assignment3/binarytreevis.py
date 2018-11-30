from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime
import time
import sys


screenMin = 0
screenMax = 300

class LinkedList:
    class __Node:
        def __init__(self, item, next=None):
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
    
class Queue:
    def __init__(self):
        self.items = LinkedList()
        self.frontIdx = 0

    def __compress(self):
        newitems = LinkedList()
        for i in range(self.frontIdx, len(self.items)):
            newitems.append(self.items[i])

        self.items = newitems
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError

        
        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError

        return self.items[self.frontIdx]

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def clear(self):
        self.items = []
        self.frontIdx = 0


#copied from book
class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class. 
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
        def getVal(self):
            return self.val
        
        def setVal(self, newval):
            self.val = newval
            
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setLeft(self, newleft):
            self.left = newleft
            
        def setRight(self, newright):
            self.right = newright
            
        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

        def inorder(self):          #result is a inorder traversal list
            fin = []
            if self.left:
                fin = fin + self.left.inorder()
            fin.append(self.getVal())
            if self.right is not None:
                fin = fin + self.right.inorder()
            return fin

        def preorder(self):        #result is a preorder traversal list
            fin = []
            fin.append(self.getVal())
            if self.left:
                fin = fin + self.left.preorder()
            if self.right:
                fin = fin + self.right.preorder()
            return fin

        def postorder(self):        #result is a postorder traversal list
            fin = []
            if self.left:
                fin = fin + self.left.postorder()
            if self.right is not None:
                fin = fin + self.right.postorder()
            fin.append(self.getVal())
            return fin

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
            
    # Below are the methods of the BinarySearchTree class. 
    def __init__(self, root=None, contents=None):
        self.root = root
        if contents is not None:
            for x in contents:
                self.insert(x)
        
    def __insert(root, key):
        if root is None:            #tree is empty
            return BinarySearchTree.Node(key)     

        if key < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(), key))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(), key))

        return root
    def insert(self, val):
        self.root = BinarySearchTree.__insert(self.root, val)
        
    

    def __delete(root, key):

        def minValueNode(node):
            current = node

            while current.getLeft():
                current = current.getLeft()

            return current
        #Empty Tree
        if root is None:
            return None
        #if it is less than it is to the left subtree
        if key < root.getVal():
            root.setLeft(BinarySearchTree.__delete(root.getLeft(), key))
            
        #if it is greater than it must be to the right subtree
        elif key > root.getVal():
            root.setRight(BinarySearchTree.__delete(root.getRight(), key))
        #node = key this is the node to delete!
        else:
            if root.getLeft() is None:
                temp = root.getRight()
                root = None
                return temp
            elif root.getRight() is None:
                temp = root.getLeft()
                root = None
                return temp

            temp = minValueNode(root.getRight())        #get
            root.setVal(temp.getVal())                  #copy 
            root.setRight(BinarySearchTree.__delete(root.getRight(), temp.getVal()))    #delete

        return root
    
    def delete(self, val):
        self.root = BinarySearchTree.__delete(self.root, val)

    
    def __iter__(self):
        if self.root:
            return iter(self.root)
        else:
            return iter([])

    def inorder(self):
        if self.root:
            return list(self.root.inorder())
        else:
            return list(self.root.inorder())

    def preorder(self):
        if self.root:
            return list(self.root.preorder())
        else:
            return list(self.root.preorder())

    def postorder(self):
        if self.root:
            return list(self.root.postorder())
        else:
            return list(self.root.postorder())

    def levelorder(self):
        lst = []
        queue = Queue()
        queue.enqueue(self.root)
        while queue.isEmpty() == False:
            x = queue.dequeue()
            lst.append(x.getVal())      
            if x.getLeft() is not None:
                queue.enqueue(x.getLeft())
            if x.getRight() is not None:
                queue.enqueue(x.getRight())
        return lst

    def levelorderlvls(self):
        queue = Queue()
        lst = []
        queue.enqueue(self.root)
        while not queue.isEmpty():
            x = queue.dequeue()
            if x is not None:
                lst.append(x.getVal())
                queue.enqueue(x.getLeft())
                queue.enqueue(x.getRight())
            else:
                lst.append(None)

        return lst

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"


class Visualize(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.paused = False
        self.stop = False
        self.running = False
        self.locked = False

    def buildWindow(self):

       
        cv = ScrolledCanvas(self, 600, 600, 600, 600)
        cv.pack(side=tkinter.LEFT)
        t = RawTurtle(cv)
        screen = t.getscreen()
        screen.tracer(100000)

        screen.setworldcoordinates(screenMin, screenMin, screenMax, screenMax)
        screen.bgcolor("white")
        t.hideturtle()

        frame = tkinter.Frame(self)
        frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        tree = BinarySearchTree()


        def containsHandler():
            node = float(nodeInput.get())
            if node in tree:
                tkinter.messagebox.showwarning("Search Results", "Item is in tree!")
            else:
                tkinter.messagebox.showwarning("Search Results", "Item is NOT in tree!")           
        def insertHandler():
            node = float(nodeInput.get())
            tree.insert(node)
            t.clear()
            redraw()

             
        def deleteHandler():
            node = float(nodeInput.get())
            tree.delete(node)
            t.clear()
            redraw()

        

        def quitHandler():
            self.master.quit()

        def drawline(x0, y0, x1, y1):  # use top first, then bottom
            t.goto(x0, y0)
            t.down()
            t.goto(x1, y1+10)
            t.up()

        def redraw():
            lst = []
            lst = tree.levelorderlvls()
            lvl0 = []                               #Make empty lists for each depth level of tree
            lvl1 = []
            lvl2 = []
            lvl3 = []
            lvl4 = []
            lvl5 = []
            lvl6 = []
            for i in range(len(lst)):
                if len(lvl0) < 1:
                    lvl0.append(lst[i])
                elif len(lvl1) < 2:
                    lvl1.append(lst[i])
                elif len(lvl2) < 4:
                    lvl2.append(lst[i])
                elif len(lvl3) < 8:
                    lvl3.append(lst[i])
                elif len(lvl4) < 16:
                    lvl4.append(lst[i])
                elif len(lvl5) < 32:
                    lvl5.append(lst[i])
                elif len(lvl6) < 64:
                    lvl6.append(list[i])
            for x in lvl0:
                t.goto(150, 260)
                t.write(x, False)
            for i in range(len(lvl1)):                              #1 Level Draw
                if lvl1[i]:
                    drawline(150, 260, (i+1)*100, 220)
                    t.goto((i+1) * 100, 220)
                    t.write(lvl1[i], False, align="center")
            for i in range(len(lvl2)):                              #2 Level Draw
                if lvl2[i]:
                    drawline(((i//2) + 1)*100, 220, (i+1) * 60, 180)
                    t.goto((i+1)*60, 180)
                    t.write(lvl2[i], False, align="center")
            for i in range(len(lvl3)):                              #3 Level Draw
                if lvl3[i]:
                    drawline(((i // 2) + 1) * 60, 180, (i+1)*33, 140)
                    t.goto((i+1)*33, 140)
                    t.write(lvl3[i], False, align="center")
            for i in range(len(lvl4)):                              #4 Level draw
                if lvl4[i]:
                    drawline(((i // 2) + 1) * 33, 140, (i + 1) * 17, 100)
                    t.goto((i+1)*17, 100)
                    t.write(lvl4[i], False, align="center")
            for i in range(len(lvl5)):                              #5 level draw
                if lvl5[i]:
                    drawline(((i // 2) + 1) * 17, 100, (i + 1) * 9, 60)
                    t.goto((i+1)*9, 60)
                    t.write(lvl[i], False, align="center")
            for i in range(len(lvl6)):                              #6 level draw
                if lvl6[i]:
                    drawline(((i // 2) + 1) * 9, 60, (i + 1) * 4, 20)
                    t.goto((i+1)*4, 20)
                    t.write(lvl[i], False, align="center")

        quitButton = tkinter.Button(frame, text="Quit", command=quitHandler)        #Quit button
        quitButton.pack()

        text = tkinter.Label(frame, text="Node Value:")                             
        text.pack()

        nodeInput = tkinter.Entry(frame, width=20)
        nodeInput.pack()

        insertButton = tkinter.Button(frame, text="Insert", command=insertHandler)  #Insert Button
        insertButton.pack()

        deleteButton = tkinter.Button(frame, text="Remove", command=deleteHandler)  #Delete Button
        deleteButton.pack()

        containsButton = tkinter.Button(frame, text="Contains?", command=containsHandler)   #Contatins Button
        containsButton.pack()


def main():
    root = tkinter.Tk()
    root.title("Binary Tree Visualization")
    tree = Visualize(root)
    tree.mainloop()


if __name__ == "__main__":
    main()    
