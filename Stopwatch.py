"""
Stopwatch class acts as a stopwatch that counts the seconds it takes for a player to win a game
This time is then used to rank the players
"""


import time

class Stopwatch:
    def __init__(self):
        self.startVal = 0 # epoch = 0 seconds
        self.endVal = 0 # end time = 0 seconds
        self.runTime = 0 # how long the stopwatch has been running
        self.on = False # is th stopwatch on (True) or off (False)

    # start method checks if the stopwatch is running
    # if it isn't, it sets the epoch as the current time, found using time.time()
    # it then changes the self.on value to True
    def start(self):
        if not self.on:
            self.startVal = time.time()
            self.on = True

    # update method updates the runTime by subtracting the start time (startVal) from the current or end time (endVal)
    def update(self):
        if self.on:
            self.runTime = time.time() - self.startVal
        else:
            self.runTime = self.endVal - self.startVal

    # calls the update method and returns the current run time
    def getTime(self):
        self.update()
        return self.runTime

    # stop method checks if the stopwatch is running
    # if it is, it finds the end time (endVal) using time.time(), calls the update method and sets self.on as False
    def stop(self):
        if self.on:
            self.endVal = time.time()
            self.update()
            self.on = False

    # reset method makes the values of self.startVal, self.runTime, and self.endVal as 0 again
    def reset(self):
        self.startVal = 0
        self.runTime = 0
        self.endVal = 0