class qrcode:
    def __init__(self):
        import os
        
    def create(self, text, path_to_save = "encrypted.jpg"):
        import qrcode as code
        img = code.make(text)
        img.save(path_to_save)
        
    def read(self, path):
        import cv2
        d = cv2.QRCodeDetector()
        val, _, _ = d.detectAndDecode(cv2.imread(path))
        return val
