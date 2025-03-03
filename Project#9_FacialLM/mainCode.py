import cv2 as cv
import numpy as np
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector\


cap=cv.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=1)
while True:
    success,frame= cap.read()
    frame=cv.flip(frame,1)
    frame,faces= detector.findFaceMesh(frame,draw=True)
    if faces:
        face=faces[0]
        point_Id=len(face)
        i=0
        while i<point_Id:
            # cv.putText(frame,f'{i}',(face[i][0]-10,face[i][1]-5),cv.FONT_HERSHEY_PLAIN,1,(0,255,0),1)

            i+=1
    cv.imshow("output",frame)

    if cv.waitKey(1) & 0xFF==27:
        break



