import cv2 as cv
import numpy as np
import cvzone

capture=cv.VideoCapture(0)
capture.set(cv.CAP_PROP_BRIGHTNESS,0.5)

#testColours
lowerOrange=np.array([7,66,255])
upperOrange=np.array([22,97,255])
upper_PurplePen=np.array([124,169,126])
lower_PurplePen=np.array([118,132,77])
cap_lower=np.array([105,46,16])
cap_upper=np.array([130,179,40])
upper_face=np.array([15,133,211])
lower_face=np.array([4,36,64])
lower_blueDiary=np.array([104,92,53])
upper_blueDiary=np.array([114,141,104])
minRed=np.array([0,152,226])
maxBlue=np.array([101,255,255])
minBlue=np.array([95,191,254])
maxRed=np.array([179,245,255])
BGRorange=(100,165,255)
BGRskinColor=(90,100,140)
BGRDiary=(102,74,56)
BGR_BLACK=(0,0,0)
maxh=0
maxs=0
maxv=0
minh=255
mins=255
minv=255




def detect_color(mask,colorCode,ColorName,mode):
    contour,heir= cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    if len(contour)!=0:
        for i in contour:
            area=cv.contourArea(i)
            peri=cv.arcLength(i,True)
            if (area >3000) and peri>10:
                x,y,w,h=cv.boundingRect(i)
                # aprox=cv.approxPolyDP(i,0.07*peri,True)
                if mode=="rect":

                    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv.circle(frame,(x,y),5,(255,255,255),cv.FILLED)
                    cv.circle(frame,(x+w,y),5,(255,255,255),cv.FILLED)
                    cv.circle(frame,(x,y+h),5,(255,255,255),cv.FILLED)
                    cv.circle(frame,(x+w,y+h),5,(255,255,255),cv.FILLED)
                    cvzone.putTextRect(frame,f'{ColorName}',(x+w//4,y-30),2,2,(255,255,255),colorCode)

                if mode=="point":
                    cvzone.putTextRect(frame,f'{ColorName}',(x+w//2,y-30+h//2),2,2,(255,255,255),colorCode)
                    cv.circle(frame,(x+w//2,y+h//2),8,colorCode,cv.FILLED)



while True: 


    Success, frame= capture.read()
    frame=cv.flip(frame,1)
    cx,cy=int(frame.shape[1]//2),int(frame.shape[0]//2)
    blur=cv.GaussianBlur(frame,(3,3),5)
    hsvimg=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    # cv.circle(frame,(cx,cy),5,(255,0,0),3)
    pixcel_center=frame[cy,cx]
    # print(pixcel_center)
    bgr= pixcel_center.reshape(1,1,3)
    hsvpixcel=cv.cvtColor(bgr,cv.COLOR_BGR2HSV)

    # if maxh<hsvpixcel[0][0][0]:
    #     maxh=hsvpixcel[0][0][0]
    # if maxs<hsvpixcel[0][0][1]:
    #     maxs=hsvpixcel[0][0][1]
    # if maxv<hsvpixcel[0][0][2]:
    #     maxv=hsvpixcel[0][0][2]
    # if minh>hsvpixcel[0][0][0]:
    #     minh=hsvpixcel[0][0][0]
    # if mins>hsvpixcel[0][0][1]:
    #     mins=hsvpixcel[0][0][1]
    # if minv>hsvpixcel[0][0][2]:
    #     minv=hsvpixcel[0][0][2]
    # print(f'max(hsv)= {maxh},{maxs},{maxv}')
    # print(f'min(hsv)= {minh},{mins},{minv}')
    if cv.waitKey(1) & 0xFF == ord('q'):
        maxh=0
        maxs=0
        maxv=0
        minh=255
        mins=255
        minv=255
        
    
    # mask1=cv.inRange(hsvimg,lower_face,upper_face)
    # mask2=cv.inRange(hsvimg,lowerOrange,upperOrange)
    # mask3=cv.inRange(hsvimg,minRed,maxRed)
    # mask4=cv.inRange(hsvimg,minBlue,maxBlue)
    mask5=cv.inRange(hsvimg,lower_blueDiary,upper_blueDiary)
    # cv.imshow("hsv",cv.resize(hsvimg,(400,300)))
    cv.imshow("mask",cv.resize(mask5,(400,300)))
    # # cv.imshow("mask2",mask2)

    # detect_color(mask1,BGRskinColor,"skin",mode="rect")
    # detect_color(mask2,BGRorange,"orange",mode="rect")
    detect_color(mask5,BGRDiary,"Diary",mode="point")

    cv.imshow("Img",frame)

    if cv.waitKey(1) & 0XFF==27:
        break

# print(frame[cy,cx])
# cv.waitKey(0)
capture.release()
cv.destroyAllWindows()

