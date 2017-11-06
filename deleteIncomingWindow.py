from tkinter import *

class deleteIncoming():

    def __init__(self, root, incomingsdata, displayFrame):
        self.root = root
        self.data = incomingsdata
        self.dispFrame = displayFrame
        self.frame = Frame(self.root)
        Label(self.frame, text = "choose the ID of the \n incoming entry you wish to delete and \n press ok").pack()
        self.ID=Entry(self.root)
        self.ID.pack()
        Button(self.frame, text = 'OK', width = 25, command = self.close_windows).pack()
        self.frame.pack()

    def close_windows(self):
        if (self.isInt(self.ID.get())):
            if (int(self.ID.get()) > len(self.data)):
                self.newWindow = Toplevel(self.root)
                self.incomingsApp = InvalidIndexWindow(self.newWindow)
            else:
                del self.data[int(self.ID.get()) - 1]
                self.dispFrame.destroy()
                self.root.destroy()
        else:
            newWindow = Toplevel(self.root)
            app = self.errorWindow(newWindow)

    def isInt(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False




    class errorWindow:
        def __init__(self, root):
            self.root = root
            self.frame = Frame(self.root)
            Label(self.root, text="ERROR! The ID needs to be expressed as a number\n Please try again ").pack()
            Button(self.frame, text='OK', command=self.close_windows).pack()
            self.frame.pack()

        def close_windows(self):
            self.root.destroy()


class InvalidIndexWindow:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        Label(self.root, text="ERROR! The ID chosen is invalid\n Please try again ").pack()
        Button(self.frame, text='OK', command=self.close_windows).pack()
        self.frame.pack()

    def close_windows(self):
        self.root.destroy()