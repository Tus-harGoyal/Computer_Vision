import cv2
import numpy as np

# Functions

def rescaleFrame(frame,scale):
    height= int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimension=(width,height)
    return cv2.resize(frame,dimension)

# --------------

#objects

# orgimg= cv2.imread("resources/logo.jpg")
# img= rescaleFrame(orgimg,0.5)
img2= cv2.imread("C: \Users \Tusha \ComputerVision")
video = cv2.VideoCapture("resources/video.mp4")
bg=np.zeros((512,512,3),np.uint8)

#----------------

# print(orgimg.shape)
# print(img.shape)

# while True:
#     success, frame= video.read()
#     rescale_frame= rescaleFrame(frame,0.25)
#     cv2.imshow("video", frame)
#     cv2.imshow("video2", rescale_frame)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
# cv2.imshow("orgimg",orgimg)
# cv2.imshow("img",img)
# cv2.imshow("op",img)
scale=0.5
width,height=int(img2.shape[0]*scale),int(img2.shape[1]*scale)
pointTable1=np.float32([[482, 226],[981, 203],[979, 852],[478, 903]])
pointTable2=np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix= cv2.getPerspectiveTransform(pointTable1,pointTable2)
warpimg= cv2.warpPerspective(img2,matrix,(width,height))
# cv2.imshow("output",warpimg)
# cv2.imshow("output2",rescaleFrame(img2,0.5))


bg[100:200,100:200]=255,255,0
cv2.line(bg,(0,0),(400,400),(255,200,100),5)
cv2.rectangle(bg,(300,300),(bg.shape[0],bg.shape[1]),(0,255,0),4)
cv2.putText(bg,"OpenCv",(300,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)

# camCapture= cv2.VideoCapture(0)
# while True:
#     success, frame= camCapture.read()
#     cv2.imshow("rescale video",rescaleFrame(frame,0.75))
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.imshow("bg",bg)
# print("h,w,c=", orgimg.shape)
cv2.imshow("opp",img2)
cv2.waitKey(0)

