"""
Prompts the user to enter their name if they win a game
Adds the input to the list of players (based on level)
Displays the top five high scorers for the level the last game was played at

Also gives the user the option to view all high scorers from each level (by using the HighScorers class)
"""


from tkinter import *
from tkinter import messagebox
import pickle
from Player import Player
from HighScorers import HighScorers
from MultipleUsers import MultipleUsers


class Prompt(Frame):
    def __init__(self, root, minTime, mines, rows, columns):
        super().__init__(root)
        self.grid()

        self.minTime = minTime # time taken by the player to win the game
        # number of mines, rows and columns in the game, to calculate the level at which the user was playing
        self.mines = mines
        self.rows = rows
        self.columns = columns

        # label and entry field to input the name of the player
        self.labelName = Label(self, text="Enter your name", font="Times 14 bold")
        self.labelName.grid(row=0, column=0)

        self.entryName = Entry(self)
        self.entryName.grid(row=0, column=1)
        self.entryName.config(font="Times 14 bold")

        # submit button calls the submit method
        self.buttonSubmit = Button(self, text="Submit", command=self.submit, font="Times 14 bold")
        self.buttonSubmit.grid(row=0, column=2)

        # text box to display the list of high scorers
        self.textNames = Text(self, height=10, width=75)
        self.textNames.grid(row=1, column=0, columnspan=4)
        self.textNames.config(font="Times 14")

        # all button calls the allHighScorers method
        self.buttonAll = Button(self, text="View all high scorers", command=self.allHighScorers, font="Times 14 bold")
        self.buttonAll.grid(row=0, column=3)

    # displays the messagebox asking if the player already exists in the system, or if it's a new player
    def promptExistingUser(self):
        answer = messagebox.askyesno(message="Are you an existing user?")
        return answer

    # disables the submit button and the entry field, so that once the user inputs a name, he or she cannot make any changes
    def submit(self):
        self.buttonSubmit.config(state="disabled")
        self.entryName.config(state="disabled")
        self.writeFile()

    # reads the file for the required level, adds the users stats to it, and inserts the top five names in the textbox
    def writeFile(self):
        name = self.entryName.get()
        playerList = []
        title = ""
        # if the binary file containing Player objects exists, open it and store the data in a list (do this for each level)
        try:
            if self.mines == 10:
                fileIn = open("High Scorers - Easy.bin", "rb")
                playerList = pickle.load(fileIn)
                fileIn.close()
            elif self.mines == 20:
                fileIn = open("High Scorers - Intermediate.bin", "rb")
                playerList = pickle.load(fileIn)
                fileIn.close()
            elif self.mines == 50:
                fileIn = open("High Scorers - Hard.bin", "rb")
                playerList = pickle.load(fileIn)
                fileIn.close()
        except:
            pass

        # call self.promptExistingUser()
        ans = self.promptExistingUser()
        # check if the answer is yes (he or she is an existing user) or not
        if ans:
            # make an empty list
            personList = []
            # append every person with the name the user entered to the previously created list
            for person in playerList:
                if person.getName() == name:
                    personList.append(person)
            # if there is only one person in the list, update his or her minimum time and total number of games
            if len(personList) == 1:
                personList[0].setMinTime(self.minTime)
                personList[0].setNumGames()
            # if there is more than one player in the list, make a MultipleUsers window
            elif len(personList) > 1:
                root2 = Tk()
                root2.title("      ")
                multi = MultipleUsers(root2, personList)
                root2.mainloop()
                person = multi.getUser()
                person.setMinTime(self.minTime)
                person.setNumGames()
            # if there is no person in the list (i.e. the user entered yes in error), display a message box displaying the error
            # create a Player object with the player's name, update his or her minimum time and total number of games, and append the object to playerList
            elif len(personList) == 0:
                messagebox._show(message="Oops! Looks like you aren't an existing player.\nDon't worry, we added you to our system.")
                person = Player(name)
                person.setMinTime(self.minTime)
                person.setNumGames()
                playerList.append(person)
        # if the person selected no, create a Player object with the player's name, update his or her minimum time and total number of games, and append the object to playerList
        else:
            person = Player(name)
            person.setMinTime(self.minTime)
            person.setNumGames()
            playerList.append(person)

        # for the Easy level
        if self.mines == 10 and self.rows == 10 and self.columns == 10:
            # open the respective binary file
            fileOut = open("High Scorers - Easy.bin", "wb")
            # make a title variable to be inserted in the beginning of the respective text box
            title = "\nHigh Scorers - Easy\n\n"
            # dump playerList into the file
            pickle.dump(playerList, fileOut)
            fileOut.close()
        # for the Intermediate level
        elif self.mines == 20 and self.rows == 10 and self.columns == 20:
            # open the respective binary file
            fileOut = open("High Scorers - Intermediate.bin", "wb")
            # make a title variable to be inserted in the beginning of the respective text box
            title = "\nHigh Scorers - Intermediate\n\n"
            # dump playerList into the file
            pickle.dump(playerList, fileOut)
            fileOut.close()
        # for the Hard level
        elif self.mines == 50  and self.rows == 25 and self.columns == 20:
            # open the respective binary file
            fileOut = open("High Scorers - Hard.bin", "wb")
            # make a title variable to be inserted in the beginning of the respective text box
            title = "\nHigh Scorers - Hard\n\n"
            # dump playerList into the file
            pickle.dump(playerList, fileOut)
            fileOut.close()

        # create an empty list
        highScorerList = []
        # for every player in playerLIst, append his or her minimum time to the previously created list
        for player in playerList:
            highScorerList.append(player.getMinTime())

        # if the length of the list is less than 5, set a variable called length equal to the length of the list
        if len(playerList) < 5:
            length = len(playerList)
        # otherwise, set it to 5
        else:
            length = 5
        # run the following loop length number of time
        for i in range(length):
            # find the minimum in highScorersList
            minScore = min(highScorerList)
            # find the index of the minimum in highScorersList
            ind = highScorerList.index(minScore)
            # insert the name and minimum time of player at index ind in playerList in textNames
            # insert it at the row determined by the iteration number, so the lowest time get inserted at 1.0, the next at 2.0 and so on
            self.textNames.insert(float(length), playerList[ind].getName() + " - " + str(playerList[ind].getMinTime()) + "\n")
            # delete the time from highScorersList and the Player object from playerList
            del highScorerList[ind]
            del playerList[ind]
        # insert the title in the first row of textNames
        self.textNames.insert(0.0, title)
        self.textNames.config(state="disabled")

    # allHighScorers method makes a HighScorers window
    def allHighScorers(self):
        root = Tk()
        root.title("      ")
        scorers = HighScorers(root)