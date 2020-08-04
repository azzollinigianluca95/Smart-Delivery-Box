import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Orders:

    def __init__(self):

        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', self.scope)

        self.client = gspread.authorize(self.creds)

        self.sheet = self.client.open('Ordini').sheet1


    def loadOrder(self):

        num = 1
        ordini = self.sheet.get_all_records()

        for x in ordini:
            num = num + 1
            #print (num) #Conto righe


        if (num != 0):

            x=2
            out_file = open("order.txt", "w+")
            out_file.write("{}\t{}\t{}\t{}\t{}\n".format(self.sheet.cell(x, 1).value, self.sheet.cell(x, 2).value,
                                                         self.sheet.cell(x, 3).value, self.sheet.cell(x, 4).value,
                                                         self.sheet.cell(x, 5).value))
            out_file.close()

            if (num > 2):

                for x in range(3,num+1):

                    #print(self.sheet.cell(x,5).value) #ID Telegram
                    #print(x)

                    out_file = open("order.txt", "a")
                    out_file.write("{}\t{}\t{}\t{}\t{}\n".format(self.sheet.cell(x,1).value,self.sheet.cell(x,2).value,self.sheet.cell(x,3).value,self.sheet.cell(x,4).value,self.sheet.cell(x,5).value))
                    out_file.close()

    def findIndex(self, order):

        num = 1
        orders = self.sheet.get_all_records()

        for x in orders:
            num = num + 1

        for x in range(2, num + 1):

            if(order == self.sheet.cell(x,1).value):
                return x

    def deleteLine(self, index):
        self.sheet.delete_row(index)

    def deleteOrder(self, order):
        self.sheet.delete_row(self.findIndex(order))