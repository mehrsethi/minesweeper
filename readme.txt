Running Main creates an instance of the Application class.


Application class creates the main window for the program. It calls the generateBoard function from the Board file to
generate the values for each of the buttons on the board. It then creates a number of Boxes (created by inheriting
from the Button class) on the window as per the difficulty level selected (the default is 100 Boxes, 10 rows, and 10
columns). All the boxes are added to a dictionary with the coordinates (column number, row number) of each box as its
key.
The Application class also creates a label to display a stopwatch, which is linked to the updateTime
method which updates the label every second. The Stopwatch class is instantiated in the constructor and starts when the
first button is clicked (using changeText). It is stopped when the game ends (using checkWinner method).
The Application window also has a label to count down the number of flags used to mark down the mines. This is linked to
the updateFlagNumber method which gets called in the setFlag method (whenever the user right clicks on a Box).
In the center of the first row of the Application window is the reset button which calls the resetBoard method. The
display of the reset button changes based on whether the user wins or loses a game, or if he/she is still playing it.

The Application class also creates the menubar with Settings and Help menus. The Help menu has an instructions command
which instantiates the Help window, that has the details of how the game is played. The Settings menu has the options
for starting a new game (calls the reset method), exiting the application (calls .quit()), changing the difficulty level
(opens a DifficultyLevel window), changing the device (opens a Device window), or viewing the scoreboard (instantiates
HighScorers).
The DifficultyLevel class updates the number of mines, rows and columns based on user input and then calls the reload
method of the Application class, which destroys and then remakes the entire window. The size of the Canvas also gets
accordingly adjusted. If the number of rows is greater than can be accommodated on the screen, the vertical scrollbar
gets activated. DifficultyLevel also has various error checking procedures to make sure the user inputs the correct
information.
The Device class updates the device variable in Application according to the selection made by the user, and then calls
the reload method of the Application class.


Clicking each button has three possibilities - the button opens if it has a number on it, the surrounding buttons also
open if the first button has a value of 0, and the game ends if the button is a mine. Whenever a button is clicked, the
changeText method gets called, which updates the image of the button with its value and disables the button. If the value
is zero it calls itself for all the surrounding buttons. It then calls the checkWinner method, which checks if the user
lost the game or not. If the button clicked was a mine, it opens a messagebox informing the user that he/she lost. If
the player didn't lose, the method checks if he/she won by counting all the unopened boxes and checking if they are equal
to the number of mines. If the more boxes are unclicked than the number of mines, then the game continues. If the user
wins the game, the Prompt class gets instantiated.


The Prompt window asks the player for his or her name, and takes the time taken for him or her to win the game from the
Application class. It then asks the user if he or she is an existing Player, and accordingly either updates the stats
for the existing Player object or creates a new object. There is also input error checking to make sure that the Player
object actually exists if the user selects the existing player option. It then opens the binary file containing a list of
all Players for the respective difficulty level, if it exists. It updates the list of Player and writes the updated list
back to the file.
If the user enters a name that has multiple Player objects, the MultipleUsers class gets instantiated. It displays a
listbox with all the players with the same name, along with their stats and asks the user to pick one.
It then displays the top five high scorers for that difficulty level to the user in a text box.
The Prompt window also has a button that allows the user to view all the high scorers for all difficulty levels. This
again instantiates the HighScorers class.


Currently, the "High Scorers - Easy" file has three Players with the name "Gumby", this can be used to test the
MultipleUsers feature. The "High Scorers - Intermediate" file doesn't exist to ascertain that the still program works,
and creates that file. The "High Scorers - Hard" file has many players to highlight the scrollbar feature of the
textboxes on the HighScorers window.