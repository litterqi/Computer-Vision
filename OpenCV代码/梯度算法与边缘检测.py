import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../kaggle/wallpaper2.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny=cv.Canny(gray,100,200)

cv.imshow("canny",canny)
cv.waitKey()