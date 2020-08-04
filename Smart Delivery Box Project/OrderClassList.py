# coding=utf-8

import OrderClass  # Import Python file

def loadorders():
    OrdersList = []
    orderFile = open('order.txt', 'r+')
    lines = orderFile.readlines()
    orderFile.seek(0)
    for line in lines:
        w = []
        for words in line.split('\t'):
            w.append(words)
        '''
        print w[0]
        print w[1]
        print w[2]
        print w[3]
        print w[4]
        '''
        OrdersList.append(OrderClass.Order(w[0], w[1], w[2], w[3], w[4]))
    return OrdersList

'''
QrCode = '408-0179906-0375508'

loadorders()

for OrderClass.Order in OrdersList:
    if QrCode == OrderClass.Order.SerialNumber:
        print OrderClass.Order.SerialNumber
        print OrderClass.Order.CustomerName
        print OrderClass.Order.OrderDescription

'''