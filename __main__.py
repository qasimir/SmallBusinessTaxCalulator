from tkinter import *
from Incomings import IncomingsForm as incomings
from Outgoings import OutgoingsForm as outgoings
from Settings import SettingsForm as settings
from deleteIncomingWindow import deleteIncoming as deleteIncoming
from deleteOutgoingWindow import deleteOutgoing as deleteOutgoing

import csv


class mainWindow:

    def __init__(self):
        # set up the project and frames
        ########################################
        self.root = Tk()
        self.root.title("Tax Calculator")
        self.root.geometry("500x500")
        self.showButtonFrame = Frame(self.root, height=25)
        self.showButtonFrame.pack()
        self.deleteButtonFrame = Frame(self.root, height=25)
        self.deleteButtonFrame.pack()
        self.displayFrame = Frame(self.root, height=25)
        self.displayFrame.pack()
        ########################################

        # set up the toolbar
        ########################################
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New Incoming", command=self.new_incomings_window)
        fileMenu.add_command(label="New Outgoing", command=self.new_outgoings_window)
        settingsMenu = Menu(menubar)
        settingsMenu.add_command(label="Settings", command=self.settings_window)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Settings", menu=settingsMenu)

        Button(self.showButtonFrame, text="Show Incomings", command=self.showIncomings).pack(side=LEFT)
        Button(self.showButtonFrame, text="Show Outgoings", command=self.showOutgoings).pack(side=LEFT)
        Button(self.deleteButtonFrame, text="Delete an Incoming", command=self.deleteAnIncoming).pack(side=LEFT)
        Button(self.deleteButtonFrame, text="Delete an Outgoing", command=self.deleteAnOutgoing).pack(side=LEFT)

        ########################################

        # set up the data
        ########################################
        self.incomingsdata = []
        self.outgoingsdata = []
        ########################################
        self.root.mainloop()


    def showIncomings(self):
        # need to cover the case where there are no incomings and/or blank vars
        self.displayFrame.destroy()
        self.displayFrame = Frame(self.root, height=25)
        self.displayFrame.pack()
        i=0
        for d in self.incomingsdata:
            i+=1
            labelText= "ID: {} \n {}, {}, {}".format(i, d[0], d[1], d[2])
            Label(self.displayFrame, text=labelText).pack()
            Label(self.displayFrame, text="\n").pack()


    def showOutgoings(self):
        # need to cover the case where there are no incomings and/or blank vars
        self.displayFrame.destroy()
        self.displayFrame = Frame(self.root, height=25)
        self.displayFrame.pack()
        i=0
        for d in self.outgoingsdata:
            i+=1
            labelText= "ID: {} \n {}, {}, {}".format(i, d[0], d[1], d[2])
            Label(self.displayFrame, text=labelText).pack()
            Label(self.displayFrame, text="\n").pack()


    def deleteAnOutgoing(self):
        self.newWindow = Toplevel(self.root)
        self.incomingsApp = deleteOutgoing(self.newWindow,self.outgoingsdata, self.displayFrame)


    def deleteAnIncoming(self):
        self.newWindow = Toplevel(self.root)
        self.incomingsApp = deleteIncoming(self.newWindow, self.incomingsdata, self.displayFrame)


    def new_incomings_window(self):
        self.newWindow = Toplevel(self.root)
        self.incomingsApp = incomings(self.newWindow, self.incomingsdata)


    def new_outgoings_window(self):
        self.newWindow = Toplevel(self.root)
        self.outgoingsApp = outgoings(self.newWindow, self.outgoingsdata)

    def settings_window(self):
        self.newWindow = Toplevel(self.root)
        self.settingsApp = settings(self.newWindow)

mainWindow()


