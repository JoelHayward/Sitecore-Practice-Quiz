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
        self.master.geometry("1200x600")

        self.frame_questions = tk.Frame(master, width=600, height=600, bd=1)
        self.frame_questions.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.frame_scores = tk.Frame(master, width=600, height=600, bd=1)
        self.frame_scores.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.questions = [
            Question("What does the abbreviation 'CDN' stand for in the context of Sitecore?", "Content Delivery Network", ["Content Development Network", "Custom Design Node", "Core Database Node"]),
    Question("What is the main purpose of Sitecore's xDB?", "Collect and connect customer data to provide a comprehensive view of the customer", ["Improve website speed", "Manage website themes", "Secure customer data"]),
    Question("Which of the following is NOT a feature of Sitecore's xDB?", "It allows you to build and deploy websites", ["It collects customer data from all channels", "It connects customer data for a comprehensive view", "It allows for personalization based on collected data"]),
    Question("What is the main function of Sitecore's Universal Tracker?", "Tracking user interactions across multiple channels", ["Improving search performance", "Managing multiple websites", "Automating marketing tasks"]),
    Question("What is the purpose of a xConnect client in Sitecore?", "It serves as an intermediary between your application and xConnect, allowing you to read, write, and search for contacts and interactions", ["It creates new websites", "It manages user permissions", "It improves website load times"]),
    Question("What is the purpose of dividing configuration files into layers in Sitecore?", "To control load order and provide better control over when files are loaded at runtime", ["To increase file size", "To improve UI", "To reduce system requirements"]),
    Question("What is the function of the Sitecore layer in Sitecore's configuration files?", "It contains configuration files for standard Sitecore components and features", ["It contains user data", "It contains security settings", "It contains network configurations"]),
    Question("What is the function of the Modules layer in Sitecore's configuration files?", "It contains configuration files for official Sitecore modules", ["It contains configuration files for Sitecore themes", "It contains configuration files for users", "It contains security settings"]),
    Question("What is the function of the Custom layer in Sitecore's configuration files?", "It contains the patch files you create in order to modify settings in the default Sitecore configuration", ["It contains user data", "It contains security settings", "It contains network configurations"]),
    Question("What is the function of the Environment layer in Sitecore's configuration files?", "It contains the patch files you create to configure Sitecore for different environments, such as QA, production, or development", ["It contains security settings", "It contains network configurations", "It contains user data"]),
    Question("In which layers are you allowed to change Sitecore settings by placing patch files?", "Custom and Environment", ["Sitecore and Modules", "Sitecore and Custom", "Modules and Environment"]),
    
            # Add your questions here...
        ]

        random.shuffle(self.questions)
        self.questions = self.questions[:50]

        self.current_question = 0
        self.score = 0
        self.all_scores = self.load_all_scores()

        self.question_label = tk.Label(self.frame_questions, text="", wraplength=380, anchor="w", padx=10, pady=10)
        self.answer_buttons = []
        self.next_button = None
        self.score_label = tk.Label(self.frame_scores, text="Score: 0 / 0", padx=10, pady=10, anchor="w")
        self.top_score_label = tk.Label(self.frame_scores, text=self.format_top_scores(), padx=10, pady=10, anchor="w")
        self.average_score_label = tk.Label(self.frame_scores, text=self.calculate_average_score(), padx=10, pady=10, anchor="w")

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

        self.all_scores.append(percentage)
        self.save_all_scores()

        self.top_score_label['text'] = self.format_top_scores()
        self.average_score_label['text'] = self.calculate_average_score()

        self.show_restart_prompt()

    def calculate_average_score(self):
        if self.all_scores:
            average_score = sum(self.all_scores) / len(self.all_scores)
            return f"Average Score: {average_score:.2f}%"
        else:
            return "Average Score: N/A"

    def format_top_scores(self):
        if self.all_scores:
            highest_score = max(self.all_scores)
            return f"Top Score: {highest_score:.2f}%"
        else:
            return "Top Score: None"

    def save_all_scores(self):
        with open("all_scores.txt", "w") as file:
            for score in self.all_scores:
                file.write(f"{score}\n")

    def load_all_scores(self):
        try:
            with open("all_scores.txt", "r") as file:
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
