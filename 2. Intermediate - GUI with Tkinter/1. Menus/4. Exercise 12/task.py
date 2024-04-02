# import modules
from tkinter import *


# define all functions
def say_hello():
    print("hello there!")


def popup_menu_event(event):
    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x_root
    y_position_of_click = event.y_root
    # post/place the pop menu where the user clicked.
    popup_menu.post(x_position_of_click, y_position_of_click)


# create window
window = Tk()
window.title("Exercise 12")
window.geometry("400x300")

# create widgets
popup_menu = Menu(window)
menu_bar = Menu(window)

edit_menu = Menu(menu_bar)

view_menu = Menu(menu_bar)

help_menu = Menu(menu_bar)

file_menu = Menu(menu_bar)
save_submenu = Menu(file_menu)

# configure widgets
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="Save", menu=save_submenu)
save_submenu.add_command(label="Save...")
save_submenu.add_command(label="Save as...")
save_submenu.add_command(label="Save all")
file_menu.add_command(label="Open", command=say_hello)
file_menu.add_command(label="New", command=say_hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit())

menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Find")

menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom in")
view_menu.add_command(label="Zoom out")
view_menu.add_separator()
view_menu.add_command(label="View options")
view_menu.add_separator()
view_menu.add_command(label="Recent changes")

menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Getting started")
help_menu.add_command(label="Tip of the day")
help_menu.add_command(label="Open help")
help_menu.add_command(label="Submit bug report")

popup_menu.add_command(label="Copy")
popup_menu.add_command(label="Paste")

# bind widget events to functions
window.bind("<Button-3>", popup_menu_event)

# configure window
window.config(menu=menu_bar)

# open window
window.mainloop()
