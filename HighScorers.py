"""
Displays to the user all the players who have played the game in order of their ranking, going from the person
who took the least time to the person who took the most
The screen is divided into High Scorers for Easy, Intermediate and Hard levels
"""


from tkinter import *
import pickle


class HighScorers(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()

        # screen heading label
        self.labelHeading = Label(self, text="HIGH SCORERS", font="Times 18 bold")
        self.labelHeading.grid(row=0, column=2)

        # heading label for each column
        self.labelEasy = Label(self, text="EASY", font="Times 14 bold")
        self.labelEasy.grid(row=1, column=0)

        self.labelInter = Label(self, text="INTERMEDIATE", font="Times 14 bold")
        self.labelInter.grid(row=1, column=2)

        self.labelHard = Label(self, text="HARD", font="Times 14 bold")
        self.labelHard.grid(row=1, column=4)

        # vertical scrollbar for each column, implemented in the adjacent right column
        self.scrollbarEasy = Scrollbar(self, orient="vertical")
        self.scrollbarEasy.grid(row=2, column=1, sticky="N" + "S")

        self.scrollbarInter = Scrollbar(self, orient="vertical")
        self.scrollbarInter.grid(row=2, column=3, sticky="N" + "S")

        self.scrollbarHard = Scrollbar(self, orient="vertical")
        self.scrollbarHard.grid(row=2, column=5, sticky="N" + "S")

        # text boxes for each column to display the high scorers
        self.textEasy = Text(self, height=15, width=35)
        self.textEasy.grid(row=2, column=0)

        self.textInter = Text(self, height=15, width=35)
        self.textInter.grid(row=2, column=2)

        self.textHard = Text(self, height=15, width=35)
        self.textHard.grid(row=2, column=4)

        # configuring each scrollbar to its respective textbox
        self.textEasy.config(yscrollcommand=self.scrollbarEasy.set)
        self.scrollbarEasy.config(command=self.textEasy.yview)

        self.textInter.config(yscrollcommand=self.scrollbarInter.set)
        self.scrollbarInter.config(command=self.textInter.yview)

        self.textHard.config(yscrollcommand=self.scrollbarHard.set)
        self.scrollbarHard.config(command=self.textHard.yview)

        # call the readFile method
        self.readFile()

    # the readFile method reads the binary files for Easy, Intermediate and Hard level players
    # and inserts their names and minimum times in order of ranking into the respective textboxes
    def readFile(self):
        # empty lists created to read respective files
        playerListEasy = []
        playerListInter = []
        playerListHard = []

        # each of the three files is read in a separate try/except block because when the game starts
        # there may not be any players in one or more of these files, i.e. these files do not exist
        try:
            fileIn = open("High Scorers - Easy.bin", "rb")
            playerListEasy = pickle.load(fileIn)
            fileIn.close()
        except:
            playerListEasy = []

        try:
            fileIn = open("High Scorers - Intermediate.bin", "rb")
            playerListInter = pickle.load(fileIn)
            fileIn.close()
        except:
            playerListInter = []

        try:
            fileIn = open("High Scorers - Hard.bin", "rb")
            playerListHard = pickle.load(fileIn)
            fileIn.close()
        except:
            playerListHard = []

        # make lists of the lists of players for each level, the titles to be inserted, and the three textboxes in which to dispaly the information
        playerList = [playerListEasy, playerListInter, playerListHard]
        textList = [self.textEasy, self.textInter, self.textHard]

        # iterate through each of the three playerList's
        for i in range(len(playerList)):
            # append the minimum time taken by each item (which is a Player object) to a temporary list called highScorerList
            highScorerList = []
            for player in playerList[i]:
                highScorerList.append(player.getMinTime())

            # find the lowest time, insert it to the respective textbox, and remove that time from playerList
            # repeat the process till the highScorerList is empty
            for k in range(len(highScorerList)):
                minScore = min(highScorerList)
                index = highScorerList.index(minScore)
                textList[i].insert(float(k+1), playerList[i][index].getName() + " - " + str(playerList[i][index].getMinTime()) + "\n")
                textList[i].config(font="Times 14")
                # the name and minimum time is inserted in the textbox at the row determined by the iteration number of the for loop (k), after converting it to a float
                # this means the 7th high scorer (determined at the 7th iteration of the loop), will be inserted at 7.0 [7th row, 1st column]
                del highScorerList[index]
                del playerList[i][index]
            # change the state of the textbox to disabled to prevent the user from editing the information
            textList[i].config(state="disabled")