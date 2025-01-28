import cv2 as cv
import numpy as np

capture=cv.VideoCapture(0)

lowerOrange=np.array([11,195,90])
upperOrange=np.array([18,255,157])
upper_PurplePen=np.array([124,169,126])
lower_PurplePen=np.array([118,132,77])
upper_face=np.array([15,133,211])
lower_face=np.array([4,36,64])



maxh=0
maxs=0
maxv=0
minh=255
mins=255
minv=255
while True: 


    Success, frame= capture.read()
    frame=cv.flip(frame,1)
    cx,cy=int(frame.shape[1]//2),int(frame.shape[0]//2)
    blur=cv.GaussianBlur(frame,(3,3),5)
    hsvimg=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.circle(frame,(cx,cy),5,(255,0,0),3)
    pixcel_center=frame[cy,cx]
    bgr= pixcel_center.reshape(1,1,3)
    hsvpixcel=cv.cvtColor(bgr,cv.COLOR_BGR2HSV)
    

    # print("h",hsvpixcel[0][0][0])
    if maxh<hsvpixcel[0][0][0]:
        maxh=hsvpixcel[0][0][0]
    if maxs<hsvpixcel[0][0][1]:
        maxs=hsvpixcel[0][0][1]
    if maxv<hsvpixcel[0][0][2]:
        maxv=hsvpixcel[0][0][2]
    if minh>hsvpixcel[0][0][0]:
        minh=hsvpixcel[0][0][0]
    if mins>hsvpixcel[0][0][1]:
        mins=hsvpixcel[0][0][1]
    if minv>hsvpixcel[0][0][2]:
        minv=hsvpixcel[0][0][2]
    

    print(f'max(hsv)= {maxh},{maxs},{maxv}')
    print(f'min(hsv)= {minh},{mins},{minv}')

    
    mask=cv.inRange(hsvimg,lower_face,upper_face)
    # face("hsv",hsvimg)
    cv.imshow("mask",mask)
    contour,heir= cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    bigC=np.array([[0,0],[100,0],[100,100],[0,100]])
    if len(contour)!=0:
        for i in contour:
            area=cv.contourArea(i)
            peri=cv.arcLength(i,True)
            if (area >1000) and peri>10:
                x,y,w,h=cv.boundingRect(i)
                # aprox=cv.approxPolyDP(i,0.07*peri,True)
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
    #             if (len(aprox)==4):
    #                 cv.polylines(frame,[aprox],True,(0,255,0),1)


    
    # contour,hairarhcie= cv.findContours(mask,)
    cv.imshow("Img",frame)

    if cv.waitKey(1) & 0XFF==27:
        break
    if cv.waitKey(1) & 0xFF == ord('q'):
        maxh=0
        maxs=0
        maxv=0
        minh=255
        mins=255
        minv=255
        cv.waitKey(20)
capture.release()
cv.destroyAllWindows()

