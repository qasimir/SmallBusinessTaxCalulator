from tkinter import *

class OutgoingsForm():

    def getMonth(self):
        print(self.month.get())

    def getDay(self):
        print(self.day.get())

    def settings_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Demo2(self.newWindow)

    def new_incomings_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Demo2(self.newWindow)

    def new_outgoings_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = outgoingsForm(self.newWindow)

    def __init__(self, root):
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
        fileMenu.add_command(label="Incomings", command=self.new_incomings_window)
        fileMenu.add_command(label="Outgoings", command=self.new_outgoings_window)
        settingsMenu = Menu(menubar)
        settingsMenu.add_command(label="Settings", command=self.settings_window)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Settings", menu=settingsMenu)
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
        ########################################
        self.root.mainloop()






class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()










    def setDay(self, value):
        self.day = value

    def setDescription(self, value):
        self.description = value

    def setAmount(self, value):
        self.amount = value

    def getDay(self):
        return self.day

    def getDescription(self):
        return self.description

    def getAmount(self, value):
        return self.amount

    def submit(self):
        if (self.isFloat(self.amountEntry.get())):
            self.setAmount(self.amountEntry.get())
            self.setDay(self.day)
            self.setDescription(self.descEntry.get())
            self.data.append([self.day.get(), self.descEntry.get(), self.amountEntry.get()])
            self.root.destroy()
        else:
            newWindow = Toplevel(self.root)
            app = self.errorWindow(newWindow)