# import modules
from tkinter import *


# define all functions
def save():
    pass


def save_as():
    pass


def save_all():
    pass


def file_open():
    pass


def file_new():
    pass


def edit_cut():
    pass


def edit_copy():
    pass


def edit_paste():
    pass


def edit_find():
    pass


def view_zoom_in():
    pass


def view_zoom_out():
    pass


def view_options():
    pass


def view_recent_changes():
    pass


def help_getting_started():
    pass


def help_tip_of_day():
    pass


def help_open_help():
    pass


def help_submit_bug_report():
    pass


def popup_menu_event(event):
    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x_root
    y_position_of_click = event.y_root
    # post/place the pop menu where the user clicked.
    popup_menu.post(x_position_of_click, y_position_of_click)


# create window
window = Tk()
window.title("Exercise 14")
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
save_submenu.add_command(label="Save...", command=save)
save_submenu.add_command(label="Save as...", command=save_as)
save_submenu.add_command(label="Save all", command=save_all)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="New", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=edit_find)

menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom in", command=view_zoom_in)
view_menu.add_command(label="Zoom out", command=view_zoom_out)
view_menu.add_separator()
view_menu.add_command(label="View options", command=view_options)
view_menu.add_separator()
view_menu.add_command(label="Recent changes", command=view_recent_changes)

menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Getting started", command=help_getting_started)
help_menu.add_command(label="Tip of the day", command=help_tip_of_day)
help_menu.add_command(label="Open help", command=help_open_help)
help_menu.add_command(label="Submit bug report", command=help_submit_bug_report)

popup_menu.add_command(label="Copy", command=edit_copy)
popup_menu.add_command(label="Cut", command=edit_cut)
popup_menu.add_command(label="Paste", command=edit_paste)
popup_menu.add_command(label="Find", command=edit_find)
popup_menu.add_separator()
popup_menu.add_command(label="Help", command=help_open_help)

# bind widget events to functions
window.bind("<Button-3>", popup_menu_event)

# configure window
window.config(menu=menu_bar)

# open window
window.mainloop()
