#errors so far: 
#no input into search bars = python crashes
#states with a space in their names (ex: north dakota, south carolina) into search bars = python crashes
#city is wonky: it causes python to crash most of the time
#if city has an input but not state: python crashes
#if py

# myString
# if not myString: print("hi")

import tkinter
from tkinter import messagebox

tk_box = tkinter.Tk()
tk_box.withdraw() #there was a tk pop up box along side the actual error box, apparently this makes it go away
def no_input():
    raise ValueError 

# i don't know exactly how to get it to recognize that no input was given into the search bars
try:
    no_input()
except ValueError:
    messagebox.showerror("Error", "No input has been received. Please try again.")

