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

def greyimg(frame):
    return cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
# --------------

#objects

orgimg= cv.imread("resources/book.png")
# print (orgimg)
img= rescaleFrame(orgimg,0.5)
img2= greyimg(rescaleFrame(cv.imread("resources/book.png"),0.5))
img3= rescaleFrame(cv.imread("resources/Shapes.png"),0.5)
video = cv.VideoCapture("resources/video.mp4")
bg1=np.zeros((img2.shape[0],img2.shape[1],3),np.uint8)
bg2=np.zeros((img2.shape[0],img2.shape[1],3),np.uint8)


# --------


# cv.imshow("cannyimg",canny(img2,50,50))
# cv.imshow("blurop",canny(GausBlur(img2,1,1,10),50,150))

# contour Detection
sourceImg= GausBlur(img2,3,3,0)
ret,thresh= cv.threshold(sourceImg,175,255,cv.THRESH_BINARY)
cv.imshow("threshIMG",thresh)
contour1, hierarchie1 =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'c,h(thresh)= {len(contour1)},{len(hierarchie1)}')
contour2, hierarchie2 =cv.findContours(canny(sourceImg,100,700),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'c,h (canny)= {len(contour2)},{len(hierarchie2)}')
# print(contour)
cv.drawContours(bg1,contour1,-1,(255,255,0),2)
cv.drawContours(bg2,contour2,-1,(0,255,0),2)
cv.imshow("contourThresh",bg1)
cv.imshow("contourCanny",bg2)
cv.imshow("canny",canny(sourceImg,70,70))

cv.waitKey(0)