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

orgimg= cv.imread("resources/logo.jpg")
# print (orgimg)
img= rescaleFrame(orgimg,0.5)
img2= rescaleFrame(cv.imread("resources/book.png"),0.5)
img3= rescaleFrame(cv.imread("resources/Shapes.png"),0.5)
video = cv.VideoCapture("resources/video.mp4")
img4= rescaleFrame(cv.imread("resources/graySnake.png"),0.7)
img5=rescaleFrame(cv.imread("resources/jamesClear.png"),0.5)
img6=rescaleFrame(cv.imread("resources/me.png"),0.2)
img7=rescaleFrame(cv.imread("resources/landscape.png"),0.5)   
img8=cv.imread("resources/faces.png")  
img10=rescaleFrame(cv.imread("resources/groupOfPeople.png"),0.8)   
                                         
# print(bg2.shape)
#  ------------------
source=greyimg(img10)
# cv.imshow("source",source)
## Edge Detection 2 (its prety good!)

laplacian= cv.Laplacian(source,cv.CV_64F)
laplacian=np.uint8(np.absolute(laplacian))
# cv.imshow("laplacian",laplacian)

##Canny edge detection

cannyEdge=canny(source,50,50)
# cv.imshow("canny Edge Detection",cannyEdge)

#Trial
adaptiveThreshIMG=cv.adaptiveThreshold(source,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,16)
cannyAThrIMG=canny(adaptiveThreshIMG,50,50)
# cv.imshow("EXP",cannyAThrIMG)

cannyLap=canny(laplacian,100,100)
# cv.imshow("CannyLAp",cannyLap)

# Sobel

Sobelx=cv.Sobel(source,cv.CV_64F,1,0)
Sobely=cv.Sobel(source,cv.CV_64F,0,1)
# cv.imshow("sovelx",Sobelx)
# cv.imshow("sobely",Sobely)
Sobelxy=cv.Sobel(source,cv.CV_64F,1,1)
# cv.imshow("sobelxy",Sobelxy)
# cv.imshow("combined",cv.bitwise_or(Sobelx,Sobely))

#Haars Cascade Face detection
source2=img10
haars_cascade= cv.CascadeClassifier('resources\haar_face.xml')
face_rect= haars_cascade.detectMultiScale(source2,scaleFactor=1.2,minNeighbors=4)
print(f'{len(face_rect)} face(s) detected')
for (x,y,h,k) in face_rect:
    cv.rectangle(source2,(x,y),(x+h,y+k),(255,255,0),2)
cv.imshow("Faces",rescaleFrame(source2,0.5))


cv.waitKey(0)
