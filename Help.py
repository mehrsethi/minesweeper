"""
Reads the instructions for Minesweeper from a text file, and writes them to a text box
"""

from tkinter import *

class Help(Frame):
    def __init__(self, rootWindow):
        super().__init__(rootWindow)
        self.grid()

        # create the text box
        self.textInfo = Text(self)
        self.textInfo.grid(row=0, column=0)

        # add a vertical scrollbar
        self.scrollbar = Scrollbar(self, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="N" + "S")

        # configure the scrollbar to the textbox
        self.textInfo.config(yscrollcommand=self.scrollbar.set, width=85, height=25, bg="black", fg="#00ffff")
        self.scrollbar.config(command=self.textInfo.yview)

        # call the insertInfo method
        self.insertInfo()


    def insertInfo(self):
        listInfo = [] # empty list for the file
        # open the file for reading
        fileIn = open("help.txt", "r")
        # add each stripped line to the list
        for line in fileIn:
            line = line.strip()
            listInfo.append(line)
        # insert each item of listInfo to the top of the textbox in the reverse order
        for index in range(len(listInfo)-1, -1, -1):
            self.textInfo.insert(0.0, listInfo[index] + "\n")
        fileIn.close()
