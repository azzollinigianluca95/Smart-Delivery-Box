from Crypto.Cipher import AES
import base64

from Crypto.Cipher.AES import AESCipher


class Cripting:


    def __init__(self, key, order):

        self.SDB_ID = key
        self.OrderId = order.rjust(32)

        self.cipher = AES.new(self.SDB_ID, AES.MODE_ECB)

    def encode(self):
        return base64.b64encode(self.cipher.encrypt(self.OrderId))

    def decode(self, encoded):
        return cipher.decrypt(base64.b64decode(encoded)).strip()