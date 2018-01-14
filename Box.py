"""
Box class inherits from Button, but has an extra attribute for image (because access to the image attribute is limited
in the Button class)
"""


from tkinter import Button

class Box(Button):
    def __init__(self, rootWindow, image , state, command):
        super().__init__(rootWindow, image=image, state=state, command=command)
        self.__image = image

    def getImage(self):
        return self.__image

    def setImage(self, newImage):
        self.__image = newImage