import cv2 as cv
import numpy as np
import functions as f

'''Test Images'''
img1=f.rescale(cv.imread("Test_Imges/AtomicHabbits.jpg"),0.2)
img2=f.rescale(cv.imread("Test_Imges/notes.jpg"),0.2)
img3=cv.imread("Test_Imges/FRAME.png")

'''Code Starts'''

TestImg=img3
# print (TestImg.shape[:2])
f.init_Trackbar()

'''PreProcess'''
gray= f.grayImg(TestImg)

while True:
    TrackVals=f.GetValTrackBars()
    # print(TrackVals)
    blur=f.G_blur(gray,2,TrackVals[2])
    # blur=f.G_blur(gray,2,2)
    # adaptiveThreshIMG=cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,3,3)
    canny=f.canny(blur,TrackVals[0],TrackVals[1])
    # canny=f.canny(blur,130,105)
    imgDialate=cv.dilate(canny,(5,5),5)
    # imgErode=cv.erode(imgDialate,(5,5),1)
    # cv.imshow("Post_processed_Image",imgErode)
    # cv.imshow("testImg",canny)
    contour,hairarchie= cv.findContours(imgDialate,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # blackBg=np.zeros(source.shape[:2],dtype='uint8')
    Doc_shape=cv.drawContours(TestImg.copy(),contour,-1,255,1)
    cv.imshow("contours",Doc_shape)
    # print(f'{len(contour)} countour(s)')
#130,105,2
    biggestContour=f.biggest_Contour_Point(contour)
    print (biggestContour)

    # output=img2.copy()
    if len(contour)!=0:
        output=cv.drawContours(TestImg.copy(),biggestContour,-1,(0,0,255),10)
        cv.imshow("Corner_Points",output)
    # else: print("none")

    # height,width=(TestImg.shape[0],int(TestImg.shape[1]))
    # pointTable1=np.float32(biggestContour)
    # pointTable2=np.float32([[0,0],[0,height],[width,height],[width,0]])
    # matrix= cv.getPerspectiveTransform(pointTable1,pointTable2)
    # warpimg= cv.warpPerspective(TestImg,matrix,(width,height))
    # cv.imshow("output",warpimg)
    

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    


