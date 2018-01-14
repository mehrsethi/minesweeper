"""
The main program - makes the main frame for the game
"""


from tkinter import *
from Application import Application

# function: main
# description: runs the main program
# input: none
# output: none
def main():

    root = Tk()
    root.title("Minesweeper")
    app = Application(root)

    root.mainloop()


main()