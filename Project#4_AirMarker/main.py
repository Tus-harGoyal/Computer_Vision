import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cv2 as cv

# testImg=cv.imread("resources/hand.png")
frame=cv.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=1)
blank= None
def Cal_distance(p1,p2):
    x1,y1=p1  #index
    x2,y2=p2
    distance= ((x2-x1)**2 +  (y2-y1)**2)**0.5
    return distance
def mid(p1,p2):
    x1,y1=p1  #index
    x2,y2=p2
    mid=((x1+x2)//2,(y1+y2)//2)
    return mid


# hand,img=detector.findHands(testImg)
# cv.imshow("image",img)
# cv.waitKey(0)
# landMarks=hand[0]['lmList']
# x1,y1=landMarks[4][:2]
# x2,y2=landMarks[8][:2]
# # print(point1,point2)
# distance= ((x2-x1)**2 +  (y2-y1)**2)**0.5
# print(f'distance= {distance}')
ErasePosN = (0, 0)
ErasePosI = (0, 0)
currentpos = (0, 0)
newpos = (0, 0)
colour=(0,0,255)
while True:
    
    Success, img= frame.read()
    img=cv.flip(img,1)
    hand,img= detector.findHands(img,draw=False)
    if blank is None:
        blank=np.zeros_like(img)
        cvzone.putTextRect(blank,"RESET",(40,400))
        cvzone.putTextRect(blank,"G",(40,100),5,5,(255,255,255),(0,255,0))
        cvzone.putTextRect(blank,"B",(40,200),5,5,(255,255,255),(255,255,0))
        cvzone.putTextRect(blank,"R",(40,300),5,5,(255,255,255),(0,0,255))

    if hand:
        
        landMarks=hand[0]['lmList']
        p1=landMarks[8][:2]  #index
        p2=landMarks[4][:2]  #thumb
        p3=landMarks[12][:2] #middle

        currentpos=mid(p1,p2)
        ErasePosI=mid(p1,p3)
        # print(point1,point2)
        distance= Cal_distance(p1,p2)
        distanceEraser= Cal_distance(p1,p3)
        print(f'current= {currentpos}')
        if p1[0]<100 and p1[0]>40 and p1[1]>50 and p1[1]<100:
            print("green")
            colour=(0,255,0)
        if p1[0]<100 and p1[0]>40 and p1[1]>150 and p1[1]<200:
            print("blue")
            colour=(255,255,0)
        if p1[0]<100 and p1[0]>40 and p1[1]>250 and p1[1]<300:
            print("red")
            colour=(0,0,255)

        if distance<20:
           
           cv.line(blank,currentpos,newpos,colour,5)
           #resetting
        if p1[0]<200 and p1[0]>40 and p1[1]>350 and p1[1]<400:
            blank=np.zeros_like(img)
            cvzone.putTextRect(blank,"RESET",(40,400))
            cvzone.putTextRect(blank,"G",(40,100),5,5,(255,255,255),(0,255,0))
            cvzone.putTextRect(blank,"B",(40,200),5,5,(255,255,255),(255,255,0))
            cvzone.putTextRect(blank,"R",(40,300),5,5,(255,255,255),(0,0,255))      

        if distanceEraser<25: 
           cv.line(blank,ErasePosI,ErasePosN,(0,0,0),30)
           cv.circle(img,ErasePosN,10,(255,250,255),cv.FILLED)

        


    newpos= currentpos
    ErasePosN=ErasePosI
    combined = cv.addWeighted(img, 0.7, blank, 0.3, 0)
    cv.imshow("output",combined)  
    # cv.imshow("video",img) 
    
    if cv.waitKey(1) & 0XFF==27:
        break
    