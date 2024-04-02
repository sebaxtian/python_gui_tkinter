# import modules
from tkinter import *


# define all functions
# TODO define a function that updates the text option of label1 with "Hello"
def say_hello(event):
    label1.config(text="Hello")


# TODO define a function that updates the text option of label1 with "Goodbye"
def say_goodbye(event):
    label1.config(text="Goodbye")


# create window
window = Tk()
window.title("Exercise 9")
window.geometry("300x300")

# create widgets
label1 = Label()

# place widgets into window container using the pack layout
label1.pack()

# bind widget events to functions
window.bind("<Enter>", say_hello)
window.bind("<Leave>", say_goodbye)   # TODO bind the window to the input event for when the mouse leaves the window

# open window
window.mainloop()
