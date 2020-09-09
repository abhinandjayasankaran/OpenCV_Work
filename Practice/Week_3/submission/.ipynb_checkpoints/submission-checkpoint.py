import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

DATA_PATH = os.getcwd()

imgPath = DATA_PATH + "/data/sample.jpg"

img = cv2.imread(imgPath)  #Reading Image
imgCopy = img.copy()       #Creating a copy image

global scaleFactor, scaleType, maxScaleValue, maxScaleType, scaledImg

scaleType = 0
scaleFactor = 1
maxScaleValue = 100
maxScaleType = 1

scaledImg = img.copy()


def resizeImg(*args):
    
    scaleFactor=1
    
    if scaleType == 0:
    
        scaleFactor = 1 + (args[0]/100)
        scaledImg=cv2.resize(img, None, fx=scaleFactor, fy=scaleFactor, interpolation = cv2.INTER_LINEAR)
        cv2.imshow("Resize Image", scaledImg)
    
    elif scaleType == 1:
        
        scaleFactor = 1-(args[0]/100)
        
        if args[0] == 100:
            scaleFactor = 1 - (99/100)
        
        scaledImg=cv2.resize(img, None, fx=scaleFactor, fy=scaleFactor, interpolation = cv2.INTER_LINEAR)
        cv2.imshow("Resize Image", scaledImg)
    
    
def resizeScaleType(*args):
    
    global scaleType
    
    scaleFactor = 1
    
    scaleType = args[0]
    
    cv2.setTrackbarPos("Resize Scale %", "Resize Trackbar", 0)


cv2.namedWindow("Resize Image")
cv2.namedWindow("Resize Trackbar")
cv2.createTrackbar("Resize Scale %", "Resize Trackbar", scaleFactor, maxScaleValue, resizeImg)
cv2.createTrackbar("Scale Up/Down(0/1)", "Resize Trackbar", scaleType, maxScaleType, resizeScaleType)

cv2.imshow("Resize Image", scaledImg)

c = cv2.waitKey(0)

cv2.destroyAllWindows()
exit()