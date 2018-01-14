"""
Prompted when there are multiple users with the same name, it displays all these players, including their minimum times and total number of games played
It asks the user to pick one of the players and updates their stats according to the game won
"""


from tkinter import *
from tkinter import messagebox

class MultipleUsers(Frame):
    def __init__(self, root, playerList):
        super().__init__(root)
        self.grid()

        self.root = root

        self.clashList = playerList # list of all the players with the same name
        self.user = playerList[0] # set the first player in the list as default

        # label with heading
        self.labelHeading = Label(self, text="There are multiple players with that name!")
        self.labelHeading.grid()

        # list box to display the names
        self.listNames = Listbox(self, width=80, height=len(self.clashList)+1)
        for k in range(len(self.clashList)):
            self.listNames.insert(len(self.clashList), str(k+1) + ". " + self.clashList[k].getName() + " - " + str(self.clashList[k].getMinTime()) + " - " + str(self.clashList[k].getNumGames()) + "\n")
        self.listNames.insert(0, "Name  -   Minimum Time  -  Number of Games Won")
        self.listNames.grid()

        # submit button calls the submit method
        self.buttonSubmit = Button(self, text="Submit", command=self.submit)
        self.buttonSubmit.grid()

    # submit method sets self.user equal to the player object at the index returned by the listbox in clashList
    def submit(self):
        if self.listNames.curselection()[0] != 0:
            self.user = self.clashList[self.listNames.curselection()[0]-1]
            # exits the Multiple Users loop and closes the window
            self.quit()
            self.root.destroy()
        # if the user chooses the heading row, display an error
        else:
            messagebox.showerror("INVALID SELECTION", "Please make a valid selection from 1-" + str(len(self.clashList)))

    # returns the Player object the user selected
    def getUser(self):
        return self.user