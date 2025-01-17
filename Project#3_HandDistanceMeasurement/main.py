import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import math

cap= cv.VideoCapture(0)
cap.set(3,500)
cap.set(4,600)

detector = HandDetector(detectionCon=0.8,maxHands=1)  #detection confidanced 80%

while True:
    Success, frame= cap.read()
    hand, img= detector.findHands(frame)
    
    if hand:
        landMarks=hand[0]['lmList']
        # print(landMarks[0][:2])                               #0 means hand no 1, Lmlist is Landmark list 
        x1,y1= landMarks[4][:2]
        x2,y2= landMarks[8][:2]
        # print (x1,y1)
        distance= ((x2-x1)**2+(y2-y1)**2)**0.5
        print("distace =", distance)
        # print (len(landMarks))
        # print (landMarks[4])
        lineImg=cv.line(img.copy(),(x1,y1),(x2,y2),(0,255,0),3)
        textImg=cv.putText(lineImg.copy(),str(round(distance,2)),((x1+x2)//2,(y1+y2)//2),cv.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
        cv.imshow("video",textImg)
    else: 
        cv.imshow("video",frame)
    

    if cv.waitKey(5) & 0XFF==27 :
        break
    
    