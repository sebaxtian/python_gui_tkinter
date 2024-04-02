# import modules
from tkinter import *

# create window
window = Tk()
window.title("Exercise 1")

# create widgets
top_frame = Frame(window)
middle_frame = Frame(window)
bottom_frame = Frame(window)

text1 = Label(top_frame, text="This application demonstrates frame layout")
# TODO Create and frame your 4 buttons here
button1 = Button(middle_frame, text="Button 1", fg="green")
button2 = Button(middle_frame, text="Button 2", fg="red")
button3 = Button(bottom_frame, text="Button 3", fg="blue")
button4 = Button(bottom_frame, text="Button 4", fg="blue")

# place widgets into window container using the pack layout
top_frame.pack()
middle_frame.pack()
bottom_frame.pack()
text1.pack()
# TODO Pack your 4 buttons into the window
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

# open window
window.mainloop()
