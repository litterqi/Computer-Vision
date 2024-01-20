import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../kaggle/wallpaper2.jpg')

cv.imshow("blue",img[:, :, 0])
cv.imshow("green",img[:, :, 1])
cv.imshow("red",img[:, :, 2])
cv.waitKey()

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey()