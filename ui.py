from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
         self.quiz = quiz_brain
         self.window = Tk()
         self.window.title("Quizzyy")
         self.window.config(padx=20, pady=20, bg=THEME_COLOR)

         self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
         self.score_label.grid(row=0, column=1)

         self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
         self.question_text = self.canvas.create_text(
             150,
             125,
             width = 280,
             text="Some Question Text",
             fill = THEME_COLOR,
             font=("Ariel", 20, "italic")
         )
         self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

         true_img = PhotoImage(file= "images/true.png")
         self.true=Button(image=true_img, highlightthickness=0, command=self.true_pressed)
         self.true.grid(row=2, column=1)

         false_img = PhotoImage(file="images/false.png")
         self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
         self.false.grid(row=2, column=0)

         self.get_next_question()

         self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
       is_right = self.quiz.check_answer("False")
       self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)