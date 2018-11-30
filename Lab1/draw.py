import tkinter
import turtle
import sys

def main():
    root = tkinter.Tk() #creates the root window
    
    cv = tkinter.Canvas(root, width=600, height=600) #canvas widget
    cv.pack(side = tkinter.LEFT) # packs canvas into root window
    
    root.title("Draw!") #changes name of root window
    
    t = turtle.RawTurtle(cv) #create turtle
    
    screen = t.getscreen() #get screen from turtle
    
    frame = tkinter.Frame(root) #frame widget
    frame.pack(side = tkinter.RIGHT, fill=tkinter.BOTH)
    screen.tracer(0) #update screen
    
    textLab = tkinter.Label(frame,text= "Text to Write")
    textLab.pack()
    textVar = tkinter.StringVar()
    textEntry= tkinter.Entry(frame,textvariable=textVar)
    textEntry.pack()
    
    def writeHandler():
        t.write(textVar.get())
        
    Writebutton = tkinter.Button(frame, text = "Write Text", command =writeHandler)
    Writebutton.pack()
    
    def quitHandler():
        print("Goodbye")
        sys.exit(0)
    
    quitbutton = tkinter.Button(frame, text="quit", command=quitHandler)
    quitbutton.pack()
    
    def clickHandler(x,y): #create click handler
        t.goto(x,y)
        screen.update()
    screen.onclick(clickHandler) #calls the click handler
    
    def dragHandler(x,y):
        t.goto(x,y)
        screen.update()
    t.ondrag(dragHandler)
    
    
        
        

    
    
    
    
    
    
    
    tkinter.mainloop() #tells tkinter to listen for events
    
    
    
    
    
    
    





if __name__ == "__main__":
    main()