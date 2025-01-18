import cv2 as cv
import cvzone
from cvzone.HandTrackingModule import HandDetector
import math
import random

cap= cv.VideoCapture(0)

img_dim=480,640
# cap.set(3,500)
# cap.set(4,600)

detector = HandDetector(detectionCon=0.8,maxHands=1)  #detection confidanced 80%

'''gameVar'''
#circles
cx,cy=100,100

press_Count=0
pressed=False

while True:
    Success, img= cap.read()
    img=cv.flip(img,1)
    hand, img= detector.findHands(img,draw=False)
    colour1=(255,255,0)
    colour2=(255,0,0)
    colour3=(255,100,0)
    
    
    if hand:
        landMarks=hand[0]['lmList']
        # print(landMarks[0][:2])                               #0 means hand no 1, Lmlist is Landmark list 
        x1,y1= landMarks[5][:2]
        x2,y2= landMarks[17][:2]
        # print (x1,y1)
        distance= ((x2-x1)**2+(y2-y1)**2)**0.5
        # print("distace =", distance)
        # print (len(landMarks))
        # print (landMarks[4])
        x,y,w,h=hand[0]['bbox']  #,y,,h,w
        # lineImg=cv.line(img.copy(),(x1,y1),(x2,y2),(255,255,0),3)
        cvzone.putTextRect(img,f'{round(distance,1)} cm',(x,y),2)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        if distance>100 and x<cx<x+w and y<cy<y+h:
            pressed=True
            colour1=0,0,255
            colour2=0,200,255
            colour3=200,0,255
            
        if distance<100 and pressed is True:
            press_Count+=1
            # print("count increassed")
            pressed=False
            cx=random.randint(50,img_dim[1]-50)
            cy=random.randint(50,img_dim[0]-50)

    # print(pressed)
     
    # print(press_Count)
    cvzone.putTextRect(img,str(press_Count),(500,50),2)
    cv.circle(img,(cx,cy),20,colour1,cv.FILLED)        
    cv.circle(img,(cx,cy),15,colour2,cv.FILLED)        
    cv.circle(img,(cx,cy),10,colour3,cv.FILLED)        
    
    cv.imshow("video",img)
    if cv.waitKey(1) & 0XFF==27 :
        break
    
    