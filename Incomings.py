from tkinter import *


class IncomingsForm():




    def __init__(self, root, data):
        self.root = root
        self.frame = Frame(self.root)

        self.data = data

        # set up the month and day drop down
        ########################################
        self.day = StringVar(self.root)
        Label(self.root, text="Date").pack()
        self.day.set("Date")
        days = (
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.dayOptionMenu = OptionMenu(self.root, self.day, *(days))
        self.dayOptionMenu.pack()
        ########################################

        # Description:
        ########################################
        Label(self.root, text="Description").pack()
        self.descEntry = Entry(self.root)
        self.descEntry.pack()
        ########################################

        # amount:
        ########################################
        Label(self.root, text="Amount").pack()
        self.amountEntry = Entry(self.root)
        self.amountEntry.pack()
        ########################################

        # submit button
        ########################################
        self.submitButton = Button(self.root, text="Submit", command=self.submit)
        self.submitButton.pack()
        ########################################


        self.frame.pack()

    def isFloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False


    def submit(self):
        if (self.isFloat(self.amountEntry.get())):
            self.data.append([self.day.get(), self.descEntry.get(), self.amountEntry.get()])
            self.root.destroy()
        else:
            newWindow = Toplevel(self.root)
            app = self.errorWindow(newWindow)


    class errorWindow:
        def __init__(self, root):
            self.root = root
            self.frame = Frame(self.root)
            Label(self.root, text="ERROR! The amount needs to be expressed as:\n \"123.45\" Please try again ").pack()
            Button(self.frame, text='OK', command=self.close_windows).pack()
            self.frame.pack()

        def close_windows(self):
            self.root.destroy()