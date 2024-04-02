# import modules
from tkinter import *


# define all functions
def draw_with_brush(event):
    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x
    y_position_of_click = event.y

    # define a circle with the mouse click at its center
    x1 = x_position_of_click - 5
    y1 = y_position_of_click - 5
    x2 = x_position_of_click + 5
    y2 = y_position_of_click + 5
    colour = "green"
    outline = "blue"
    # draw a circle while button_1 active and mouse is moving
    canvas.create_oval(x1, y1, x2, y2, fill=colour, outline=outline)


# create window
window = Tk()
window.title("Python GUI with tkinter canvas widget")
window.geometry("850x500")

# create widgets
canvas = Canvas(window)

# place widgets into window container using the pack layout
canvas.pack(fill=BOTH, expand=1)

# bind widget events to functions
canvas.bind("<B1-Motion>", draw_with_brush)

# open window
window.mainloop()
