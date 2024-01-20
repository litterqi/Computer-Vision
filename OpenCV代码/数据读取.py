import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../kaggle/wallpaper2.jpg')

print(type(img))
print(img.shape)

cv.imshow("image",img)
cv.waitKey()