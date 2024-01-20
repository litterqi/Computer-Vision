import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../kaggle/wallpaper2.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners=cv.goodFeaturesToTrack(gray,500,0.1,10)
for corner in corners:
    x, y =corner.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,255,0),-1)

cv.imshow("corners",img)
cv.waitKey()