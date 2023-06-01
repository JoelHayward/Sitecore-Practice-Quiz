import random
import tkinter as tk
from tkinter import messagebox


class Question:
    def __init__(self, question, correct_answer, other_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.answers = other_answers
        self.answers.append(correct_answer)
        random.shuffle(self.answers)


class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Sitecore Practice Quiz")
        self.master.geometry("700x400")  # Adjust the size of the window if needed

        self.questions = [
            Question("What does the abbreviation 'CDN' stand for in the context of Sitecore?",
                     "Content Delivery Network",
                     ["Content Development Network", "Custom Design Node", "Core Database Node"]),
            Question("What is the main purpose of Sitecore's xDB?",
                     "Collect and connect customer data to provide a comprehensive view of the customer",
                     ["Improve website speed", "Manage website themes", "Secure customer data"]),
            # Add your questions here...
        ]

        # Shuffle the questions and select the first 50 questions
        random.shuffle(self.questions)
        self.questions = self.questions[:50]

        self.current_question = 0
        self.score = 0
        self.top_scores = self.load_top_scores()  # Load the top scores from the file

        self.question_label = tk.Label(master, text="", wraplength=380, anchor="w", padx=10, pady=10)
        self.answer_buttons = []
        self.next_button = None
        self.score_label = tk.Label(master, text="Score: 0 / 0", padx=10, pady=10, anchor="w")
        self.top_score_label = tk.Label(master, text=self.format_top_scores(), padx=10, pady=10, anchor="w")
        self.average_score_label = tk.Label(master, text=self.calculate_average_score(), padx=10, pady=10, anchor="w")

        self.question_label.pack()
        self.score_label.pack(anchor="w")
        self.top_score_label.pack(anchor="w")
        self.average_score_label.pack(anchor="w")

        self.show_question()

    def show_question(self):
        for button in self.answer_buttons:
            button.destroy()
        self.answer_buttons.clear()

        question = self.questions[self.current_question]
        question_number = self.current_question + 1
        self.question_label['text'] = f"Question {question_number}: {question.question}"

        for answer in question.answers:
            button = tk.Button(
                self.master,
                text=answer,
                width=60,
                wraplength=380,  # Adjust the wrap length as needed
                command=lambda ans=answer: self.check_answer(ans)
            )
            button.pack(pady=5)
            self.answer_buttons.append(button)

    def check_answer(self, selected_answer):
        question = self.questions[self.current_question]
        if selected_answer == question.correct_answer:
            self.score += 1
        self.current_question += 1
        total_questions = len(self.questions)
        self.score_label['text'] = f"Score: {self.score} / {total_questions}"

        correct_answer = question.correct_answer
        messagebox.showinfo("Answer", f"The correct answer is: {correct_answer}")

        if self.current_question < total_questions:
            self.show_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        percentage = (self.score / len(self.questions)) * 100
        message = f"You've completed the quiz with a score of {self.score} out of {len(self.questions)}\n" \
                  f"Percentage: {percentage:.2f}%"
        messagebox.showinfo("Quiz Finished", message)

        if percentage > max(self.top_scores):
            self.top_scores = [percentage]
            self.save_top_scores()

        self.top_score_label['text'] = self.format_top_scores()
        self.average_score_label['text'] = self.calculate_average_score()
        self.update_average_score_label()  # Update the average score label

        self.show_restart_prompt()

    def calculate_average_score(self):
        if self.top_scores:
            average_score = sum(self.top_scores) / len(self.top_scores)
            return f"Average Score: {average_score:.2f}%"
        else:
            return "Average Score: N/A"

    def format_top_scores(self):
        if self.top_scores:
            highest_score = max(self.top_scores)
            return f"Top Score: {highest_score:.2f}%"
        else:
            return "Top Score: None"

    def save_top_scores(self):
        with open("top_scores.txt", "w") as file:
            for score in self.top_scores:
                file.write(f"{score}\n")

    def load_top_scores(self):
        try:
            with open("top_scores.txt", "r") as file:
                return [float(line.strip()) for line in file]
        except FileNotFoundError:
            return []

    def show_restart_prompt(self):
        restart = messagebox.askyesno("Restart Quiz", "Do you want to restart the quiz?")
        if restart:
            self.restart_quiz()
        else:
            self.quit_quiz()

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.show_question()
        self.score_label['text'] = "Score: 0 / 0"
        self.update_average_score_label()  # Update the average score label

    def quit_quiz(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit the quiz?"):
            self.master.quit()

    def update_average_score_label(self):
        self.average_score_label['text'] = self.calculate_average_score()


root = tk.Tk()
quiz = Quiz(root)
root.mainloop()
