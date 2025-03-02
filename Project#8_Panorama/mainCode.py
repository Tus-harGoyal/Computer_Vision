import cv2 as cv
import numpy as np
import os

MF='Resource'
save_Location=r'C:\Users\Tusha\ComputerVision\Project#8_Panorama\Output'
myF=os.listdir(MF)


for folder in myF:

     path=MF+'/'+folder
     list=os.listdir(path)
     imageArray=[]
     i=0
     for images in list:
          imgread= cv.imread(f'{path}/{images}')
          imgread=cv.resize(imgread,(500,500))
          imageArray.append(imgread)
          cv.imshow(f'{i}',imageArray[i])
          cv.imshow
          i+=1
     print(f'{len(imageArray)} image(s) found')
     stitcher=cv.Stitcher.create()
     (status,result)=stitcher.stitch(imageArray)
     if status==cv.STITCHER_OK:
          print("generate done")
          cv.imshow(folder+' result',result)
          cv.waitKey(1)
     else:
          print("not generated")
     cv.waitKey(0)
     cv.destroyAllWindows()
     print(save_Location+'/'+folder+'_result'+'.jpg')
     save=int (input("wanna save?"))
     if save ==1:   
          cv.imwrite(save_Location+'/'+folder+'_result'+'.jpg',result)

          print("result saved")

# img=cv.imread(f'{path}')
# cv.imshow("img",img)
cv.waitKey(0)