from tkinter import *

window = Tk()
window.title("My second APP with mistakes")

text1 = Label(window, text="Hello World!")
text2 = Label(window, text="Programming with Python is much easier")
text3 = Label(window, text="I like using\n Tkinter")

text1.pack()
text2.pack()
text3.pack()

window.mainloop()
