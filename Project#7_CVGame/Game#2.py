import numpy as np
import cv2 as cv
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap=cv.VideoCapture(0)
h=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
w=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(h,w)
score=0

detector=HandDetector(detectionCon=0.8,maxHands=1)
# Bg= np.zeros((h,w,3),dtype=np.uint8)
#Player
pw=10
ph=80
pc=(200,0,150)
pX1=(0,int(h/2-ph/2))
pX2=(pw,int(h/2+ph/2))
#opponent
Ow=10
Oh=80
Oc=(200,150,10)
Otop=0
Obottom=Otop+Oh
OpX1=(w-Ow,int(Otop))
OpX2=(w,int(Obottom))


ballC=(200,200,200)
ballC2=(0,0,0)
ballPos=[int(w/2),int (h/2)]
Crad=10
Crad2=10
ballVx=10
ballVy=10
ypos=h/2


while True:
    success,frame= cap.read()
    frame=cv.flip(frame,1)
    hand, frame= detector.findHands(frame,draw=False)
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


    ballPos[0]+=ballVx
    ballPos[1]+=ballVy
    if ballPos[0]+Crad>w or ballPos[0]-Crad<0:
        ballVx*=-1
    if ballPos[1]+Crad>h or ballPos[1]-Crad<0:
        ballVy*=-1    
    #ball-plalyer Collission
    if ballPos[0]-Crad<=pw+2 and ballPos[1]>ypos-ph/2 and ballPos[1]<ypos+ph/2:
        ballVx*=-1
        score+=1
    
    if ballPos[0]-Crad<=-1 or ballPos[0]+Crad>w+1:
        ballPos[0]=w//2
        ballPos[1]=h//2
    
    
    #opponent
    if ballPos[0]>w/2:

        if ballPos[1]-Crad<Otop:
            Otop-=abs(ballVy)*2
            
        elif ballPos[1]+Crad>Obottom:
            Otop+=abs(ballVy)*2

        if Otop>h-Oh:
            Otop=h-Oh
        if Otop<0:
            Otop=0
    OpX1=(w-Ow,int(Otop))
    Obottom=Otop+Oh
    OpX2=(w,int(Obottom)) 
    if ballPos[0]+Crad>=w-Ow-2 and ballPos[1]>Otop and ballPos[1]<Obottom:
        ballVx*=-1

    #rendering Objects
    cv.rectangle(frame,pX1,pX2,pc,cv.FILLED)
    cv.rectangle(frame,OpX1,OpX2,Oc,cv.FILLED)
    cv.circle(frame,(ballPos),Crad,ballC,cv.FILLED)
    cv.circle(frame,(ballPos),Crad2,ballC2,2)
    cvzone.putTextRect(frame,"Score: "+str(score),(w//2-100,50),3,3,(255,255,255),(0,200,0))

    cv.imshow("pong",frame)
    # cv.imshow("bg",Bg)
    if cv.waitKey(1) & 0xFF==27:
        break
    


print (f'your Score : {score}')
cap.release()
cv.destroyAllWindows()