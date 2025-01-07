import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Functions

def rescaleFrame(frame,scale):
    height= int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension)

def translate(frame,x,y):
    dimension=(frame.shape[1],frame.shape[0])
    translateMatrix=np.float32([[1,0,x],[0,1,y]])
    return cv.warpAffine(frame,translateMatrix,dimension)

def rotation(frame,angle,point):
    (height,widht)=frame.shape[:2]
    rotMatrix=cv.getRotationMatrix2D(point,angle,1.0)
    dimension=(widht,height)
    return  cv.warpAffine(frame,rotMatrix,dimension)

def canny(frame,th1,th2):
    return cv.Canny(frame,th1,th2)

def GausBlur(frame,x,y,z):
    return cv.GaussianBlur(frame,(x,y),z)

def medianBlur(frame,x):
    return cv.medianBlur(frame,x)                  #good for removing noise

def greyimg(frame):
    return cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

def BITsubtract(frame1,frame2):
    return cv.bitwise_and(cv.bitwise_not(frame2),frame1)    # A-B= A^(B')


# --------------

#objects

orgimg= cv.imread("resources/book.png")
# print (orgimg)
img= rescaleFrame(orgimg,0.5)
img2= rescaleFrame(cv.imread("resources/book.png"),0.5)
img3= rescaleFrame(cv.imread("resources/Shapes.png"),0.5)
video = cv.VideoCapture("resources/video.mp4")
img4= rescaleFrame(cv.imread("resources/graySnake.png"),0.4)
img5=rescaleFrame(cv.imread("resources/jamesClear.png"),0.5)
img6=rescaleFrame(cv.imread("resources/me.png"),0.2)
img7=rescaleFrame(cv.imread("resources/landscape.png"),0.5)                                               
# print(bg2.shape)
#  -------------------
source=rescaleFrame(greyimg(img4),0.5)

threshold,threshImg= cv.threshold(source,100,255,cv.THRESH_BINARY)
# print(thresh)
print (threshold)
# cv.imshow("threshIMG",threshImg)

#Adaptive Threshold
                                                                                     # (kernalSize,C_Val)
adaptiveThreshIMG1= cv.adaptiveThreshold(source,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,10)
cv.imshow("ATh_IMG1",adaptiveThreshIMG1)
adaptiveThreshIMG2= cv.adaptiveThreshold(source,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,15)
cv.imshow("ATh_IMG2",adaptiveThreshIMG2)
adaptiveThreshIMG3= cv.adaptiveThreshold(source,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,9,10)
cv.imshow("ATh_IMG3",adaptiveThreshIMG3)
adaptiveThreshIMG4= cv.adaptiveThreshold(source,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,9,15)
cv.imshow("ATh_IMG4",adaptiveThreshIMG4)
adaptiveThreshIMG5= cv.adaptiveThreshold(source,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,5,10)
cv.imshow("ATh_IMG5",adaptiveThreshIMG5)
adaptiveThreshIMG6= cv.adaptiveThreshold(source,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,5,15)
cv.imshow("ATh_IMG6",adaptiveThreshIMG6)

## more Kernal size makes boundaries thinnner, while more C_Val reduces point chunks and noise


cv.waitKey(0)