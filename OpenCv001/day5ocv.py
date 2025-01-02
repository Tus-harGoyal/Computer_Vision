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
# --------------

#objects

orgimg= cv.imread("resources/book.png")
# print (orgimg)
img= rescaleFrame(orgimg,0.5)
img2= greyimg(rescaleFrame(cv.imread("resources/book.png"),0.5))
img3= rescaleFrame(cv.imread("resources/Shapes.png"),0.5)
video = cv.VideoCapture("resources/video.mp4")
bg1=np.ones((img2.shape[0],img2.shape[1],3),np.uint8)
bg2=np.zeros((img2.shape[0],img2.shape[1],3),np.uint8)
img4= rescaleFrame(cv.imread("resources/graySnake.png"),0.4)
img5=rescaleFrame(cv.imread("resources/jamesClear.png"),0.5)
img6=rescaleFrame(cv.imread("resources/me.png"),0.2)
img7=rescaleFrame(cv.imread("resources/landscape.png"),0.5)
cv.imshow("ls",medianBlur(img7,3))                                                          

#  -------------------
source=img7
print (source.shape)
# cv.imshow("snake",source)
# BGRimg=cv.cvtColor(source,cv.COLOR_GRAY2BGR)
# cv.imshow("snakeColoured",BGRimg)
# a=250
# bg1[:]=[a,a,a]

# cv.imshow("background",bg1)
colorized = cv.cvtColor(source,cv.COLOR_BGR2HSV)
colorized2 = cv.applyColorMap(source, cv.COLORMAP_TURBO)
colorized3= cv.applyColorMap(source, cv.COLORMAP_AUTUMN)
colorized4 = cv.applyColorMap(source, cv.COLORMAP_BONE)
colorized5 = cv.applyColorMap(source, cv.COLORMAP_CIVIDIS)
colorized6 = cv.applyColorMap(source, cv.COLORMAP_COOL)
colorized7 = cv.applyColorMap(source, cv.COLORMAP_HOT)
colorized8=cv.applyColorMap(img5,cv.COLORMAP_CIVIDIS)
# cv.imshow('Colorized', colorized)
# cv.imshow('2', colorized2)
# cv.imshow('3', colorized3)
# cv.imshow('4', colorized4)
# cv.imshow('5', colorized5)
# cv.imwrite("outputs/myImg.png",colorized5)
# cv.imshow('6', colorized6)
# cv.imshow('7', colorized7)
# cv.imshow('James', colorized8)

b,g,r = cv.split(source)     #bgr Intensity maps
# cv.imshow("b",b)
# cv.imshow("g",g)
# cv.imshow("r",r)

# cv.imshow("merged",cv.merge([b,g,r]))        #merges b,g,r according to respective intensity maps
# cv.imshow("inversemerged",cv.merge([r,g,b]))
cv.waitKey(0)

