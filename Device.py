"""
Displays to the user the various device options (Mac/PC) -- changes the value in the Application class so that the
appropriate code can be executed
"""


from tkinter import *

class Device(Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.grid()

        self.root = root

        self.app = app # reference to the Application class, to have access to its variables and methods

        # the string variable, with default value set as "mac"
        self.deviceVar = StringVar(value="mac")

        # the two radiobuttons displaying options - Mac and PC
        self.radioMac = Radiobutton(self, text="Mac", value="mac", variable=self.deviceVar, command=self.setMac)
        self.radioMac.grid(row=0, column=0)

        self.radioPc = Radiobutton(self, text="PC", value="pc", variable=self.deviceVar,command=self.setPC)
        self.radioPc.grid(row=0, column=2)

        # submit button to call the setValue method
        self.buttonSubmit = Button(self, text="Submit", command=self.setValue, state="normal")
        self.buttonSubmit.grid(row=2, column=1)

    # the radiobuttons don't automatically update the value of the string variable on Macs so I use following two methods
    # to change the default value for deviceVar
    # sets the deviceVar as "mac"
    def setMac(self):
        self.deviceVar.set("mac")

    # sets the deviceVar as "pc"
    def setPC(self):
        self.deviceVar.set("pc")

    # sets the value of the device variable of the Application class to the string in deviceVar
    # closes the Choose Device window
    def setValue(self):
        self.app.device = self.deviceVar.get()
        self.app.reload()
        self.root.destroy()