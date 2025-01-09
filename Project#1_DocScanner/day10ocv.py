import cv2 as cv
import numpy as np
import functions as f


img1=f.rescale(cv.imread("Test_Imges/AtomicHabbits.jpg"),0.2)
img2=f.rescale(cv.imread("Test_Imges/notes.jpg"),0.2)
img3=f.rescale(cv.imread("Test_Imges/Trimmer.jpg"),0.2)

f.init_Trackbar()
source=f.grayImg(img2)

print (source.shape[:2])
while True:
    TrackVals=f.GetValTrackBars()
    # print(TrackVals)
    TestIMG=f.G_blur(source,2,TrackVals[2])
    canny=f.canny(TestIMG,TrackVals[0],TrackVals[1])
    imgDialate=cv.dilate(canny,(5,5),2)
    imgErode=cv.erode(imgDialate,(5,5),1)
    cv.imshow("ProcessIMG",imgErode)
    # cv.imshow("testImg",canny)
    contour,hairarchie= cv.findContours(imgErode,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    blackBg=np.zeros(source.shape[:2],dtype='uint8')
    cv.drawContours(blackBg,contour,-1,255,1)
    cv.imshow("contours",blackBg)
    print(f'{len(contour)} countour(s)')
    biggestContour=f.biggest_Contour_Point(contour)
    # print (biggestContour)

    output=img2.copy()
    if len(contour)!=0:
        output=cv.drawContours(output,biggestContour,-1,(0,0,255),10)
        cv.imshow("OutputTest",output)
    # else: print("none")
    
    

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    


