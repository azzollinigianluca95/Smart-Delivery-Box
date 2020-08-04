from tkinter import *
import tkinter.messagebox
import qrcode
from PIL import Image, ImageTk
import Cripting
import Orders

class Windows:
    
    def __init__(self,where):
        
        self.frame = where
        
        
        
    def requestWindow(self):
    
        spedizioneButton = Button(self.frame, text="Voglio spedire", command= self.shipment)
        consegnaButton = Button(self.frame, text="Aggiungi ordine", command=self.addOrder)

        spedizioneButton.grid(row=0, column=0, padx=10, pady=5)
        consegnaButton.grid(row=0, column=1, padx=10, pady=5)


    def shipment(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.labelID = Label(self.frame, text="Order ID")  # Testo "Order ID"
        self.entryID = Entry(self.frame)  # Spazio per inserire l'ordine
        self.OKButton = Button(self.frame, text="Genera QR", command= self.buttonCondition1)

        self.labelID.pack(side=LEFT, pady=5)
        self.entryID.pack(side=LEFT)
        self.OKButton.pack(padx=2)


    def showQR(self):

        orderID = self.entryID.get()

        for widget in self.frame.winfo_children():
            widget.destroy()

        encoder = Cripting.Cripting('SDB-000-AAA-AAAA', orderID)
        img = qrcode.make(encoder.encode())
        img.save('tempQR.png')

        qrImage = ImageTk.PhotoImage(Image.open("tempQR.png"))

        label = Label(self.frame, image=qrImage)
        label.photo = qrImage

        label.pack()



    def addOrder(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.QRflag=1

        self.labelOrderID = Label(self.frame, text="ID Ordine")
        self.entryOrderID = Entry(self.frame)

        self.labelItem = Label(self.frame, text="Cosa consegni")
        self.entryItem = Entry(self.frame)

        self.labelReceiver = Label(self.frame, text="Destinatario")
        self.entryReceiver = Entry(self.frame)

        self.labelTelegramID = Label(self.frame, text="ID Telegram")
        self.entryTelegramID = Entry(self.frame)


        self.OKButton = Button(self.frame, text="Invia", command=self.buttonCondition2)


        self.labelOrderID.grid(row=0, column=0, pady=2, padx=2)
        self.entryOrderID.grid(row=0, column=1, pady=2, padx=2)

        self.labelItem.grid(row=0, column=2, padx=2)
        self.entryItem.grid(row=0, column=3, pady=2)

        self.labelReceiver.grid(row=1, column=0, padx=2)
        self.entryReceiver.grid(row=1, column=1, pady=2)

        self.labelTelegramID.grid(row=1, column=2, padx=2)
        self.entryTelegramID.grid(row=1, column=3, pady=2)


        self.OKButton.grid(row=2, column=3, sticky=E, pady=2)
        

    def buttonCondition1(self):

        ID = self.entryID.get()
        if (len(ID) > 32):
            tkinter.messagebox.showerror("ERRORE","ID Ordine non valido:\nlunghezza massima 32 caratteri")

        if (len(ID) < 32):
            self.showQR()

    def buttonCondition2(self):

        orderID = self.entryOrderID.get()
        if (len(orderID) > 32):
            tkinter.messagebox.showerror("ERRORE","ID Ordine non valido:\nlunghezza massima 32 caratteri")


        if (len(orderID) < 32):
            self.addLine()



    def addLine(self):
        orderID = self.entryOrderID.get()
        item = self.entryItem.get()
        receiver = self.entryReceiver.get()
        telegramID = self.entryTelegramID.get()

        for widget in self.frame.winfo_children():
            widget.destroy()

        row = ["{}".format(orderID), "SDB-000-AAA-AAAA", "{}".format(receiver),"{}".format(item),"{}".format(telegramID)]

        tkinter.messagebox.showinfo("","Caricamento avvenuto con successo")

        tkinter._exit()

        Orders.Orders().addRow(row)

