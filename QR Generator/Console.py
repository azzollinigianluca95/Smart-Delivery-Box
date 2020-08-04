#!/usr/bin python

from tkinter import *
import tkinter.messagebox
import qrcode
from PIL import Image
import LayoutStandard
import Windows

mainWin = Tk()
mainWin.title("Smart Delivery Box")
mainWin.resizable(False,False)

layout = LayoutStandard.LayoutStandard(mainWin)
layout.pack()

Windows.Windows(layout.centro).requestWindow()


mainWin.mainloop()