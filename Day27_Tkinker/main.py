from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

#label
label = Label(text="New text")
label.pack()
label.config(text="new text")
#Button
def button_clicked():
    print("I am clicked")
    label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()


window.mainloop()