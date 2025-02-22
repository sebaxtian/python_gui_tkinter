# import modules
from tkinter import *

# create window
window = Tk()
window.title("Python GUI with tkinter canvas widget")
window.geometry("850x500")

# create widgets
canvas = Canvas(window)

# place widgets into window container using the pack layout
canvas.pack(fill=BOTH, expand=1)

# Make some aRt!
# create a rectangle with create_rectangle
x1 = 20
y1 = 20
x2 = 300
y2 = 200
colour = "red"
canvas.create_rectangle(x1, y1, x2, y2, fill=colour)
# create a oval with create_oval
x1 = 50
y1 = 50
x2 = 300
y2 = 300
colour = "blue"
width = 10
outline = "grey"
canvas.create_oval(x1, y1, x2, y2, fill=colour, width=width, outline=outline)
# create a line with create_line
x1 = 100
y1 = 130
x2 = 250
y2 = 300
width = 20
canvas.create_line(x1, y1, x2, y2, width=width)
# create a arc with create_arc
x1 = 10
y1 = 50
x2 = 300
y2 = 300
width = 10
canvas.create_arc(x1, y1, x2, y2, width=width)
# create a text with create_text
x1 = 400
y1 = 400
text = "Digital Technologies\nMake the rockin' World Go Round!"
justify = CENTER
font = "Times", "40", "italic"
canvas.create_text(x1, y1, text=text, justify=justify, font=font)

# open window
window.mainloop()
