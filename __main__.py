from tkinter import *
from Incomings import IncomingsForm as incomings
from Outgoings import OutgoingsForm as outgoings
from Settings import SettingsForm as settings

import csv


class mainWindow:

    def __init__(self):
        # set up the project
        ########################################
        self.root = Tk()
        self.root.title("Tax Calculator")
        self.root.geometry("500x500")
        ########################################

        # set up the toolbar
        ########################################
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Incomings", command=self.new_incomings_window)
        fileMenu.add_command(label="Outgoings", command=self.new_outgoings_window)
        settingsMenu = Menu(menubar)
        settingsMenu.add_command(label="Settings", command=self.settings_window)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Settings", menu=settingsMenu)

        Button(self.root, text="Show Incomings", command=self.showIncomings).pack()
        ########################################

        # set up the data
        ########################################
        self.incomingsdata = []
        self.outgoingsdata = []
        ########################################
        self.root.mainloop()


    def showIncomings(self):
        print(self.incomingsdata[0])# need to cover the case where there are no incomings and/or blank vars
        i=0
        for d in self.incomingsdata:
            i+=1
            labelText= "ID: {} \n {}, {}, {}".format(i, d[0], d[1], d[2])
            Label(self.root, text=labelText).pack()
            Label(self.root, text="\n").pack()



    def new_incomings_window(self):
        self.newWindow = Toplevel(self.root)
        self.incomingsApp = incomings(self.newWindow, self.incomingsdata)


    def new_outgoings_window(self):
        self.newWindow = Toplevel(self.root)
        self.outgoingsApp = outgoings(self.newWindow)

    def settings_window(self):
        self.newWindow = Toplevel(self.root)
        self.settingsApp = settings(self.newWindow)

mainWindow()
