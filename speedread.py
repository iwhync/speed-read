from time import sleep
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter as tk

root = Tk()
root.title("Speed Read") # title bar
root.configure(background="white") # background
root.geometry("900x500") # size

default = """Hi, This is some speed reading software. You can use it by just hitting the button below this text box. The speed
option has 3 values. 1 is the fastest at 10 words a second, and 3 is the slowest at a little over 3 words a second. Try with
this text and see if you can keep up, but you can type over this or paste anything you like into this text box \n\n
Why use this? Well, it's handy if you want to read a large article with minimal effort. Your brain can take in far more than you
realise it can, and I'd imagine you're reading this word for word without much trouble. Enjoy!""" # default text

lbl1 = Label(root, text="Speed Read", font=("Ariel Bold", 70)) # where words will appear
lbl1.configure(background="White") # Making the text colour fit
lbl1.place(relx=.5, rely=.18, anchor="center") # in the middle
t = scrolledtext.ScrolledText(root, height = 15, width = 100, wrap=WORD, borderwidth=1, relief="solid") # our entry box
t.place(relx=.5, rely=.6, anchor="center") 
t.insert(1.0,default) # adding default text

lbl3 = Label(root, text="Select Speed", font=("Helvetica Bold", 10)) # speed selection label
lbl3.configure(background="white")
lbl3.place(relx=.80, rely=.88, anchor="w")

read = []

speed = [1,2,3] # speed options


speed_cb = ttk.Combobox(root, textvariable=speed) # dropdown speed box
speed_cb['values'] = speed 
speed_cb['state'] = 'readonly'  # normal
speed_cb.place(relx=.80, rely=.93, anchor="w")
speed_cb.current(0) # default at first item in list (1)

def get():
    spud = float("0."+str(speed_cb.get())) # taking from dropdown for our speed selection as number
    read = t.get("1.0",END) # taking text from entry box
    x = read.split() # split by " "
    length = len(x) # how many words
    a = 0 # variable for counting 
    while a < length: # to activate the script
        if (var1.get() == 1): # check if capitalize box is ticked
            x[a] = x[a].upper() # capitalize each word first
        lbl1.config(text = x[a]) # update label with each word
        sleep(spud) # sleep for speed selection
        Tk.update(lbl1) # update label with next word
        a += 1 # adding to counting variable
        
def paste(): # instead of right click menu
    t.delete("1.0","end") # delete all existing text from entry box
    t.focus() # select entry box
    t.event_generate('<Control-v>') # paste
    
var1 = tk.IntVar() # set capitalize checkbox as 1 or 0 
c1 = tk.Checkbutton(root, text="Capitalize?",variable=var1, onvalue=1, offvalue=0, bg="white") # for check button
c1.pack() 
c1.place(relx=.04, rely=.92, anchor="w")
        
btn0 = Button(root, text="Read", bg="black", fg="white",command=get) # finally buttons for functions
btn0.place(relx=.45, rely=.90, anchor="center")
btn0 = Button(root, text="Paste", bg="white", fg="black",command=paste)
btn0.place(relx=.38, rely=.90, anchor="w")


root.mainloop()
