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
source=img3
bg=np.zeros(source.shape[:2],dtype='uint8')                  #BG DIMENSIONS MUST BE SAME SIZE OF THE IMAGE
blank=np.zeros((700,700,3),dtype='uint8')
# c1=blank.copy()
# c1[:]=0,0,241
# cv.imshow("blue",c1)
rectangle= cv.rectangle(bg.copy(),(100,100),(300,300),255,-1)
circle=cv.circle(bg.copy(),(bg.shape[1]//2,bg.shape[0]//2),100,255,-1)

# cv.imshow("CIRCLE",circle)   
# cv.imshow("RECTANGEL",rectangle)

weired_Shape= cv.bitwise_and(circle,rectangle)
# cv.imshow("WEIRED SHAPE",weired_Shape)

maskImg= cv.bitwise_and(source,source,mask=weired_Shape)
# cv.imshow("MASKED IMAGE",maskImg)

#    HISTOGRAM

source=img2
cv.imshow("image",source)

histogram1= cv.calcHist([source],[0],None,[256],[0,256])
histogram2= cv.calcHist([source],[1],None,[256],[0,256])
histogram3= cv.calcHist([source],[2],None,[256],[0,256])

# imshow

# print(histogram)
plt.figure()
plt.title("HISTOGRAM")
plt.xlabel("BINS")
plt.xlim([0,256])
plt.ylabel( "#PIXCLE")
plt.plot(histogram1,color = 'blue')
plt.plot(histogram2,color = 'green')
plt.plot(histogram3,color = 'red')
plt.show()

cv.waitKey(0)