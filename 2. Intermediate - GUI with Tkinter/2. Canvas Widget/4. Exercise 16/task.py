# import modules
from tkinter import *


# define all functions
def draw_rectangle(event):
    rectangle_height = 20
    rectangle_length = rectangle_height * 2

    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x
    y_position_of_click = event.y

    # define a rectangle with the mouse click at its center
    x1 = x_position_of_click - rectangle_length / 2
    y1 = y_position_of_click - rectangle_height / 2
    x2 = x_position_of_click + rectangle_length / 2
    y2 = y_position_of_click + rectangle_length / 2
    colour = "green"
    outline = "blue"
    # draw a circle while button_1 active and mouse is moving
    canvas.create_rectangle(x1, y1, x2, y2, fill=colour, outline=outline)


# create window
window = Tk()
window.title("Exercise 16")
window.geometry("850x500")

# create widgets
canvas = Canvas(window)

# place widgets into window container using the pack layout
canvas.pack(fill=BOTH, expand=1)

# bind widget events to functions
canvas.bind("<B1-Motion>", draw_rectangle)

# open window
window.mainloop()
