# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.


from tkinter import *
from tkinter import font


# I underlined my title, changed the font and size, and added color and borders to my labels.
class Gravity():
    def __init__(self,master):

        #declare variables
        self.m1 = DoubleVar()
        self.m2 = DoubleVar()
        self.r = DoubleVar()
        self.calculate = DoubleVar()
        self.calculate.set(0.0)

        #Title
        self.title_font = font.Font(family="Times New Roman", size = 30, weight = font.NORMAL, underline = 2)
        self.title = Label(master, text="Force of Gravity Calculator", font = self.title_font)
        self.title.grid(row=1, column=1, columnspan = 2)

        #Description
        self.description = Label(master, text = "In the boxes below, please enter the mass of the first and second object and the distance between the centers of the two objects.")
        self.description.grid(row = 2, column = 1, columnspan = 2)

        #Entry labels and entry widget
        self.m1_label = Label(master, text = "First Object Mass (kg) =", bg = "green", relief = RIDGE)
        self.m1_label.grid(row = 3, column = 1)
        self.m1_entry = Entry(master, textvariable = self.m1)
        self.m1_entry.grid(row = 3, column = 2)

        self.m2_label = Label(master, text="Second Object Mass (kg) =", bg = "green", relief = RIDGE)
        self.m2_label.grid(row = 4, column = 1)
        self.m2_entry = Entry(master, textvariable = self.m2)
        self.m2_entry.grid(row = 4, column = 2)

        self.r_label = Label(master, text="Distance (m) =", bg = "green", relief = RIDGE)
        self.r_label.grid(row = 5, column = 1)
        self.r_entry = Entry(master, textvariable = self.r)
        self.r_entry.grid(row = 5, column = 2)

        #Calculator button and result
        self.calculate_button = Button(master, text = "CALCULATE FORCE (N)", command = lambda: self.button_click())
        self.calculate_button.grid(row = 6, column = 1)
        self.calculate_label = Label(master, textvariable = self.calculate, bg = "black", fg = "white", relief = RIDGE)
        self.calculate_label.grid(row = 6, column = 2)

    def button_click(self):
        try:
            self.calculate.set((6.67 * (10 ** -11)) * (self.m1.get() * self.m2.get())/ (self.r.get() ** 2))
        except:
            self.calculate.set("Error")



#Add exceptions if ZeroDivisionError, self.calculate.set("Error (distance cannot be zero)")

if __name__ == "__main__":
    root = Tk()
    root.title("Gravity Calculator App")
    my_app = Gravity(root)
    root.mainloop()

