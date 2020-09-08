### Python Script for cropping image from given static image by selecting crop ara by drawing rectangle
### Author: Abhinand Jayasankaran

import cv2
import math
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import os

DATA_PATH = os.getcwd()

imgPath = DATA_PATH + "/data/sample.jpg"


img = cv2.imread(imgPath)
imgCopy = img.copy()

def drawBox(action,x,y,flags,userdata):
    
    global topLeftColumn, topLeftRow, bottomRightRow, bottomRightColumn
    
    
    if action == cv2.EVENT_LBUTTONDOWN:
        topLeftColumn,topLeftRow = (x,y)
        cv2.circle(img,(topLeftColumn,topLeftRow),1,(0,0,255),2,cv2.LINE_AA)
    elif action == cv2.EVENT_LBUTTONUP:
        bottomRightColumn, bottomRightRow = (x,y)
        cv2.rectangle(img,(topLeftColumn,topLeftRow),(bottomRightColumn,bottomRightRow),(0,0,255),2, cv2.LINE_AA)
        cv2.putText(img,"Enter y to crop and save or c=clear & retry...", (10,450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 )
        

cv2.namedWindow("Image_Window")
cv2.setMouseCallback("Image_Window",drawBox)



k=0

while k!=27:
    
    cv2.imshow("Image_Window",img)
    cv2.putText(img,"Pick point and drag(ESC=exit,c=clear)", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 )
    k = cv2.waitKey(1)
    
    if k==ord('c') or k==ord('C'):
        img = imgCopy.copy()
        
    elif k==ord('y') or k==ord('Y'):
        cropImg = imgCopy[topLeftRow:bottomRightRow,topLeftColumn:bottomRightColumn]
        cv2.imwrite("croppedImage.jpg",cropImg)
        break
        

cv2.destroyAllWindows()
exit()
        
