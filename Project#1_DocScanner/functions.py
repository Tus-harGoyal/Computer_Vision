import cv2 as cv

def rescale(frame,factor):
    newDimensions=(int(frame.shape[1]*factor),int(frame.shape[0]*factor))
    return cv.resize(frame,newDimensions)

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
    cv.resizeWindow("cannyBars",300,300)
    cv.createTrackbar("T1","cannyBars",100,255,nothing)
    cv.createTrackbar("T2","cannyBars",100,255,nothing)
    cv.createTrackbar("G_Blur","cannyBars",1,15,nothing)
    

def GetValTrackBars():
    t1=cv.getTrackbarPos("T1","cannyBars")
    t2=cv.getTrackbarPos("T2","cannyBars")
    Iteratn=cv.getTrackbarPos("G_Blur","cannyBars")
    src=t1,t2,Iteratn
    return src