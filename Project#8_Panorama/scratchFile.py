import cv2 as cv
import numpy as np
import os

MF='Project#8_Panorama\Resource'
myF=os.listdir(MF)

for folder in myF:
    path=MF+'/'+folder
    print(path)
img=cv.imread(path)
cv.imshow("img",img)
cv.waitKey(0)