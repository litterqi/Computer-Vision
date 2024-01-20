import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

gray=cv.imread("../kaggle/opencv_logo.jpg",cv.IMREAD_GRAYSCALE)

_, binary =cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)

kernel=np.ones((5,5),np.uint8)

erosion=cv.erode(binary,kernel)
dilation=cv.dilate(binary,kernel)

cv.imshow("binary",binary)
cv.imshow("erosion",erosion)
cv.imshow("dilation",dilation)

cv.waitKey()