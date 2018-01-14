"""
This file contains only one function - generateBoard() - which is used by the Application class
to generate a minesweeper board with randomly arranged mines, and consequently generate a number for each of
the surrounding boxes
"""


import random

# function: generateBoard
# description: generates a list of lists representing rows, each "row" list has the values of the buttons in that row
# input: number of mines, number of rows, number of columns
# output: a list of "row" lists containing the values of different buttons
def generateBoard(mines, rows, columns):
    # mines, rows and columns are respectively the number of mines, rows and columns the board should have
    mines = int(mines)
    # makes an empty dictionary to which all physical positions of boxes are added as keys (in the format [x-coordinate,y-coordinate] or [column#,row#])
    dict = {}
    for x in range(1, columns+1):
        for y in range(1, rows+1):
            dict[(str(x) + "," + str(y))] = 0

    # randomly distribute the however many mines are specified before throughout the board
    # this is done by randomly generating an x and y coordinate and concatenating the strings together with a comma in between
    # these strings (keys) along with their values are added to the dictionary
    # the coordinates are also added to a list composed solely of all the mines on the board
    mineList = []
    for i in range(0, mines):
        randx = random.choice(range(1, columns + 1))
        randy = random.choice(range(1, rows + 1))
        tempMine = str(randx) + "," + str(randy)
        # if the randomly generated mine is already a mine, the process is repeated
        while dict[tempMine] == "m":
            randx = random.choice(range(1, columns + 1))
            randy = random.choice(range(1, rows + 1))
            tempMine = str(randx) + "," + str(randy)
        dict[tempMine] = "m"
        mineList.append(tempMine)

    # for each mine in mineList, the value of the surrounding boxes is updated by 1
    for string in mineList:
        tempCood = string.split(",")
        tempCood[0] = int(tempCood[0])
        tempCood[1] = int(tempCood[1])
        # for the central boxes, excluding the first and last rows and columns
        if tempCood[0] in range(2, columns) and tempCood[1] in range(2, rows):
            SW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) + 1)
            S = str(int(tempCood[0])) + "," + str(int(tempCood[1]) + 1)
            SE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) + 1)
            W = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]))
            E = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]))
            NW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) - 1)
            N = str(int(tempCood[0])) + "," + str(int(tempCood[1]) - 1)
            NE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) - 1)
            checkList = [SW, S, SE, W, E, NW, N, NE]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the first column, excluding corners
        elif tempCood[0] == 1 and tempCood[1] in range(2, rows):
            S = str(int(tempCood[0])) + "," + str(int(tempCood[1]) + 1)
            SE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) + 1)
            E = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]))
            N = str(int(tempCood[0])) + "," + str(int(tempCood[1]) - 1)
            NE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) - 1)
            checkList = [S, SE, E, N, NE]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the last column, excluding corners
        elif tempCood[0] == columns and tempCood[1] in range(2, rows):
            SW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) + 1)
            S = str(int(tempCood[0])) + "," + str(int(tempCood[1]) + 1)
            W = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]))
            NW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) - 1)
            N = str(int(tempCood[0])) + "," + str(int(tempCood[1]) - 1)
            checkList = [SW, S, W, NW, N]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the last row, excuding corners
        elif tempCood[1] == rows and tempCood[0] in range(2, columns):
            W = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]))
            E = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]))
            NW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) - 1)
            N = str(int(tempCood[0])) + "," + str(int(tempCood[1]) - 1)
            NE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) - 1)
            checkList = [W, E, NW, N, NE]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the first row, excluding corners
        elif tempCood[1] == 1 and tempCood[0] in range(2, columns):
            SW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) + 1)
            S = str(int(tempCood[0])) + "," + str(int(tempCood[1]) + 1)
            SE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) + 1)
            W = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]))
            E = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]))
            checkList = [SW, S, SE, W, E]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the North-West corner [at position (1,1)]
        elif tempCood[0] == 1 and tempCood[1] == 1:
            S = str(int(tempCood[0])) + "," + str(int(tempCood[1]) + 1)
            SE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) + 1)
            E = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]))
            checkList = [S, SE, E]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the South-West corner [at position (1, last row #)]
        elif tempCood[0] == 1 and tempCood[1] == rows:
            E = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]))
            N = str(int(tempCood[0])) + "," + str(int(tempCood[1]) - 1)
            NE = str(int(tempCood[0]) + 1) + "," + str(int(tempCood[1]) - 1)
            checkList = [N, NE, E]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the North-East corner [at position (last column #, 1)
        elif tempCood[0] == columns and tempCood[1] == 1:
            SW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) + 1)
            S = str(int(tempCood[0])) + "," + str(int(tempCood[1]) + 1)
            W = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]))
            checkList = [S, SW, W]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass
        # for the South-East corner [at position (last column #, last row #)
        elif tempCood[0] == columns and tempCood[1] == rows:
            NW = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]) - 1)
            N = str(int(tempCood[0])) + "," + str(int(tempCood[1]) - 1)
            W = str(int(tempCood[0]) - 1) + "," + str(int(tempCood[1]))
            checkList = [N, NW, W]
            for item in checkList:
                if dict[item] in range(0, 8):
                    dict[item] += 1
                elif dict[item] == "m":
                    pass


    # a new list is created, to which empty list equal to the number of rows are added
    ultimateList = []
    for i in range(0, rows):
        tempList = []
        ultimateList.append(tempList)

    # the values of each row are then appended to the previously created list of lists
    # this means that ultimate list is a list of rows, and each list within ultimateList has the column values of each row
    # this list is the function's output
    for row in range(0, rows):
        for column in range(0, columns):
            ultimateList[row].append(dict[str(column+1) + "," + str(row+1)])
    return ultimateList