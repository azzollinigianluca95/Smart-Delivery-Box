from tkinter import *

frame = None

class LayoutStandard:

    def __init__(self, where):
        self.frame = Frame(where)

        self.topFrame = Frame(self.frame, height=100, bg="lightblue")

        self.bottomFrame = Frame(self.frame, height=100, bg="lightblue")

        self.leftFrame = Frame(self.frame, width=100, bg="lightblue")

        self.rightFrame = Frame(self.frame, width=100, bg="lightblue")

        self.centro = Frame(self.frame, width=300, height=300)

    def pack(self):
        self.frame.pack()
        self.topFrame.pack(side=TOP, fill=X)
        self.bottomFrame.pack(side=BOTTOM, fill=X)
        self.leftFrame.pack(side=LEFT, fill=Y)
        self.rightFrame.pack(side=RIGHT, fill=Y)
        self.centro.pack()

    def unpackAll(self):
        self.topFrame.forget()
        self.bottomFrame.forget()
        self.leftFrame.forget()
        self.rightFrame.forget()
        self.centro.forget()

    def unpackCenter(self):
        for widget in self.centro.winfo_children():
            widget.destroy()
