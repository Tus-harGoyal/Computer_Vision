import numpy as np
import cv2 as cv
import easyocr
import os
import cvzone


thresh=0.7
image=cv.imread(r'C:\Users\Tusha\ComputerVision\Project#6_TextDetection\TestImg\img1.png')
image=cv.resize(image,(500,600))
cv.imshow("image",image)
reader= easyocr.Reader(['en'],gpu=False)
text=reader.readtext(image)
for t in text:
    box,txt,score=t 
    points=np.array(box,np.int32)
    pts=points.reshape((-1, 1, 2))
    if score>thresh:
        cv.polylines(image,[pts],True,(0,255,0),1)
        cvzone.putTextRect(image,txt,(box[0][0]+10,box[0][1]-20),1,1,(255,255,255),(200,100,255))

cv.imshow("image",image)
cv.waitKey(0)
cv.destroyAllWindows()