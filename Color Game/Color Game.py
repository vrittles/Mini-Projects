import random
from tkinter import *
from tkinter import messagebox 

colors = ['Red', 'Green', 'Blue', 'Black', 'White', 'Yellow', 'Pink', 'Orange', 'Violet']

score = 0

timeleft = 15

def startGame(event):
    global score
    global timeleft
    
    if timeleft == 15:
        countdown()
        
    checkColor()
    

def checkColor():
    global score
    global timeleft
    
    if timeleft > 0:
        
        if e.get().lower() == colors[0].lower():
            score += 1
            
        e.delete(0, 'end')
        
        random.shuffle(colors)
        
        l.config(fg = str( colors[0]), text = str( colors[1] ) )
        
        score_lbl.config(text = "Score : " + str(score))

        e.focus_set()
        
def countdown():

    global timeleft
    
    if timeleft > 0:
        timeleft -= 1
        
    time_lbl.config(text = "Time left : " + str(timeleft))
    
    time_lbl.after(1000, countdown)
    
    
root = Tk()
root.title("Color Game")
root.geometry("300x200")

instructions = Label(root, text = "Press Enter to START the Game\nEnter the Color of LETTERS displayed")
instructions.pack()

score_lbl = Label(root, text = "Score : 0")
score_lbl.pack()

time_lbl = Label(root, text = "Time left : 15")
time_lbl.pack()

l = Label(root)
l.pack()

e = Entry(root)

root.bind("<Return>", startGame)
e.pack()
e.focus_set()

root.mainloop()
