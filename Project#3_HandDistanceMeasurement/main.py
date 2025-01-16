import cv2 as cv
from cvzone.HandTrackingModule import HandDetector


cap= cv.VideoCapture(0)
cap.set(3,500)
cap.set(4,600)

detector = HandDetector(detectionCon=0.8,maxHands=1)

while True:
    Success, frame= cap.read()
    hand, frame= detector.findHands(frame)
    cv.imshow("video",frame)
    if cv.waitKey(1) & 0XFF==27 :
        break
    
    