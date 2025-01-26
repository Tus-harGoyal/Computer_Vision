import cv2 as cv
import numpy as np

capture=cv.VideoCapture(0)

lower=np.array([15,150,20])
upper=np.array([35,255,255])


while True: 
    Success, frame= capture.read()
    frame=cv.flip(frame,1)
    blur=cv.GaussianBlur(frame,(3,3),5)
    hsvimg=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    
    mask=cv.inRange(hsvimg,lower,upper)
    cv.imshow("hsv",hsvimg)
    cv.imshow("mask",mask)
    contour,heir= cv.findContours(mask,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    bigC=np.array([[0,0],[100,0],[100,100],[0,100]])
    if len(contour)!=0:
        for i in contour:
            area=cv.contourArea(i)
            peri=cv.arcLength(i,True)
            if (area >1000) and peri>10:
                x,y,w,h=cv.boundingRect(i)
                aprox=cv.approxPolyDP(i,0.07*peri,True)
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
                if (len(aprox)==4):
                    cv.polylines(frame,[aprox],True,(0,255,0),1)


    
    # contour,hairarhcie= cv.findContours(mask,)
    cv.imshow("Img",frame)

    if cv.waitKey(1) & 0XFF==27:
        break
capture.release()
cv.destroyAllWindows()

