import cv2 as cv
import numpy as np

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
img2= greyimg(rescaleFrame(cv.imread("resources/book.png"),0.5))
img3= rescaleFrame(cv.imread("resources/Shapes.png"),0.5)
video = cv.VideoCapture("resources/video.mp4")
bg1=np.ones((img2.shape[0],img2.shape[1],3),np.uint8)
bg2=np.zeros((img2.shape[0],img2.shape[1]),np.uint8)
img4= rescaleFrame(cv.imread("resources/graySnake.png"),0.4)
img5=rescaleFrame(cv.imread("resources/jamesClear.png"),0.5)
img6=rescaleFrame(cv.imread("resources/me.png"),0.2)
img7=rescaleFrame(cv.imread("resources/landscape.png"),0.5)
# cv.imshow("ls",bg2)                                                  
# print(bg2.shape)q
#  -------------------
source=img7

rectangle= cv.rectangle(bg2.copy(),(100,100),(400,400),255,-1)
circle=cv.circle(bg2.copy(),(bg2.shape[1]//2,bg2.shape[0]//2),200,255,-1)
# cv.imshow("rectangel",rectangle)
cv.imshow("circile",circle)
BitwishAND= cv.bitwise_and(rectangle,circle)
BitwiseOR=cv.bitwise_or(circle,rectangle)
bitwiseXOR=cv.bitwise_xor(circle,rectangle)
bitwiseNOT=cv.bitwise_not(circle)
bitwiseSUB=BITsubtract(circle,rectangle)
cv.imshow("BIT SUB",bitwiseSUB)

cv.waitKey(0)