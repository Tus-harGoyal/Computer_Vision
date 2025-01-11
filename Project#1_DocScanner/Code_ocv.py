import cv2 as cv
import numpy as np
import functions as f
from imutils.perspective import four_point_transform


'''Test Images'''
img1=f.rescale(cv.imread("Test_Imges/AtomicHabbits.jpg"),0.5)
img2=f.rescale(cv.imread("Test_Imges/notes.jpg"),0.5)
img3=cv.imread("Test_Imges/FRAME.png")
img4=f.rescale(cv.imread("Test_Imges/card.png"),0.5)
img5=f.rescale(cv.imread("Test_Imges/notes2.jpg"),0.8)

'''Var'''

TestImg=img4
HEIGHT=TestImg.shape[1]
WIDTH=TestImg.shape[0]
CAM=0

'''Code Starts'''

print (TestImg.shape[:2])
f.init_Trackbar()

'''PreProcess'''
gray= f.grayImg(TestImg)

while True:
    TrackVals=f.GetValTrackBars()
    blur=f.G_blur(gray,5,TrackVals)
    _,threshold=cv.threshold(blur,100,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
    # cv.imshow("threshimg",threshold)
    erode=cv.erode(threshold,np.ones((5,5),np.uint8),iterations=2)
    # cv.imshow("erode",erode)
    contours,_=cv.findContours(erode,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    cv.imshow("contours",f.rescale(cv.drawContours(TestImg.copy(),contours,-1,(0,0,255),10),0.2))
    contours=sorted(contours,key=cv.contourArea,reverse=True)
    doc_contour=f.biggest_Contour_Point(contours,WIDTH,HEIGHT)
    print (doc_contour.size)
    if doc_contour.size !=0:
        contourLine=cv.drawContours(TestImg.copy(),[doc_contour],-1,(0,255,0),10)
        cv.imshow("contour",f.rescale(contourLine,0.8))
    else: 
        print("contour not found")
    
    warped = four_point_transform(TestImg.copy(),doc_contour.reshape(4,2))
    cv.imshow("wraped",f.rescale(warped,0.8))
    
    if cv.waitKey(1) & 0XFF==27:
        break 
    


