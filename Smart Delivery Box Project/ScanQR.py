# Library
import io
import picamera
import zbar
import Crypter
import time
import RGB
import OrderClassList
import Orders
from PIL import Image
from time import sleep

# inizializzo il pin della porta GPIO
'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
'''
def scanqr():
    Orders.Orders().loadOrder() #Sincronizza Ordini da FoglioGoogle->orders.txt
    timeout=60 #Timeout time for QRCode scanning
    timeout_start = time.time() #Avvio Timer
    while time.time() < timeout_start + timeout:
        RGB.RGBClass()
        RGB.RGBClass.blue_on()
        RGB.RGBClass.red_off()
        RGB.RGBClass.green_off()
        # crea uno stream dati in memoria
        stream = io.BytesIO()

        #  visualizzazione dello streaming della camera
        with picamera.PiCamera() as camera:
            camera.exposure_mode = 'auto'
            camera.preview_fullscreen = False
            # ridimensiono il preview per poter interrompere in caso di problemi
            camera.preview_window = (300, 200, 640, 480)
            camera.start_preview()
            sleep(1)  # aumentare se si vuole inquadrare meglio
            camera.capture(stream, format='jpeg')

        # recupera tutto il flusso per creare l'immagine
        stream.seek(0)
        pil = Image.open(stream)

        # inizializza lo scan dell'immagine
        scanner = zbar.ImageScanner()

        # configura il lettore
        scanner.parse_config('enable')

        pil = pil.convert('L')
        width, height = pil.size
        # raw = pil.tostring()
        raw = pil.tobytes()

        # wrap dati della immagine
        image = zbar.Image(width, height, 'Y800', raw)

        # cerca un QRcode
        scanner.scan(image)

        # se la password corrisponde ed e' esatta
        for symbol in image:
            # if hashlib.sha256(password).hexdigest() == symbol.data:
            for order in OrderClassList.loadorders(): #Carico e inizializzo classe da Orders.txt
                ''' 
                TO SHOW + CMD CLICK                
                '''
                if (len(symbol.data)==44):
                    if Crypter.decode(symbol.data) == order.SerialNumber or Crypter.decode(symbol.data)=='000-0000000-0000001':
                        #Gestione SpecialKeyQRCode
                        if(Crypter.decode(symbol.data)=='000-0000000-0000001'):
                            order = 1

                        RGB.RGBClass.blue_off()
                        RGB.RGBClass.green_on()
                        '''
                        print Crypter.decode(symbol.data)
                        print order.SerialNumber
                        print len(symbol.data)
                        '''
                        return order  # strip Eliminato qui
                    else:
                        RGB.RGBClass.blue_off()
                        RGB.RGBClass.red_pulse()

                else:
                        RGB.RGBClass.blue_off()
                        RGB.RGBClass.red_pulse()
        # pulisci e cancella
        del (image)
    return None