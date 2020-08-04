# coding=utf-8

class Order:
    def __init__(self, SerialNumber, DeliveryBoxSerial ,CustomerName, OrderDescription, CustomerTelegram, Delivered=0):
        self.SerialNumber = SerialNumber            #Order serial same as Amazon
        self.DeliveryBoxSerial = DeliveryBoxSerial  #Serial code of DeliveryBox
        self.CustomerName = CustomerName            #Name & Surname of the Customer
        self.OrderDescription = OrderDescription
        self.CustomerTelegram = CustomerTelegram    #Telegram Info about the Customer
        self.Delivered = Delivered