# import modules
from tkinter import *

# create window
window = Tk()
window.title("Exercise 6")
window.geometry("300x350")

# create widgets
# TODO create 2 labels and 4 buttons
label1 = Label(window, text="TEXT 1")
button1 = Button(window, text="BUTTON 1")
button2 = Button(window, text="BUTTON 2")
button3 = Button(window, text="BUTTON 3")
button4 = Button(window, text="BUTTON 4")
label2 = Label(window, text="TEXT 2")

# place widgets into window container using the grid layout
# TODO use a grid layout to position the widgets
label1.grid(row=0, column=0)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=2, column=0)
button4.grid(row=2, column=1)
label2.grid(row=1, column=2, columnspan=2, rowspan=2)

# open window
window.mainloop()
