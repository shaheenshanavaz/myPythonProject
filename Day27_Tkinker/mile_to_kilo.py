from tkinter import *

window = Tk()
window.title("Mile to kilometer converter")
window.minsize(width=300, height=100)

#Label
equal_label = Label(text="label", font=("Arial", 13))
equal_label.config(text="to equal to")
equal_label.grid(column=0, row=1)

#Entry
input = Entry(width=10)
input.grid(column=4, row=0)

#Label
mile_label = Label(text="Miles", font=("Arial", 13))
mile_label.grid(column=5, row=0)

#Label
ans_label = Label(text="0", font=("Arial", 13))
ans_label.grid(column=4, row=1)

#Label
kilo_label = Label(text="KM", font=("Arial", 13))
kilo_label.grid(column=5, row=1)

#Button
def calculate_miles():
    mile_value = input.get()
    kilo_value = int(mile_value) * 1.609344
    ans_label.config(text=kilo_value)
    # ans_label.config(text=input.get() * 1.609344)


button = Button(text="Calculate", command=calculate_miles)
button.grid(column=4, row=2)

window.mainloop()
