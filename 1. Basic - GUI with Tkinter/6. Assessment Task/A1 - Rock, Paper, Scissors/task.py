# import modules
from tkinter import *
import random

# define global variables
user_score = 0
computer_score = 0
user_choice = ""
computer_choice = ""
rps = ("rock", "paper", "scissors")


# define all functions
def choice_to_number(choice):
    return rps.index(choice)


def number_to_choice(number):
    return rps[number]


def random_choice():
    return random.choice(rps)


def result(user_choice_string, computer_choice_string):
    global user_score
    global computer_score

    user_choice_number = choice_to_number(user_choice_string)
    computer_choice_number = choice_to_number(computer_choice_string)

    if user_choice_number==computer_choice_number:
        print("tie")
    elif (user_choice_number-computer_choice_number)%3 == 1:
        print("you win :(")
        user_score = user_score + 1
    else:
        print("you LOSE sucker!")
        computer_score = computer_score + 1
    text_area.config(text="Your Choice: {uc} \nMy Choice : {cc} \n Your Score : {us} \n Computer Score : {cs} ".format(uc=user_choice,cc=computer_choice,us=user_score,cs=computer_score))

def rock():
    global user_choice
    global computer_choice
    user_choice = "rock"
    computer_choice=random_choice()
    result(user_choice, computer_choice)


def paper():
    global user_choice
    global computer_choice
    user_choice = "paper"
    computer_choice=random_choice()
    result(user_choice, computer_choice)


def scissors():
    global user_choice
    global computer_choice
    user_choice = "scissors"
    computer_choice=random_choice()
    result(user_choice, computer_choice)


# create window
window = Tk()
window.title("Rock, Paper, Scissors - A Game for All!")
window.geometry("400x300")


# create widgets
rock_button = Button(text="Rock", command=rock)
paper_button = Button(text="Paper", command=paper)
scissors_button = Button(text="Scissors", command=scissors)
text_area = Label(text="Welcome!", bg="yellow", height=6, width=20, font=("Arial", 25))

# place widgets into window container using a layout
rock_button.grid(row=0, column=0)
paper_button.grid(row=0, column=1)
scissors_button.grid(row=0, column=2)
text_area.grid(row=3, column=0, columnspan=3, rowspan=3)

# open window
window.mainloop()
