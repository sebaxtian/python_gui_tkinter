# import modules
from tkinter import *
from tkinter import messagebox

# define all functions


def confirm():
    # display the colour choice selected using the radio buttons
    print(colour_choice.get())
    if yes_no_value.get() == 1:
        messagebox.showinfo("Colour Choice", "Why did you choose " + colour_choice.get() + "?")
    else:
        messagebox.showinfo("Incomplete Form", "You must confirm your choice")


# create window
window = Tk()
window.title("Python GUI with tkinter radio buttons, check and message boxes")
window.geometry("550x200")

# define all global tkinter variables (only after initialising the Tk window)
yes_no_value = IntVar()
colour_choice = StringVar()
colour_choice.set("Red")

# create widgets
label1 = Label(window, text="Red")
radio_button1 = Radiobutton(variable=colour_choice, value="Red")
label2 = Label(window, text="Green")
radio_button2 = Radiobutton(variable=colour_choice, value="Green")
label3 = Label(window, text="Yellow")
radio_button3 = Radiobutton(variable=colour_choice, value="Yellow")
label4 = Label(window, text="Blue")
radio_button4 = Radiobutton(variable=colour_choice, value="Blue")
label5 = Label(window, text="Black")
radio_button5 = Radiobutton(variable=colour_choice, value="Black")

yes_no_label = Label(window, text="Confirmed")
yes_no_checkbutton = Checkbutton(variable=yes_no_value, onvalue=1)

button1 = Button(window, text="Submit", command=confirm)

# place widgets into window container using the grid layout
index = 1
label1.grid(row=index, column=0)
radio_button1.grid(row=index, column=1)
index = 2
label2.grid(row=index, column=0)
radio_button2.grid(row=index, column=1)
index = 3
label3.grid(row=index, column=0)
radio_button3.grid(row=index, column=1)
index = 4
label4.grid(row=index, column=0)
radio_button4.grid(row=index, column=1)
index = 5
label5.grid(row=index, column=0)
radio_button5.grid(row=index, column=1)

yes_no_label.grid(row=6, column=0)
yes_no_checkbutton.grid(row=6, column=1)

button1.grid(row=7, column=0, columnspan=2)

# open window
window.mainloop()
