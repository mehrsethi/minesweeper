"""
Application class creates the tkinter window that contains the actual game. It display to the user a certain number of
buttons based on the level as determined by the DifficultyLevel class (the default is the easy level with a 10x10 grid).
When the user clicks a button the changeText method is called, which displays the value of the button to the user and
opens the surrounding buttons (by calling changeText on them) if the value of the button clicked by the user is zero.

On winning the game, the Prompt class is instantiated, and that part of the program is executed.

The Application class also displays a menubar with options for changing the difficulty level, the device, viewing the
scoreboard, starting a new game, exiting the application or viewing the instruction on how to play the game.
Clicking any of these options calls their respective methods which execute the respective parts of the program.

On the top left corner of the screen is a timer that counts the number of seconds it takes for the player to win a game.
This is linked to the Stopwatch class.

Right clicking on any button changes its display to a flag, right clicking twice changes it to a question mark. There is
a flag counter on the top right corner of the screen which displays the total number of mines remaining to be found.
"""


from tkinter import *
from tkinter import messagebox
from Box import Box
from Board import generateBoard
from Stopwatch import Stopwatch
from DifficultyLevel import DifficultyLevel
from Device import Device
from Help import Help
from Prompt import Prompt
from HighScorers import HighScorers



class Application(Frame):
    def __init__(self, rootWindow):
        super().__init__(rootWindow)
        self.grid()

        self.rootWindow = rootWindow

        # set the defaults for the number of flags/mines, rows and columns
        self.flagNumber = 10
        self.mines = 10
        self.rows = 10
        self.columns = 10

        # make the device variable
        self.device = ""

        # call the generateBoard function, and instantiate the Stopwatch class
        self.boardList = generateBoard(self.mines, self.rows, self.columns)
        self.stopwatch = Stopwatch()

        # open the files for different images to be displayed, and store them in separate variables
        self.smile = PhotoImage(file="Smile.gif")
        self.dead = PhotoImage(file="Dead.gif")
        self.glasses = PhotoImage(file="Glasses.gif")
        self.one = PhotoImage(file="One.gif")
        self.two = PhotoImage(file="Two.gif")
        self.three = PhotoImage(file="Three.gif")
        self.four = PhotoImage(file="Four.gif")
        self.five = PhotoImage(file="Five.gif")
        self.six = PhotoImage(file="Six.gif")
        self.seven = PhotoImage(file="Seven.gif")
        self.eight = PhotoImage(file="Eight.gif")
        self.mine = PhotoImage(file="Mines.gif")
        self.blank = PhotoImage(file="Blank.gif")
        self.flag = PhotoImage(file="Flag.gif")
        self.revealMine = PhotoImage(file="Mine.gif")
        self.question = PhotoImage(file="Question.gif")

        # add a vertical Scrollbar
        self.scrollbar = Scrollbar(self.rootWindow, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="N" + "S")

        # make a Canvas widget and based on the number of mines, set the srollregion
        if self.mines == 10:
            self.canvas = Canvas(self, scrollregion=(0, 0, 350, 350), width=350, height=380)
        elif self.mines == 20:
            self.canvas = Canvas(self, scrollregion=(0, 0, 700, 350), width=700, height=380)
        elif self.mines == 50:
            self.canvas = Canvas(self, scrollregion=(0, 0, 700, 910), width=700, height=680)
        else:
            height = (self.rows + 1) * 35
            if self.rows >= 18:
                height = 680
            self.canvas = Canvas(self, scrollregion=(0, 0, self.columns*35, (self.rows+1)*35), width=self.columns*35, height=height)
        self.canvas.grid(row=0, column=0)
        # configure the Scrollbar to the Canvas
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.yview)

        # make an empty dictionary to store all the minesweeper buttons
        self.buttonDict = {}
        # create and grid buttons based on the number of rows and columns
        # also bind the buttons to the changeText method
        # based on whether the player is using a pc or mac, bind the right click to the setFlag method
        # add the button to buttonDict
        for x in range(1, int(self.columns)+1):
            for y in range(1, int(self.rows)+1):
                self.buttonTemplate = Box(self, image=self.blank, state="normal", command=lambda xc=x, yc=y:self.changeText(xc, yc))
                self.buttonTemplate_window = self.canvas.create_window((x*35)-20, (y*35)+20, window=self.buttonTemplate)
                self.buttonTemplate.bind("<Button-2>", lambda event, xc=x, yc=y: self.setFlag(event, xcoord=xc, ycoord=yc))
                self.buttonDict[str(x) + "," + str(y)] = self.buttonTemplate

        # add a rest button and grid it to the center of the first row
        self.buttonReset = Button(self, image=self.smile, command=self.resetBoard, height=25, width=25)
        self.buttonReset_window = self.canvas.create_window(self.columns*17.3, 20, window=self.buttonReset)

        # add a timer label to the top left corner of the screen
        self.labelTimer = Label(self, text="0", bg="black", fg="red", font="Digital-7 25 bold", width=2, height=1)
        self.labelTimer_window = self.canvas.create_window(50, 20, window=self.labelTimer)

        # add a flag number label to the top right corner of the screen
        self.labelFlag = Label(self, text=self.flagNumber, bg="black", fg="red", font="Digital-7 25 bold", width=2, height=1)
        self.labelFlag_window = self.canvas.create_window((self.columns*35)-55, 20, window=self.labelFlag)

        # add a menubar
        self.menubar = Menu(self.rootWindow)

        # add the commands for the Settings menu
        self.menuSettings = Menu(self.menubar)
        self.menuSettings.add_command(label="New Game", command=self.resetBoard)
        self.menuSettings.add_separator()
        self.menuSettings.add_command(label="Difficulty Level", command=self.setLevel)
        self.menuSettings.add_command(label="Device", command=self.setDevices)
        self.menuSettings.add_command(label="Scoreboard", command=self.allHighScorers)
        self.menuSettings.add_separator()
        self.menuSettings.add_command(label="Exit", command=self.quit)

        self.menubar.add_cascade(label="Settings", menu=self.menuSettings)

        # add the Help menu with command
        self.menuHelp = Menu(self.menubar)
        self.menubar.add_cascade(label="Help", menu=self.menuHelp)
        self.menuHelp.add_command(label="Instructions", command=self.help)

        #configure menubar to the root
        self.rootWindow.config(menu=self.menubar)


    # instantiates the Help class
    def help(self):
        helpRoot = Tk()
        helpRoot.title("HELP")
        helpApp = Help(helpRoot)

    # instantiates the DifficultyLevel class
    def setLevel(self):
        level = Tk()
        level.title("Choose Difficulty Level")
        difficulty = DifficultyLevel(level, self)

    # instantiates the Device class
    def setDevices(self):
        deviceRoot = Tk()
        deviceRoot.title("Choose a Device")
        deviceApp = Device(deviceRoot, self)

    # allHighScorers method makes a HighScorers window
    def allHighScorers(self):
        root = Tk()
        root.title("      ")
        scorers = HighScorers(root)

    # returns the run time from the stopwatch
    def findMinTime(self):
        return self.stopwatch.getTime()

    # updates the time label every second
    def updateTime(self):
        self.labelTimer.config(text=str(int(self.stopwatch.getTime())))
        if self.stopwatch.on:
            self.after(100, self.updateTime)

    # changes the display for the flag label with the current flag number
    def updateFlagNumber(self):
        self.labelFlag.config(text=self.flagNumber)


    # changes the display image of the button when it is right clicked to a flag if it's blank, to a question mark if
    # it's flag, and to blank if it's a question mark
    def setFlag(self, event, xcoord, ycoord):
        if self.buttonDict[str(xcoord) + "," + str(ycoord)].getImage() == self.flag:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(image=self.question)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.question)
            self.flagNumber += 1
        elif self.buttonDict[str(xcoord) + "," + str(ycoord)].getImage() == self.blank and self.buttonDict[str(xcoord) + "," + str(ycoord)].cget("state") != "disabled":
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(image=self.flag)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.flag)
            self.flagNumber -= 1
        elif self.buttonDict[str(xcoord) + "," + str(ycoord)].getImage() == self.question:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(image=self.blank)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.blank)
        # updates the flag label
        self.updateFlagNumber()
        # calls the checkWinner method
        self.checkWinner(xcoord,ycoord)


    # called when any button is clicked
    def changeText(self, xcoord, ycoord):
        # if the image on the button is a flag, make it blank, and update the flagNumber variable and label
        if self.buttonDict[str(xcoord) + "," + str(ycoord)].getImage() == self.flag:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(image=self.blank)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.blank)
            self.flagNumber += 1
            self.updateFlagNumber()
        # start the stopwatch
        self.stopwatch.start()
        # call updateTime
        self.updateTime()
        # changes the image of the button based on its value
        if self.boardList[ycoord - 1][xcoord - 1] == 1:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.one)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.one)
        elif self.boardList[ycoord - 1][xcoord - 1] == 2:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.two)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.two)
        elif self.boardList[ycoord - 1][xcoord - 1] == 3:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.three)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.three)
        elif self.boardList[ycoord - 1][xcoord - 1] == 4:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.four)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.four)
        elif self.boardList[ycoord - 1][xcoord - 1] == 5:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.five)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.five)
        elif self.boardList[ycoord - 1][xcoord - 1] == 6:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.six)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.six)
        elif self.boardList[ycoord - 1][xcoord - 1] == 7:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.seven)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.seven)
        elif self.boardList[ycoord - 1][xcoord - 1] == 8:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.eight)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.eight)
        elif self.boardList[ycoord - 1][xcoord - 1] == "m":
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.mine)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.mine)
        elif self.boardList[ycoord - 1][xcoord - 1] == 0:
            self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="disabled", image=self.blank)
            self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.blank)
        # calls the checkWinner method
        self.checkWinner(xcoord, ycoord)
        # call changeText on all the surrounding buttons if the button clicked has value 0
        if self.boardList[ycoord-1][xcoord-1] == 0 and xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
            self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            xcoord += 1
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            ycoord += 1
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            ycoord -= 2
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            xcoord -= 2
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            xcoord += 1
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            ycoord+= 2
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            xcoord -= 1
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()
            ycoord -= 1
            if xcoord in range(1,int(self.columns)+1) and ycoord in range(1,int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].invoke()

    # called after every click to make sure that the game is not over
    def checkWinner(self, xcoord, ycoord):
        # if the user clicks a mine, change the reset button image and end the game
        if self.buttonDict[str(xcoord)+","+str(ycoord)].cget("state") == "disabled" and self.boardList[ycoord-1][xcoord-1] == "m":
            self.buttonReset.config(image=self.dead)
            # disable all the buttons
            for x in range(1, int(self.columns)+1):
                for y in range(1, int(self.rows)+1):
                    if self.boardList[y-1][x-1] == "m" and self.buttonDict[str(x) + "," + str(y)].getImage() != self.mine:
                        self.buttonDict[str(x) + "," + str(y)].config(image=self.revealMine)
                    self.buttonDict[str(x)+","+str(y)].config(state="disabled")
            # stop the stopwatch
            self.stopwatch.stop()
            # show a messagebox
            messagebox.showinfo("LOSER", "Sorry! You lost!")
        else:
            # make an empty list
            checkerList = []
            # for each button in buttonDict, if the state is normal, add it to checkerList
            for item in self.buttonDict:
                if self.buttonDict[item].cget("state") == "normal":
                    checkerList.append(item)
            # check if length of the checkerList is equal to the number of mines, i.e. the only non-disabled buttons are all mines
            if len(checkerList) == self.mines:
                # change the image for the reset button
                self.buttonReset.config(image=self.glasses)
                # stop the stopwatch
                self.stopwatch.stop()
                # show messageboxes
                messagebox.showinfo("YOU WIN!", "Congratulations! You won!")
                messagebox.showinfo("TIME TAKEN", "You took " + str(int(self.stopwatch.getTime())) + " seconds to win the game!")
                time = self.findMinTime()
                # make a Prompt window, asking the user for his or her name
                if (self.mines == 10  and self.rows == 10 and self.columns == 10) or (self.mines == 20  and self.rows == 10 and self.columns == 20) or (self.mines == 50  and self.rows == 25 and self.columns == 20):
                    root2 = Tk()
                    root2.title("High Scorers")
                    reader = Prompt(root2, time, self.mines, self.rows, self.columns)
            # if there are more buttons with a normal state than the number of mines, set checkerList equal to an empty list
            else:
                checkerList = []


    # resets the board
    def resetBoard(self):
        # changes the image on the reset button
        self.buttonReset.config(image=self.smile)
        # generates another list of values for the buttons
        self.boardList = generateBoard(self.mines, self.rows, self.columns)
        # displays all the buttons on the window
        for xcoord in range(1, int(self.columns)+1):
            for ycoord in range(1, int(self.rows)+1):
                self.buttonDict[str(xcoord) + "," + str(ycoord)].config(state="normal", image=self.blank)
                self.buttonDict[str(xcoord) + "," + str(ycoord)].setImage(self.blank)
        # stops the stopwatch and resets it
        self.stopwatch.stop()
        self.stopwatch.reset()
        # changes the flag number to the number of mines and calls the updateFlagNumber method
        self.flagNumber = self.mines
        self.updateFlagNumber()
        # changes the label timer display to 0
        self.labelTimer.config(text="0")


    # if the difficulty level is changed, it destroys the current window and sets the defaults for the flag number and timer
    # it then remakes the window using the new values for mines, rows and columns
    def reload(self):
        self.canvas.destroy()

        self.stopwatch.stop()
        self.stopwatch.reset()
        self.flagNumber = self.mines
        self.updateFlagNumber()
        self.labelTimer.config(text="0")

        self.boardList = generateBoard(self.mines, self.rows, self.columns)

        self.scrollbar = Scrollbar(self.rootWindow, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="N" + "S")

        if self.mines == 10  and self.rows == 10 and self.columns == 10:
            self.canvas = Canvas(self, scrollregion=(0, 0, 350, 350), width=350, height=380)
        elif self.mines == 20  and self.rows == 10 and self.columns == 20:
            self.canvas = Canvas(self, scrollregion=(0, 0, 700, 350), width=700, height=380)
        elif self.mines == 50  and self.rows == 25 and self.columns == 20:
            self.canvas = Canvas(self, scrollregion=(0, 0, 700, 910), width=700, height=680)
        else:
            height = (self.rows + 1) * 35
            if self.rows >= 18:
                height = 680
            self.canvas = Canvas(self, scrollregion=(0, 0, self.columns * 35, (self.rows + 1) * 35), width=self.columns * 35, height=height)
        self.canvas.grid(row=0, column=0)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.yview)

        self.buttonDict = {}
        for x in range(1, int(self.columns) + 1):
            for y in range(1, int(self.rows) + 1):
                self.buttonTemplate = Box(self, image=self.blank, state="normal", command=lambda xc=x, yc=y: self.changeText(xc, yc))
                self.buttonTemplate_window = self.canvas.create_window((x * 35) - 20, (y * 35) + 20, window=self.buttonTemplate)
                if self.device == "pc":
                    self.buttonTemplate.bind("<Button-3>", lambda event, xc=x, yc=y: self.setFlag(event, xcoord=xc, ycoord=yc))
                else:
                    self.buttonTemplate.bind("<Button-2>", lambda event, xc=x, yc=y: self.setFlag(event, xcoord=xc, ycoord=yc))
                self.buttonDict[str(x) + "," + str(y)] = self.buttonTemplate

        self.buttonReset = Button(self, image=self.smile, command=self.resetBoard, height=25, width=25)
        self.buttonReset_window = self.canvas.create_window(self.columns * 17.3, 20, window=self.buttonReset)

        self.labelTimer = Label(self, text="0", bg="black", fg="red", font="Digital-7 25 bold", width=2, height=1)
        self.labelTimer_window = self.canvas.create_window(50, 20, window=self.labelTimer)

        self.labelFlag = Label(self, text=self.flagNumber, bg="black", fg="red", font="Digital-7 25 bold", width=2, height=1)
        self.labelFlag_window = self.canvas.create_window((self.columns * 35) - 55, 20, window=self.labelFlag)