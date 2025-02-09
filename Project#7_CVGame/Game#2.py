import numpy as np
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap=cv.VideoCapture(0)
h=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
w=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(h,w)

detector=HandDetector(detectionCon=0.8,maxHands=1)
# Bg= np.zeros((h,w,3),dtype=np.uint8)
# PlayerY
pw=10
ph=80
pc=(200,0,150)
pX1=(0,int(h/2-ph/2))
pX2=(pw,int(h/2+ph/2))

ballC=(200,200,200)
ballPos=[int(w/2),int (h/2)]
Crad=10
ballVx=5
ballVy=5
ypos=h/2


while True:
    success,frame= cap.read()
    frame=cv.flip(frame,1)
    hand, frame= detector.findHands(frame,draw=True)
    if hand:
        landmark=hand[0]['lmList']
        ypos=landmark[9][1]
        # print(ypos)
        if ypos-ph/2<0:
            ypos=ph/2
        if ypos+ph/2>h:
            ypos=h-ph/2 
        pX1=(0,int(ypos-ph/2))
        pX2=(pw,int(ypos+ph/2))

    cv.rectangle(frame,pX1,pX2,pc,cv.FILLED)
    cv.circle(frame,(ballPos),Crad,ballC,cv.FILLED)
    ballPos[0]+=ballVx
    ballPos[1]+=ballVy
    if ballPos[0]+Crad>w or ballPos[0]-Crad<0:
        ballVx*=-1
    if ballPos[1]+Crad>h or ballPos[1]-Crad<0:
        ballVy*=-1    
    
    if ballPos[0]-Crad<=pw and ballPos[1]>ypos-ph/2 and ballPos[1]<ypos+ph/2:
        ballVx*=-1


    cv.imshow("pong",frame)
    # cv.imshow("bg",Bg)
    if cv.waitKey(1) & 0xFF==27:
        break

    
    
cap.release()
cv.destroyAllWindows()