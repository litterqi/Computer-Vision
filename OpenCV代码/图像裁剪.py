import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../kaggle/wallpaper2.jpg')

cut=img[50:200,100:300]
cv.imshow("cut",cut)
cv.waitKey()