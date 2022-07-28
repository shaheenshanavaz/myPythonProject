from tkinter import *
THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        # TODO Creatinga canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        # Adding an image in a canvas
        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")
        # self.canvas.create_image(100, 113, image=self.true_img)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some text here",
            fill=THEME_COLOR,
            font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Creating Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # Creating /buttons
        self.true_button = Button(image=self.true_img)
        self.true_button.grid(row=2,column=0)
        self.false_button = Button(image=self.false_img)
        self.false_button.grid(row=2, column=1)
        self.windows.mainloop()