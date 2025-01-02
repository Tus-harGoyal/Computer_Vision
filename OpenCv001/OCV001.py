import cv2
import numpy as np

oldimg = cv2.imread("resources/logo.jpg")
# print(oldimg.shape)
img= cv2.resize(oldimg,(500,600))
print(img.shape)
cropimg= img[100:500,100:400]
print(cropimg.shape)
cv2.imshow("output1",cropimg)
cv2.imshow("output2",img)

video = cv2.VideoCapture("resources/video.mp4")
kernal=np.ones((5,5),np.uint8)
# Functions
gryimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       #Greying
blrimg = cv2.GaussianBlur(gryimg,(15,15),0)         #bluring  * Blur values must be odd number
canyimg= cv2.Canny(img,50,50)                       #canning edge detection
dilimg = cv2.dilate(canyimg,kernal,iterations=2)
eroding= cv2.erode(dilimg,kernal,iterations=1)
# cv2.imshow("output1",eroding)
#
# cv2.imshow("output2",canyimg)
# canyimg= cv2.Canny(img,100,100)
# cv2.imshow("output2",canyimg)
# canyimg= cv2.Canny(img,150,150)
# cv2.imshow("output3",canyimg)
# cv2.imshow("output",img)
# cv2.imshow("output2",gryimg)



# cv2.imshow("output1",oldimg)
# cv2.imshow("output2",img)
# cap = cv2.VideoCapture(0)                         #video Capture cam
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
# while True:
#     Success, img= cap.read()
#     cv2.imshow("video",img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
cv2.waitKey(0)


