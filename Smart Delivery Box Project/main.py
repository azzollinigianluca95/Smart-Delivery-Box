# coding=utf-8

import time
import ScanQR
import TelegramMessage
from subprocess import call
import ServoMotor
import RPi.GPIO as GPIO
import Orders

#Inizilizzo Pin e ServoMotore
GPIO.setmode(GPIO.BCM)
ServoMotor.ServoClose()

'''
In un while 1 la piCamera continua a cercare Qr Code da scannerizzare,
decriptandoli usando come chiave di cifratura il seriale della SDB,
Fintanto che il seriale dell'ordine non matcha la lista degli ordini in arrivo presenti sulla SDB (orders.txt)
(Si presume che il sudetto file venga aggiornato da Amazon e si refreshi all'avvio della SDB)
Infine vengono restituiti i dati dell'ordine in fase di consegna
'''
b = ScanQR.scanqr() #Avvio Processo di ScanQR

'''
b==1 -> QR Speciale
b not none -> QR Letto correttamente dal postino
b is none -> QR NON Letto, NO apertura
'''
#Caso lettura QR in maniera corretta da Postino
if b is not None and b!=1:
    #Eliminazione ordine da "Orders.txt"
    Orders.Orders().deleteOrder(b.SerialNumber)
    
    ServoMotor.ServoOpen()
    time.sleep(40)  # Tempo inserimento pacco nel SDB
    ServoMotor.ServoClose()
    
    # Invio Messaggio da TelegramBot
    message_T = "Ciao " + b.CustomerName + " il tuo ordine che include: " + b.OrderDescription + " è in consegna presso la seguente SmartDeliveryBox: " + b.DeliveryBoxSerial
    TelegramMessage.send(message_T, b.CustomerTelegram.strip())
    time.sleep(2)
    TelegramMessage.sendqr(b.CustomerTelegram.strip())

#Caso lettura QR "Speciale" in maniera corretta
if b is not None and b==1:
    ServoMotor.ServoOpen()
    time.sleep(40) #Tempo inserimento pacco nel SDB
    ServoMotor.ServoClose()
    ScanQR.RGB.RGBClass.green_off()

#Turn off SDB
GPIO.cleanup()
call("sudo nohup shutdown -h now", shell = True)