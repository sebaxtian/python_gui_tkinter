# 1. import required modules
from tkinter import *


# 2. define functions
def clicked():   # TODO choose an name for your function.():
    print("Hello there, I am working")


window = Tk()
window.title("Clicking application")
window.geometry("300x350")

button1 = Button(window, text="Click me!", command=clicked, activebackground="red")   # TODO add the code to create a button.
button1.pack()

window.mainloop()
