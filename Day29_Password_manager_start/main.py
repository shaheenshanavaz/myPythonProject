from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwd_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letter = [random.choice(letters) for char in range(nr_letters)]
    password_symbol = [random.choice(symbols) for char in range(nr_symbols)]
    password_number = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)
    password = "".join(password_list)

    # changing the password input as a random generated password
    password_input.insert(0, password)
    pyperclip.copy(text=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_tofile():
    mywebsite = web_input.get()
    myemail = email_input.get()
    mypasswd = password_input.get()
    if len(mywebsite) == 0 or len(mypasswd) == 0:
        messagebox.showinfo(title="ERROR", message="Please fill the required fields")
    else:
        is_ok = messagebox.askokcancel(title=mywebsite, message=f"These are the fields entered:\n Email:{myemail}\n "
                                                                f"Password:{mypasswd}\n Is it ok to save?")

        if is_ok:
            with open(file="data.txt", mode="a") as myfile:
                myfile.write(f"{mywebsite} | {myemail} | {mypasswd}\n")
                # TODO to clear all entries after writing to the file
                web_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

#website label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
#website entry
web_input = Entry(width=55)
web_input.focus()
web_input.grid(column=1, row=1, columnspan=2, sticky="w")

#Email label
email_label = Label(text="Email/UserName:")
email_label.grid(column=0, row=2)
#email entry
email_input = Entry(width=55)
# To add value to Entry using .insert method
email_input.insert(0, "shaheen.shanavaz@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="w")

#Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
#password entry
password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=2, sticky="w")

#Password Buttton
password_button = Button(text="Generate Password", command=passwd_generator)
password_button.grid(column=2, row=3)
#Add Button
add_button = Button(text="ADD", width=45,  command=save_tofile)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
