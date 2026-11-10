from pathlib import Path
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
IMAGES = Path(__file__).parent / "images"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", background=THEME_COLOR,
                                 font=("Arial", 12, "bold"))
        self.score_label.grid(column=2, row=0)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=1, row=1, columnspan=2, pady=40)

        # Keep references on self so tkinter doesn't garbage-collect the images
        self.true_image = PhotoImage(file=IMAGES / "true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)

        self.false_image = PhotoImage(file=IMAGES / "false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=2, row=2)

        self.next_question()

        self.window.mainloop()

    def set_buttons(self, state):
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.set_buttons("normal")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz.\n\n"
                     f"Final score: {self.quiz.score}/{self.quiz.question_number}")
            self.set_buttons("disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        # Lock the buttons so one question can't be answered (and scored) twice
        self.set_buttons("disabled")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="#4caf50" if is_right else "#e53935")
        self.window.after(1000, self.next_question)
