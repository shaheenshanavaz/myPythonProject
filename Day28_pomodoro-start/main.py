import math
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mytimer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(mytimer)
    #timer_text = 00
    canvas.itemconfig(timer_count, text="00:00")
    #timer_label = Timer
    timer_label.config(text="Timer")
    #reset checkmarks
    check_box.config(text="")
    # reps to start again
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    # # TODO For reps 1 3 5 7
    if reps % 8 == 0:
        count_down(long_sec)
        timer_label.config(text="Break", fg=RED)
        window.bell()
    elif reps % 2 == 0:
        count_down(short_sec)
        timer_label.config(text="Break", fg=PINK)

        # TODO Notification sound
        window.bell()
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Calculating the mins and sec
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # TODO Dynamic Programming
    # Changing the seconds 9 to 09,08,07 etc
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Representing 0 sec to 00
    if count_sec == 0:
        count_sec = "00"

    # 1000 millisec break after every second count
    if count > 0:
        global mytimer
        mytimer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_box.config(text=marks)
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#TODO Creatinga canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#Adding an image in a canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

#start  button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

#reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

#check mark
check_box = Label(font=12, fg=GREEN, bg=YELLOW)
check_box.grid(column=1, row=3)






window.mainloop()