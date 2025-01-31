import cv2 as cv
import numpy as np
import functions as f
import os
from imutils.perspective import four_point_transform


'''Test Images'''
img1=cv.imread("Test_Imges/AtomicHabbits.jpg")
img2=cv.imread("Test_Imges/notes.jpg")
img3=cv.imread("Test_Imges/FRAME.png")
img4=cv.imread("Test_Imges/card.png")
img5=cv.imread("Test_Imges/notes2.jpg")
image6=cv.imread(r'C:\Users\Tusha\Downloads\mouthwash.jpg')

'''Var'''
TestImgOriginal=img3
TestImg=cv.resize(TestImgOriginal,(1000,1000))
HEIGHT=TestImg.shape[0]
WIDTH=TestImg.shape[1]
HEIGHT_orig=TestImgOriginal.shape[0]
WIDTH_orig=TestImgOriginal.shape[1]



CAM=0

'''Code Starts'''

print (TestImg.shape[:2])
f.init_Trackbar()

'''PreProcess'''
gray= f.grayImg(TestImg)

while True:
    TrackVals=f.GetValTrackBars()
    '''Max_Area_Scale_Factor'''
    # Scale_Fac_Area=TrackVals[1]
    Scale_Fac_Area=25
 
    blur=f.G_blur(gray,5,TrackVals[0])
    _,threshold=cv.threshold(blur,TrackVals[2],TrackVals[3],cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imshow("threshimg",cv.resize(threshold,(300,300)))
    erode=cv.erode(threshold,np.ones((5,5),np.uint8),iterations=2)
    cv.imshow("erode",cv.resize(erode,(300,300)))
    contours,_=cv.findContours(erode,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    cv.imshow("contours",cv.resize(cv.drawContours(TestImg.copy(),contours,-1,(0,0,255),3),(300,300)))
    contours=sorted(contours,key=cv.contourArea,reverse=True)
    # contours_rescaled=cv.resize(contours())
    doc_contour,maxArea=f.biggest_Contour_Point(contours,WIDTH,HEIGHT,int(25000*int(Scale_Fac_Area)))
    # print (maxArea)
    if doc_contour.size !=0 :
        contourLine=cv.drawContours(TestImg.copy(),[doc_contour],-1,(0,255,0),3)
        cv.imshow("Biggest_contour",cv.resize(contourLine,(300,300)))
    else: 
        print("contour not found")
    
    warped = four_point_transform(TestImg.copy(),doc_contour.reshape(4,2))
    
    if cv.waitKey(1) & 0XFF==27:
        break 
cv.destroyAllWindows()
cv.imshow("wraped",warped)
cv.waitKey(0)
cv.destroyAllWindows()
save=int (input("wanna save?"))
if save ==1:
    print("saved")
    warp_Resized=cv.resize(warped,(WIDTH_orig,HEIGHT_orig),interpolation=cv.INTER_AREA)
    cv.imwrite("Saved_Images/outputFile5.png",warp_Resized) 

     
else :print("not saved")
