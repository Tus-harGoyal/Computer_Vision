import cv2 as cv
import numpy as np
def rescale(frame,factor):
    blurred_image = cv.GaussianBlur(frame, (5, 5), 0)
    newDimensions=(int(blurred_image.shape[1]*factor),int(blurred_image.shape[0]*factor))
    return cv.resize(frame,newDimensions,interpolation=cv.INTER_CUBIC)

def grayImg(frame):
    return cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

def Center_rotate(frame,angle):
    (h,w)=frame.shape[:2]
    dim=w,h
    point= (w//2,h//2)
    rotMat=cv.getRotationMatrix2D(point,angle,1.0)
    return cv.warpAffine(frame,rotMat,dim)
    
def canny (frame,t1,t2):
    return cv.Canny(frame,t1,t2)

def G_blur(frame,kernal,iteration):
    kernal=2*kernal+1
    return cv.GaussianBlur(frame,(kernal,kernal),iteration)

def nothing ():
    pass  #call back function

def init_Trackbar():
    cv.namedWindow("cannyBars")
    cv.resizeWindow("cannyBars",500,200)
    # cv.createTrackbar("minArea","cannyBars",50,1000,nothing)
    cv.createTrackbar("maxArea_Scale","cannyBars",0,30,nothing)
    cv.createTrackbar("G_Blur","cannyBars",5,15,nothing)
    cv.createTrackbar("Thresh1","cannyBars",0,125,nothing)
    cv.createTrackbar("Thresh2","cannyBars",0,125,nothing)
    

def GetValTrackBars():
    # minArea=cv.getTrackbarPos("minArea","cannyBars")
    maxArea_Scale=cv.getTrackbarPos("maxArea_Scale","cannyBars")
    Iteratn=cv.getTrackbarPos("G_Blur","cannyBars")
    threshold=cv.getTrackbarPos("Thresh1","cannyBars")
    threshold2=cv.getTrackbarPos("Thresh2","cannyBars")
    src=Iteratn,maxArea_Scale,threshold,threshold2
    return src

def biggest_Contour_Point(contours,width,height,maxArea):
    MaxArea=0
    biggestContour=np.array([[0,0],[width,0],[width,height],[0,height]])
    for i in contours:
        area=cv.contourArea(i)   #found area of i'th contour
        if area>50 and area<maxArea:   #filter small contours and noise
            perimeter=cv.arcLength(i,True)   #true means closed contour
            aprox=cv.approxPolyDP(i,0.02*perimeter,True)      #0.02*peri is Deviation allowed from original contour
            if area>MaxArea and len(aprox)==4:
                biggestContour=aprox
                MaxArea=area
            # else:
            #     # print("area greater than 50 doesnt exist")

        # else:
        #         # print("out of bound")

    return biggestContour,MaxArea
    