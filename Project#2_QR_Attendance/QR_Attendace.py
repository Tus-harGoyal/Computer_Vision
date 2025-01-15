import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode

cam=0
HEIGHT=1080
WIDHT=1920
# cap=cv.VideoCapture(cam)
# cap.set(3,600)
# cap.set(4,800)
# cap.set(cv.CAP_PROP_FRAME_WIDTH, WIDHT)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
image=cv.imread("resources/Employee.png")
image=cv.resize(image,(400,600),interpolation=cv.INTER_AREA)
with open('DataBase.text') as file:
    myList= file.read().splitlines()
print(myList)


code= decode(image)
print(len(code))
attendance=[]
for barcode in code:
    
    data=barcode.data.decode('utf-8')
    vertex=barcode.rect
    
    '''Authentication'''
    
    if data in myList:
        
        arr=np.array([barcode.polygon],np.int32)
        arr=arr.reshape(-1,1,2)
        cv.putText(image,data,(vertex[0]+vertex[2],vertex[1]),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
        cv.putText(image,"Authentic",(vertex[0]+vertex[2],vertex[1]+vertex[2]),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
        cv.polylines(image,[arr],True,(0,255,0),2)
        if data not in attendance:
            attendance.append(data)
    else:
        arr=np.array([barcode.polygon],np.int32)
        arr=arr.reshape(-1,1,2)
        cv.polylines(image,[arr],True,(0,0,255),2)
        cv.putText(image,data,(vertex[0]+vertex[2],vertex[1]),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
        cv.putText(image,"Un-Authentic",(vertex[0]+vertex[2],vertex[1]+vertex[2]),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)

        # print(f'{data} is a un-authinticated user')
            

cv.imshow("qr",image)
cv.waitKey(0)
print (f'employees present : {attendance}')
A=set(myList)
B=set(attendance)
absentees=list(A-B)
print(f'absentees= {absentees}')
print (f'strength : {len(attendance)}')
    