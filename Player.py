"""
Player class - this object is user to represent every individual who wins a Minesweeper game
It is primarily used to retain the player's name, the minimum time within which he/she won a game, and the total number of games he/she won
"""


class Player(object):
    def __init__(self, name):
        self.name = name
        self.__numGames = 0 # default number of games is 0
        self.__minTime = 0 # default minimum time is 0

    # getter and setter functions
    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def setNumGames(self):
        self.__numGames += 1

    def getNumGames(self):
        return self.__numGames

    def getMinTime(self):
        return self.__minTime

    def setMinTime(self, newMinTime):
        # if a new game is won by a player, his/her minTime is only updated if the new minimum time is less than the previous one
        # and if the previous one is not zero (which is the default when any new player starts a game)
        if newMinTime < self.__minTime and self.__minTime > 0:
            self.__minTime = newMinTime
        elif self.__minTime == 0:
            self.__minTime = newMinTime