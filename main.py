import qrcode
from PIL import Image
import os
import cv2
from pyzbar import pyzbar
import time
import numpy as np

class Read:

    def getFromImage(self, text, show=False):
        """
        PilImage formate QRcode
        """
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
        qr.add_data(text)
        qr.make(fit=True)
        raw_image = qr.make_image(fill_color='black', back_color="white")
        raw_image.save(f'QRcode{time.time()}.jpg')

        if show:
            raw_image.show()
        else:
            return raw_image

    def read_QR_code(self, path_output_dir):
        report_history = []
        report = []
        vidcap = cv2.VideoCapture(0)
        succ, img = vidcap.read()
        succ = True
        while succ:
            cv2.imshow('img', img)
            succ, img = vidcap.read()
            cv2.imwrite(os.path.join(path_output_dir, 'qrcode.png'), img)
            data = pyzbar.decode(Image.open(os.path.join(path_output_dir, 'qrcode.png')))
            os.remove(os.path.join(path_output_dir, 'qrcode.png'))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if data:
                for info in data:
                    actTime = time.asctime()
                    pts = np.array([info.polygon], np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(img, [pts], True, (0, 255, 0), 3)
                    cv2.putText(img, info.data.decode(), (info.rect[0], info.rect[1]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                    if info.data.decode() not in report_history:
                        report_history.append(info.data.decode())
                        if report_history[-1] != report:
                            report = report_history[-1]
                            with open('register.txt', 'a') as f:
                                f.writelines(actTime + "***" + report + "\n" )
                                print(report)
        cv2.destroyAllWindows()
        vidcap.release()




rd = Read()
# rd.getFromImage('Test qr code', True)
rd.read_QR_code('C:\\Users\\stefan.gal\\Documents\\Python\\Projects\\')
