from tkinter import *

class SettingsForm():

    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()


        #Year:
        ###################################
        Label(self.root, text="Set Year").pack()
        self.year=StringVar(self.root)
        self.yearEntry=Entry(self.root)
        self.yearEntry.pack()
        ###################################

        #Month
        ###################################
        Label(self.root, text="Set Month").pack()
        self.month = StringVar(self.root)
        self.month.set("Month")
        months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        self.monthOptionMenu = OptionMenu(self.root, self.month, *(months))
        self.monthOptionMenu.pack()
        ###################################

        self.quitButton = Button(self.root, text='Apply', command=self.close_windows)
        self.quitButton.pack()



    def close_windows(self):
        self.root.destroy()