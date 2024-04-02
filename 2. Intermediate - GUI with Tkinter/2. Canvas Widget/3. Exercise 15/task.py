# import modules
from tkinter import *

# create window
window = Tk()
window.title("Exercise 15")
window.geometry("850x500")

# create widgets
canvas = Canvas(window)

# place widgets into window container using the pack layout
canvas.pack(fill=BOTH, expand=1)

# Make some a stick figure

# The Head
x1 = 175
y1 = 180
x2 = 225
y2 = 230
colour="blue"
width=5
outline="grey"
canvas.create_oval(x1, y1, x2, y2, fill=colour, width=width, outline=outline)

# The Body
x1 = 200
y1 = 230
x2 = 200
y2 = 350
width = 20
canvas.create_line(x1, y1, x2, y2, width=width)
# The Arms
x1 = 150
y1 = 250
x2 = 250
y2 = 250
width = 20
canvas.create_line(x1, y1, x2, y2, width=width)
# The Left Leg
x1 = 200
y1 = 330
x2 = 150
y2 = 400
width = 20
canvas.create_line(x1, y1, x2, y2, width=width)
# The Right Leg
x1 = 200
y1 = 330
x2 = 250
y2 = 400
width = 20
canvas.create_line(x1, y1, x2, y2, width=width)

# open window
window.mainloop()
