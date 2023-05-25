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
           Question("What is the primary programming language used to develop Sitecore?", "C#", ["PHP", "Java", "Python"]),
    Question("What is the main function of the Sitecore Content Management (CM) server?", "Editing and updating content", ["Rendering web pages", "Routing and load balancing", "Database management"]),
    Question("In Sitecore, what is the role of the Content Delivery (CD) server?", "Rendering web pages", ["Editing and updating content", "Routing and load balancing", "Database management"]),
    Question("What do you call the process of creating a component in Sitecore that displays a collection of data?", "Rendering", ["Routing", "Datasource", "Indexing"]),
    Question("Which of the following is not a type of Sitecore item?", "Solution", ["Template", "Layout", "Placeholder"]),
    Question("What does the abbreviation 'xDB' stand for in Sitecore?", "Experience Database", ["Extended Database", "XML Database", "XAML Database"]),
    Question("What does the abbreviation 'SPEAK' stand for in Sitecore?", "Sitecore Process Enablement & Accelerator Kit", ["Sitecore Personalization & Engagement Acceleration Kit", "Sitecore Programming Environment & Automation Kit", "Sitecore Presentation & Editing Accelerator Kit"]),
    Question("Which Sitecore tool allows you to test and personalize content for different users?", "Experience Editor", ["Content Editor", "Workbox", "Sitecore Rocks"]),
    Question("Which Sitecore tool is used to build custom interfaces for Sitecore users?", "SPEAK", ["Content Editor", "Experience Editor", "Workbox"]),
    Question("What is the primary purpose of the Sitecore Publishing Service?", "Improving publishing performance", ["Adding new publishing targets", "Customizing publishing restrictions", "Monitoring publishing status"]),
    Question("In Sitecore, what is the function of an index?", "Improving search performance", ["Storing content data", "Managing layout settings", "Assigning security roles"]),
    Question("Which of these is not a standard Sitecore search provider?", "Bing", ["Lucene", "Solr", "Azure Search"]),
    Question("What is the main function of the Sitecore Experience Accelerator (SXA)?", "Rapid website development", ["Performance monitoring", "User interface customization", "Mobile app development"]),
    Question("What do you call the Sitecore functionality that enables you to track user interactions and personalize their experience?", "xDB", ["SXA", "SPEAK", "Solr"]),
    Question("What is the role of Sitecore Cortex in the Sitecore Experience Platform?", "Machine learning", ["Content management", "Performance monitoring", "Website development"]),
    Question("Which of the following is not a part of Sitecore's Digital Marketing System (DMS)?", "Sitecore Rocks", ["Campaign Creator", "Engagement Automation", "Email Experience Manager"]),
    Question("In Sitecore, what is the function of a placeholder?", "Defining where components can be added", ["Storing content data", "Applying styling to components", "Creating reusable components"]),
    Question("What is the primary purpose of Sitecore's Content Testing feature?", "Optimizing content through A/B testing", ["Monitoring user interactions", "Customizing the user interface", "Managing content versions"]),
    Question("Which Sitecore module provides the ability to manage multiple websites within a single Sitecore instance?", "Multisite Management", ["Experience Accelerator", "Content Testing", "Email Experience Manager"]),
    Question("What is the main advantage of using Sitecore's Email Experience Manager (EXM)?", "Creating, sending, and tracking emails within Sitecore", ["Improved email design", "Support for multiple email clients", "Enhanced security"]),
    Question("What is the primary function of the Federated Experience Manager (FXM) in Sitecore?", "Integrating external websites with Sitecore's marketing features", ["Managing user roles and permissions", "Creating and managing digital campaigns", "Optimizing website performance"]),
    Question("What is the main use of Sitecore's Web Forms for Marketers (WFFM)?", "Creating forms for data collection", ["Building custom workflows", "Automating marketing tasks", "Designing web pages"]),
    Question("What does the abbreviation 'PaaS' stand for in the context of Sitecore?", "Platform as a Service", ["Program as a Service", "Page as a Service", "Process as a Service"]),
    Question("What do you call a series of tasks that an item can pass through in Sitecore?", "Workflow", ["Workbox", "Workpath", "Workline"]),
    Question("In Sitecore, which functionality allows for the tracking of all changes made to an item?", "Versioning", ["Indexing", "Archiving", "Caching"]),
    Question("Which of the following is not a standard part of the Sitecore client interface?", "Data Manager", ["Content Editor", "Experience Editor", "Desktop"]),
    Question("Which of the following is not a type of database in Sitecore?", "Relational Database", ["Master Database", "Web Database", "Core Database"]),
    Question("What is the primary purpose of the 'master' database in Sitecore?", "Storing all versions of all items", ["Rendering web pages", "Managing user roles", "Storing configuration data"]),
    Question("What is the main function of the 'web' database in Sitecore?", "Serving content to the live website", ["Storing all versions of all items", "Managing user roles", "Storing configuration data"]),
    Question("What is the primary function of the 'core' database in Sitecore?", "Storing configuration data", ["Serving content to the live website", "Storing all versions of all items", "Managing user roles"]),
    Question("In Sitecore, what is a 'bucket' used for?", "Storing large numbers of similar items", ["Categorizing content", "Managing user permissions", "Storing configuration data"]),
    Question("What is the main use of the 'Item' class in the Sitecore API?", "Representing a piece of content", ["Managing databases", "Rendering web pages", "Tracking user interactions"]),
    Question("Which of the following is not a type of cache in Sitecore?", "Image Cache", ["HTML Cache", "Data Cache", "Item Cache"]),
    Question("What does the abbreviation 'CDN' stand for in the context of Sitecore?", "Content Delivery Network", ["Content Development Network", "Custom Design Node", "Core Database Node"]),
    Question("Which of the following is not a common task performed using the Sitecore PowerShell Extensions (SPE)?", "Creating new users", ["Bulk updating items", "Generating reports", "Automating tasks"]),
    Question("What is the main function of Sitecore's Universal Tracker?", "Tracking user interactions across multiple channels", ["Improving search performance", "Managing multiple websites", "Automating marketing tasks"]),
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
    Question("Which layers should you not modify or add files to in Sitecore?", "Sitecore and Modules", ["Custom and Environment", "Sitecore and Custom", "Modules and Environment"]),
    Question("What is the default order of loading configuration files in Sitecore?", "Basic system files, Sitecore layer, Modules layer, Custom layer, Environment layer", ["Environment layer, Custom layer, Modules layer, Sitecore layer, Basic system files", "Modules layer, Sitecore layer, Basic system files, Custom layer, Environment layer", "Custom layer, Modules layer, Sitecore layer, Basic system files, Environment layer"]),
    Question("What is the role of the layers.config file in Sitecore?", "It defines the layers and the order in which they load at runtime", ["It defines user roles and permissions", "It manages the database connection", "It controls the website's appearance"]), Question("How can you control the sequence in which your patch files load in Sitecore?", "By adding a <loadOrder> setting to the layer", ["By renaming the files alphabetically", "By moving the files to a different folder", "By changing the file extension"]), Question("What change was made with Sitecore 9 in terms of configuration files loading?", "It introduced the ability to specify the order in which config files load", ["It introduced a new file format", "It removed the ability to load files in a specific order", "It automated the loading process"]), Question("What does a 'core role' mean in the context of Sitecore?", "It is an instance of the core Sitecore application with certain features enabled or disabled", ["It is a user role with full access to Sitecore features", "It is a basic Sitecore feature available in all versions", "It is a role assigned to the main Sitecore administrator"]), Question("How does personalization work in Sitecore?", "It displays targeted content to contacts based on their characteristics and behavior", ["It customizes the website's appearance", "It personalizes the user interface of the Sitecore application", "It allows users to personalize their accounts"]), Question("How do you set up personalization in Sitecore?", "By using the Rule Set Editor to add rules and actions to a specific component", ["By customizing the website's CSS", "By writing custom code in the backend", "By adjusting the website's settings in the control panel"]),
    Question("What is the function of the `layers.config` file in Sitecore?", "It defines the layers and the order in which they load at runtime", ["It stores user data", "It contains security settings", "It manages network configurations"]), Question("What is the purpose of Sitecore's Experience Platform (XP)?", "To create personalized experiences across all channels", ["To manage user permissions", "To improve website speed", "To build and deploy websites"]), Question("How does Sitecore's personalization feature work?", "It uses the Rule Set Editor to add rules and actions to a specific component, using these rules to display targeted, relevant content based on the characteristics and behavior of the contacts", ["It manually adjusts the website content for each user", "It changes the website layout based on user preferences", "It tracks user interactions across multiple channels"]), Question("What are the core roles in Sitecore?", "These are instances of the core Sitecore application with certain features enabled or disabled. In a fully scaled deployment, a dedicated instance performs each role", ["These are user roles with specific permissions", "These are the main modules of the Sitecore platform", "These are the main components of the Sitecore database"]), Question("What is the main benefit of using Sitecore as a CMS?", "It provides a comprehensive solution for managing content and customer experiences across multiple channels", ["It is the fastest CMS available", "It offers the best security features", "It supports the most programming languages"]), Question("What is a patch file in Sitecore?", "A file that is used to modify settings in the default Sitecore configuration", ["A file that contains security updates", "A file that is used to fix bugs in the system", "A file that is used to add new features to the system"]), Question("How can you control the sequence in which patch files load in Sitecore?", "By adding a <loadOrder> setting to the layer", ["By renaming the patch files", "By moving the patch files to a different folder", "By changing the file extensions"]), Question("In what order does Sitecore load files within a configuration layer?", "Sitecore loads the files in each subfolder in alphabetical order, with files in the root of a folder merging before files in subfolders within the folder", ["Sitecore loads the files in the order they were created", "Sitecore loads the files in reverse alphabetical order", "Sitecore loads the files randomly"]), Question("What is the main benefit of using xDB in Sitecore?", "It collects and connects customer data from multiple channels to provide a comprehensive view of each customer, enabling personalization and effective marketing", ["It speeds up the website load times", "It manages user permissions", "It secures customer data"]), Question("What does xConnect do in Sitecore?", "It serves as an intermediary between your application and xConnect, allowing you to read, write, and search for contacts and interactions", ["It manages the website themes", "It improves website load times", "It secures customer data"]),
            # Add more questions here...
        ]

        random.shuffle(self.questions)  # Shuffle the questions randomly

        self.current_question = 0
        self.score = 0
        self.top_score = self.load_top_score()  # Load the top score from the file

        self.question_label = tk.Label(master, text="", wraplength=380, anchor="w", padx=10, pady=10)
        self.answer_buttons = []
        self.next_button = None
        self.score_label = tk.Label(master, text="Score: 0 / 0", padx=10, pady=10, anchor="w")
        self.top_score_label = tk.Label(master, text=f"Top Score: {self.top_score}%", padx=10, pady=10, anchor="w")

        self.question_label.pack()
        self.score_label.pack(anchor="w")
        self.top_score_label.pack(anchor="w")

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

        if percentage > self.top_score:
            self.top_score = percentage
            self.save_top_score()

        self.show_restart_prompt()

    def save_top_score(self):
        with open("top_score.txt", "w") as file:
            file.write(str(int(self.top_score)))

    def load_top_score(self):
        try:
            with open("top_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

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

    def quit_quiz(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit the quiz?"):
            self.master.quit()


root = tk.Tk()
quiz = Quiz(root)
root.mainloop()
