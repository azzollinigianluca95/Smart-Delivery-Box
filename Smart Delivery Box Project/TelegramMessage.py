# coding=utf-8

import telegram

#token that can be generated talking with @BotFather on telegram

def send(msg, chat_id, token='729495740:AAEgizCJAcGAYdRgszvKRTrMZSaOJKkP2eg'):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)


def sendqr(chat_id):
	bot = telegram.Bot(token='729495740:AAEgizCJAcGAYdRgszvKRTrMZSaOJKkP2eg')
	send("\n Puoi aprire la tua SmartDeliveryBox con il seguente QR Code: \n", chat_id)
	bot.send_photo(chat_id=chat_id, photo=open('SpecialKeyQRCode.png', 'rb'))
	#bot.send_photo(chat_id=chat_id, photo=open('/Users/memoriessrls/PycharmProjects/RaspberryPI_Orders/SpecialKeyQRCode.png', 'rb'))

