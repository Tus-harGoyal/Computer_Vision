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

# --------------

#objects

orgimg= cv.imread("resources/logo.jpg")
img= rescaleFrame(orgimg,0.5)
img2= cv.imread("resources/book.png")
video = cv.VideoCapture("resources/video.mp4")
bg=np.zeros((512,512,3),np.uint8)

# --------

# cv.imshow("translated image",translate(img,50,50))
rotimg=rotation(img,45,(img.shape[1]//2,img.shape[0]//2))
# cv.imshow("rotated image",rotimg)
cannyimage=cv.Canny(rotimg,50,50)
# cv.imshow("cannyRotated",cannyimage)
flipimage=cv.flip(rotimg,1)
# cv.imshow("flipimage",flipimage)
cv.imshow("greyimg",cv.cvtColor(flipimage,cv.COLOR_BGR2GRAY))
cv.waitKey(0)