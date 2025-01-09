import cv2 as cv
import numpy as np
import functions as f


img1=f.rescale(cv.imread("Test_Imges/AtomicHabbits.jpg"),0.2)
img2=f.rescale(cv.imread("Test_Imges/notes.jpg"),0.2)
img3=f.rescale(cv.imread("Test_Imges/Trimmer.jpg"),0.2)

f.init_Trackbar()
source=f.grayImg(img1)

print (source.shape[:2])
while True:
    TrackVals=f.GetValTrackBars()
    # print(TrackVals)
    TestIMG=f.G_blur(source,2,TrackVals[2])
    canny=f.canny(TestIMG,TrackVals[0],TrackVals[1])
    cv.imshow("ProcessIMG",TestIMG)
    cv.imshow("testImg",canny)
    contour,hairarchie= cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    blackBg=np.zeros(source.shape[:2],dtype='uint8')
    cv.drawContours(blackBg,contour,-1,255,1)
    cv.imshow("contours",blackBg)
    print(f'{len(contour)} countour(s)')

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    


