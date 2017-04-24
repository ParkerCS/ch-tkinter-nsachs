# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification, whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)

#I changed the font of the title, size of the title, and style of the title.  I also added a border to the "Your Question Here" label

from tkinter import *
import random
from tkinter import font

class Magic():
    def __init__(self, master):

        #declare variables
        self.question = DoubleVar()
        self.question.set("")
        self.answer = DoubleVar()
        self.answer.set("Your Fortune Here")

        self.answer_options = ["It is certain", "Without a doubt", "As I see it, yes", "Most likely", "Better not to tell you now", "Don't count on it", "Outlook not so good", "Very doubtful", "My reply is no", "I don't think so"]

        #Title
        self.title_font = font.Font(family = "Courier New", size = 30, weight = font.BOLD)
        self.title = Label(master, text = "Magic 8-Ball", font = self.title_font)
        self.title.grid(row = 1, column = 1, columnspan = 2)

        #Description
        self.description = Label(master, text = "In the box below, please enter a 'yes' or 'no' question to discover your future!")
        self.description.grid(row = 2, column = 1, columnspan = 3)

        #Question label and entry widget
        self.question_label = Label(master, text = "Your Question Here:", relief = RAISED)
        self.question_label.grid(row = 3, column = 1)

        self.question_entry = Entry(master, textvariable = self.question)
        self.question_entry.grid(row = 4, column = 1)

        #Answer button and result
        self.answer_button = Button(master, text = "Show Me!", command = lambda: self.button_click())
        self.answer_button.grid(row = 3, column = 2)

        self.answer_label = Label(master, textvariable = self.answer)
        self.answer_label.grid(row = 4, column = 2)

    def button_click(self):
        self.answer.set(self.answer_options[random.randrange(len(self.answer_options))])


if __name__ == "__main__":
    root = Tk()
    root.title("Magic 8-Ball App")
    my_app = Magic(root)
    root.mainloop()