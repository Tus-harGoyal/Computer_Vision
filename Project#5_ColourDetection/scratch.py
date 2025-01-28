import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("hsv")
cv.createTrackbar("h","hsv",0,180,nothing)
cv.createTrackbar("s","hsv",0,255,nothing)
cv.createTrackbar("v","hsv",0,255,nothing)

img_hsv=np.zeros((500,400,3),dtype=np.uint8)

while True:
    h=cv.getTrackbarPos("h","hsv")
    s=cv.getTrackbarPos("s","hsv")
    v=cv.getTrackbarPos("v","hsv")

    img_hsv[:]=(h,s,v)
    img_Bgr=cv.cvtColor(img_hsv,cv.COLOR_HSV2BGR)
    cv.imshow("colour",img_Bgr)
    if cv.waitKey(1) & 0XFF==27:
        break