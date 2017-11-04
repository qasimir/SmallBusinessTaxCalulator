from tkinter import *
import csv

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class IncomingsForm():

    def getMonth(self):
        print(self.month.get())

    def getDay(self):
        print(self.day.get())

    def new_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Demo2(self.newWindow)

    def __init__(self):
        # set up the project
        ########################################
        self.root = Tk()
        self.root.title("Invoice Submission")
        self.root.geometry("500x500")
        ########################################

        #set up the toolbar
        ########################################
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Incomings", command=self.newWindow)
        fileMenu.add_command(label="Outgoings", command=self.newWindow)
        settingsMenu = Menu(menubar)
        settingsMenu.add_command(label="Settings")
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Settings", menu=settingsMenu)
        ########################################

        # add a couple of panes
        ########################################

        ########################################


        #set up the month and day drop down
        ########################################
        self.month = StringVar(self.root)
        self.month.set("Month")
        self.day = StringVar(self.root)
        self.day.set("Date")
        days = (
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        self.monthOptionMenu = OptionMenu(self.root, self.month, *(months))
        self.dayOptionMenu = OptionMenu(self.root, self.day, *(days))
        self.monthOptionMenu.pack()
        self.dayOptionMenu.pack()
        ########################################

        # Description:
        ########################################
        Label(self.root, text="Description").pack()
        self.entry = Entry(self.root)
        self.entry.pack()
        ########################################

        #submit button
        ########################################
        self.submitButton = Button(self.root, text="Submit", command = self.getDay)
        self.submitButton.pack()
        self.root.mainloop()
        ########################################





IncomingsForm()
