from tkinter import *

window = Tk()
window.title("Exercise 2")

topFrame = Frame(window)
# TODO declare/create your button frames here
firstFrame = Frame(window)
secondFrame = Frame(window)
thirdFrame = Frame(window)

topFrame.pack()
# TODO pack your button frames into the window
firstFrame.pack()
secondFrame.pack()
thirdFrame.pack()

text1 = Label(topFrame, text="This application demonstrates frame layout")
# TODO make your button objects here (all 9 of them!)
button1 = Button(firstFrame, text="Button 1", fg="green")
button2 = Button(firstFrame, text="Button 2", fg="red")
button3 = Button(firstFrame, text="Button 3", fg="blue")

button4 = Button(secondFrame, text="Button 4", fg="blue")
button5 = Button(secondFrame, text="Button 5", fg="green")
button6 = Button(secondFrame, text="Button 6", fg="red")

button7 = Button(thirdFrame, text="Button 7", fg="blue")
button8 = Button(thirdFrame, text="Button 8", fg="blue")
button9 = Button(thirdFrame, text="Button 9", fg="blue")

text1.pack()
# TODO pack your buttons into the window here
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)

button7.pack(side=LEFT)
button8.pack(side=LEFT)
button9.pack(side=LEFT)


window.mainloop()
