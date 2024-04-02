# import modules
from tkinter import *

# create window
window = Tk()
window.title("Python GUI with tkinter scale and spinbox")
window.geometry("450x100")

# create widgets
scale = Scale(window)
spinbox = Spinbox(window)

# configure widgets
scale.config(from_=10, to=500, orient=HORIZONTAL)
spinbox_values = ("One", "Two", "Three")
spinbox.config(values=spinbox_values)

# place widgets into window container using the pack layout
scale.pack()
spinbox.pack()

# open window
window.mainloop()
