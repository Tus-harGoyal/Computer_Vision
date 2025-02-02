import numpy as np
import cv2 as cv
import easyocr
import os
import cvzone


def detectTxt(path,thresh):
    filename_with_ext = os.path.basename(path)
    filename, ext = os.path.splitext(filename_with_ext)
    image=cv.imread(path)
    image=cv.resize(image,(800,1000),interpolation=cv.INTER_CUBIC)
    
    reader= easyocr.Reader(['en'],gpu=False)
    text=reader.readtext(image)
    for t in text:
        box,txt,score=t 
        points=np.array(box,np.int32)
        pts=points.reshape((-1, 1, 2))
        print (f'text= {txt}, box={box}')
        if score>thresh:
            cv.polylines(image,[pts],True,(0,255,0),1)
            cvzone.putTextRect(image,txt,(int(box[0][0]),int(box[0][1])),1,1,(255,255,255),(200,100,255))

    cv.imshow(f'{filename}',cv.resize(image,(600,800)))
    


path=r'C:\Users\Tusha\ComputerVision\Project#6_TextDetection\TestImg\img1.png'
path2=r'C:\Users\Tusha\ComputerVision\Project#6_TextDetection\TestImg\img2.png'
path3=r"C:\Users\Tusha\Downloads\tst1.jpg"
path4=r"C:\Users\Tusha\Downloads\tst2.jpg"  

detectTxt(path3,0.3)
detectTxt(path4,0.3)

cv.waitKey(0)
cv.destroyAllWindows()