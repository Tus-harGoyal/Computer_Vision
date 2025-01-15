import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode


'''var'''
path="resources/LOGO.png"
path2="resources/barcode.png"
path3="resources/testBArCode.jpg"
cam=0

HEIGHT=1080
WIDHT=1920
cap=cv.VideoCapture(cam)
# cap.set(3,600)
# cap.set(4,800)
cap.set(cv.CAP_PROP_FRAME_WIDTH, WIDHT)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
Orgimage=cv.imread(path)
while True:
    Success,image=cap.read()
    # image = cv.resize(Orgimage,(500,500),interpolation=cv.INTER_CUBIC)
    code= decode(image)
    for barcode in code:
        print (barcode.data.decode('utf-8'))
        # print (barcode.rect[:2])
        # cv.rectangle(image,barcode.rect[:2],(barcode.rect[0]+barcode.rect[2],barcode.rect[1]+barcode.rect[3]),(0,255,0),4)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape(-1,1,2)
        cv.polylines(image,[pts],True,(255,0,255),3)
        vert=barcode.rect
        cv.putText(image,barcode.data.decode('utf-8'),(vert[0],vert[1]),cv.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)
    cv.imshow("qrcode",image)
    if cv.waitKey(1) & 0XFF==27 :
        break
