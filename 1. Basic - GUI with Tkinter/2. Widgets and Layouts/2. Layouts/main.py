# import modules
from tkinter import *

# create the window
window = Tk()
window.title("Python GUI with Tkinter - Layouts")

# create the widgets
text1 = Label(window, text="This application demonstrates simple layout")
button1 = Button(window, text="Button 1", fg="green")
button2 = Button(window, text="Button 2", fg="red")   # TODO create a red button)
button3 = Button(window, text="Button 3", fg="blue")   # TODO create a blue button
text2 = Label(window, text="This is another simple label")

# place widgets into window container using the pack layout
text1.pack()
button1.pack()
button2.pack()
button3.pack()
text2.pack()

# open window
window.mainloop()
