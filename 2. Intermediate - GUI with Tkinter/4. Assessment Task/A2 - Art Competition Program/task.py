# import modules
from tkinter import *
from tkinter import messagebox

# define global variables
radio_button_values = ["Male", "Female", "Unspecified"]


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


def confirm():
    # display the colour choice selected using the radio buttons
    print("personal data value is:" + str(personal_data_usage_value.get()))
    if personal_data_usage_value.get() == 1:
        messagebox.showinfo("Submission Accept", "Your artwork has been entered into the prize draw.")
    else:
        messagebox.showinfo("Data Privacy Policy", "To continue you must accept the terms on usage of personal data")


# create window
window = Tk()
window.title("Python GUI with tkinter radio buttons, check and message boxes")
window.geometry("840x300")

# define all global tkinter variables (only after initialising the Tk window)
personal_data_usage_value = IntVar()
is_student_value = IntVar()
is_worker_bee_value = IntVar()
is_influencer_value = IntVar()
colour_choice = StringVar()
colour_choice.set("Red")

# create and layout radio button widget
for index in range(3):
    gender_label = Label(window, text=radio_button_values[index])
    gender_radio_button = Radiobutton(variable=colour_choice, value=radio_button_values[index])
    gender_label.grid(row=10, column=0 + index)
    gender_radio_button.grid(row=11, column=0 + index)

# create other widgets
canvas = Canvas(window, bg="grey")

# create other submission form widgets
first_name_label = Label(text="First name:")
first_name_entry = Entry()
family_name_entry = Entry()
family_name_label = Label(text="Family name:")
birth_date_label = Label(text="Date of Birth:")
personal_data_usage_label = Label(window, text="Personal data will be collected")
personal_data_usage_checkbutton = Checkbutton(variable=personal_data_usage_value, onvalue=1)
is_student_label = Label(text="Student?")
is_student_checkbutton = Checkbutton(variable=is_student_value, onvalue=None)
is_worker_bee_label = Label(text="Worker Bee?")
is_worker_bee_checkbutton = Checkbutton(variable=is_worker_bee_value, onvalue=None)
is_influencer_label = Label(text="Influencer?")
is_influencer_checkbutton = Checkbutton(variable=is_influencer_value, onvalue=None)
button1 = Button(window, text="Submit", command=confirm)

# create a frame widget to hold the birth_date spinboxes
birth_date_frame = Frame()
birth_day_spinbox = Spinbox(birth_date_frame, from_=1, to=31, width=2)
birth_month_spinbox = Spinbox(birth_date_frame, from_=1, to=12, width=2)
birth_year_spinbox = Spinbox(birth_date_frame, from_=1900, to=2010, width=4)

# place widgets into window container using the grid layout
first_name_label.grid(row=7, column=0)
first_name_entry.grid(row=7, column=1)
family_name_label.grid(row=8, column=0)
family_name_entry.grid(row=8, column=1)
birth_date_label.grid(row=9, column=0)

# place birth_date frame right of birth_date label
birth_date_frame.grid(row=9, column=1)
# place birth_date spinboxes inside frame container using the grid layout
birth_day_spinbox.grid(row=1, column=1)
birth_month_spinbox.grid(row=1, column=2)
birth_year_spinbox.grid(row=1, column=3)

# row 10,11 are used by the gender radio buttons
is_student_label.grid(row=12, column=0)
is_student_checkbutton.grid(row=13, column=0)
is_worker_bee_label.grid(row=12, column=1)
is_worker_bee_checkbutton.grid(row=13, column=1)
is_influencer_label.grid(row=12, column=2)
is_influencer_checkbutton.grid(row=13, column=2)
personal_data_usage_label.grid(row=14, column=0)
personal_data_usage_checkbutton.grid(row=14, column=1)
button1.grid(row=16, column=0, columnspan=2)

canvas.grid(row=1, column=4, rowspan=15, columnspan=15)

# bind widget events to functions
canvas.bind("<B1-Motion>", draw_with_brush)

# open window
window.mainloop()
