import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

gray=cv.imread("../kaggle/bookpage.jpg",cv.IMREAD_GRAYSCALE)
ret, binary =cv.threshold(gray,10,255,cv.THRESH_BINARY)

binary_adaptive=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)

ret1, binary_otsu =cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("gray",gray)
cv.imshow("binary",binary)
cv.imshow("binary_adaptive",binary_adaptive)
cv.imshow("otsu",binary_otsu)

cv.waitKey()