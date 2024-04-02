from tkinter import *

window = Tk()
window.title("Exercise 3")

top_frame = Frame(window)
# TODO declare/create your frames here
left_frame = Frame(window)
right_frame = Frame(window)
buttom_frame1 = Frame(left_frame)
buttom_frame2 = Frame(left_frame)

top_frame.pack()
# TODO pack your frames here
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
buttom_frame1.pack()
buttom_frame2.pack()


text1 = Label(top_frame, text="This application demonstrates frame layout")
# TODO create your second Label here
text2 = Label(right_frame, text="This application demonstrates frame layout")

# TODO create your 4 buttons here
button1 = Button(buttom_frame1, text="Button 1", fg="green")
button2 = Button(buttom_frame1, text="Button 2", fg="red")

button3 = Button(buttom_frame2, text="Button 3", fg="blue")
button4 = Button(buttom_frame2, text="Button 4", fg="blue")

text1.pack()
# TODO don't forget to pack all your new widgets!
text2.pack()

button1.pack(side=LEFT)
button2.pack(side=LEFT)

button3.pack(side=LEFT)
button4.pack(side=LEFT)

window.mainloop()
