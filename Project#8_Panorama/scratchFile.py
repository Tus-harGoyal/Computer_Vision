import cv2 as cv
import numpy as np
import os

MF='Resource'
myF=os.listdir(MF)
print (myF)
for i in myF:
    path=MF+'/'+i
    list=os.listdir(path)  
    print(list) 
