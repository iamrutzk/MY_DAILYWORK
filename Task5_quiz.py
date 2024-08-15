import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.geometry("400x300")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Saturn", "Jupiter", "Uranus"],
                "correct_answer": "Jupiter"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
                "correct_answer": "Leonardo da Vinci"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Ag", "Au", "Hg", "Pb"],
                "correct_answer": "Au"
            },
            {
                "question": "What is the smallest country in the world?",
                "options": ["Vatican City", "Monaco", "Nauru", "Tuvalu"],
                "correct_answer": "Vatican City"
            }
        ]

        self.current_question = random.choice(self.questions)
        self.score = 0

        self.question_label = tk.Label(self.window, text=self.current_question["question"], wraplength=400)
        self.question_label.pack()

        self.option_buttons = []
        for i, option in enumerate(self.current_question["options"]):
            button = tk.Button(self.window, text=option, command=lambda option=option: self.check_answer(option))
            button.pack()
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack()

    def check_answer(self, user_answer):
        if user_answer == self.current_question["correct_answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect answer. The correct answer is {self.current_question['correct_answer']}.")

        self.score_label.config(text=f"Score: {self.score}")

        self.current_question = random.choice(self.questions)
        self.question_label.config(text=self.current_question["question"])

        for button in self.option_buttons:
            button.pack_forget()

        self.option_buttons = []
        for i, option in enumerate(self.current_question["options"]):
            button = tk.Button(self.window, text=option, command=lambda option=option: self.check_answer(option))
            button.pack()
            self.option_buttons.append(button)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = QuizGame()
    game.run()