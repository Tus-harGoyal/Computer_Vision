import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cv2 as cv

# testImg=cv.imread("resources/hand.png")
frame=cv.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=1)
blank= None
# hand,img=detector.findHands(testImg)
# cv.imshow("image",img)
# cv.waitKey(0)
# landMarks=hand[0]['lmList']
# x1,y1=landMarks[4][:2]
# x2,y2=landMarks[8][:2]
# # print(point1,point2)
# distance= ((x2-x1)**2 +  (y2-y1)**2)**0.5
# print(f'distance= {distance}')
newpos=0
currentpos=0
while True:
    
    Success, img= frame.read()
    img=cv.flip(img,1)
    hand,img= detector.findHands(img)
    if blank is None:
        blank=np.zeros_like(img)
        cvzone.putTextRect(blank,"RESET",(40,400))
    

    if hand:
        
        landMarks=hand[0]['lmList']
        
        x1,y1=landMarks[8][:2]
        x2,y2=landMarks[4][:2]
        currentpos=((x1+x2)//2,(y1+y2)//2)
        # print(point1,point2)
        distance= ((x2-x1)**2 +  (y2-y1)**2)**0.5
        print(f'distance= {distance}')
        
        if distance<20:
           
           cv.line(blank,currentpos,newpos,(0,0,255),5)
        if currentpos[1]>400:
            blank=np.zeros_like(img)
            cvzone.putTextRect(blank,"RESET",(40,400))

    newpos= currentpos
    combined = cv.addWeighted(img, 0.7, blank, 0.3, 0)
    cv.imshow("output",combined)  
    # cv.imshow("video",img) 
    
    if cv.waitKey(1) & 0XFF==27:
        break
    