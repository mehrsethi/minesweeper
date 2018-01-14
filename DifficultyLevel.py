"""
Displays to the user the various difficulty levels that he/she can choose from - stores the input, which the
Application class then uses to generate a board with the right number of rows and columns
"""


from tkinter import *
from tkinter import messagebox

class DifficultyLevel(Frame):
    def __init__(self, root, app):
        super().__init__(root, app)
        self.grid()

        self.root = root

        self.app = app # reference to the Application class, to have access to its variables and methods

        self.m = 0 # number of mines
        self.r = 0 # number of rows
        self.c = 0 # number of columns

        # the string variable, with default value set as "e" (easy)
        self.varLevel = StringVar(value="e")

        # the four radiobuttons displaying options - Easy, Intermediate, Hard and Custom
        self.radioButtonEasy = Radiobutton(self, text="Easy", value="e", variable=self.varLevel, command=self.buttonSettingsEasy)
        self.radioButtonEasy.grid(row=0, column=0)

        self.radioButtonInter = Radiobutton(self, text="Intermediate", value="i", variable=self.varLevel, command=self.buttonSettingsInter)
        self.radioButtonInter.grid(row=0, column=1)

        self.radioButtonHard = Radiobutton(self, text="Hard", value="h", variable=self.varLevel, command=self.buttonSettingsHard)
        self.radioButtonHard.grid(row=0, column=2)

        self.radioButtonCustom = Radiobutton(self, text="Custom", value="c", variable=self.varLevel, command=self.buttonSettingsCustom)
        self.radioButtonCustom.grid(row=1, column=1)


        # the three entry fields for entering the number of mines, rows and columns if the "custom" option is selected
        # all three are disabled until the "custom" option is selected
        self.entryMines = Entry(self, state="disabled")
        self.entryMines.grid(row=2, column=0)

        self.entryRows = Entry(self, state="disabled")
        self.entryRows.grid(row=2, column=1)

        self.entryColumns = Entry(self, state="disabled")
        self.entryColumns.grid(row=2, column=2)

        # corresponding labels for the entry fields
        self.labelMines = Label(self, text="Mines")
        self.labelMines.grid(row=3, column=0)

        self.labelRows = Label(self, text="Rows")
        self.labelRows.grid(row=3, column=1)

        self.labelColumns = Label(self, text="Columns")
        self.labelColumns.grid(row=3, column=2)


        # submit button to call the readButton method which sets the values for self.m, self.r and self.c
        self.buttonSubmit = Button(self, text="Submit", command=self.readButton)
        self.buttonSubmit.grid(row=4, column=1)


    # sets the varLevel variable as "e" [the radiobuttons don't automatically update the value of the string variable on Macs]
    # if the custom option is selected and then deselected, disables the entry fields for entering the number of mines, rows and columns
    def buttonSettingsEasy(self):
        self.varLevel.set("e")
        self.entryMines.config(state="disabled")
        self.entryRows.config(state="disabled")
        self.entryColumns.config(state="disabled")

    # sets the varLevel variable as "i" [the radiobuttons don't automatically update the value of the string variable on Macs]
    # if the custom option is selected and then deselected, disables the entry fields for entering the number of mines, rows and columns
    def buttonSettingsInter(self):
        self.varLevel.set("i")
        self.entryMines.config(state="disabled")
        self.entryRows.config(state="disabled")
        self.entryColumns.config(state="disabled")

    # sets the varLevel variable as "h" [the radiobuttons don't automatically update the value of the string variable on Macs]
    # if the custom option is selected and then deselected, disables the entry fields for entering the number of mines, rows and columns
    def buttonSettingsHard(self):
        self.varLevel.set("h")
        self.entryMines.config(state="disabled")
        self.entryRows.config(state="disabled")
        self.entryColumns.config(state="disabled")

    # sets the varLevel variable as "c"
    # enables the text boxes for entering the number of mines, rows and columns
    def buttonSettingsCustom(self):
        self.varLevel.set("c")
        self.entryMines.config(state="normal")
        self.entryRows.config(state="normal")
        self.entryColumns.config(state="normal")


    # gets the button value and correspondingly sets the values for the number of mines, rows and columns
    def readButton(self):
        value = self.varLevel.get()
        if value != "c":
            if value == "e":
                self.m = 10
                self.r = 10
                self.c = 10
            elif value == "i":
                self.m = 20
                self.r = 10
                self.c = 20
            elif value == "h":
                self.m = 50
                self.r = 25
                self.c = 20
            # sets the flagNumber, mines, rows and column variables of Application class to the new number of flags, mines, rows and columns determined by the user
            self.app.flagNumber = int(self.m)
            self.app.mines = int(self.m)
            self.app.rows = int(self.r)
            self.app.columns = int(self.c)
            # calls the reload method of Application
            self.app.reload()
            # closes the Choose Difficulty Level window
            self.root.destroy()
        else:
            self.m = self.entryMines.get()
            self.r = self.entryRows.get()
            self.c = self.entryColumns.get()
            # error checking to make sure that the number of mines, rows and columns are numbers
            if self.m.isnumeric() != True or self.r.isnumeric() != True or self.c.isnumeric() != True:
                messagebox.showerror("ERROR", "You must enter only numbers! Try again!")
            else:
                # error checking to make sure that the number of rows and columns are within a specified range
                # and the number of mines is not more than the total number of boxes on the board
                if int(self.r) not in range(1, 26) or int(self.c) not in range(1, 21) or (int(self.m) not in range(1, (int(self.r)*int(self.c)+1))):
                    if int(self.r) not in range(1, 26):
                        messagebox.showerror("ERROR", "The number of rows must be between 1 and 25! Try again!")
                    elif int(self.c) not in range(1, 21):
                        messagebox.showerror("ERROR", "The number of columns must be between 1 and 20! Try again!")
                    elif int(self.m) < 1:
                        messagebox.showerror("ERROR", "The number of mines must be more than 1! Try again!")
                    elif int(self.m) > int(self.r)*int(self.c):
                        messagebox.showerror("ERROR", "The number of mines must be less than the number of total boxes! Try again!")
                else:
                    # sets the flagNumber, mines, rows and column variables of Application class to the new number of
                    # flags, mines, rows and columns determined by the user
                    self.app.flagNumber = int(self.m)
                    self.app.mines = int(self.m)
                    self.app.rows = int(self.r)
                    self.app.columns = int(self.c)
                    # calls the reload method of Application
                    self.app.reload()
                    # closes the Choose Difficulty Level window
                    self.root.destroy()