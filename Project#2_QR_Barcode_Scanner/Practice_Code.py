import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode


'''var'''
path="resources/LOGO.png"
path2="resources/barcode.png"

HEIGHT=400
WIDHT=400

image = cv.resize(cv.imread(path2),(400,400),interpolation=cv.INTER_CUBIC)
# resize_Img=cv.resize(image,(HEIGHT,WIDHT),interpolation=cv.INTER_CUBIC)
cv.imshow("qrcode",image)
code= decode(image)
for barcode in code:
    print (barcode.data)
    print (barcode.rect[:2])
    
cv.rectangle(image,barcode.rect[:2],(barcode.rect[0]+barcode.rect[2],barcode.rect[1]+barcode.rect[3]),(0,255,0),4)
cv.imshow("qrcode",image)
cv.waitKey(0)