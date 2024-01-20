import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../kaggle/poker.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

template=gray[75:105,235:265]

match=cv.matchTemplate(gray,template,cv.TM_CCOEFF_NORMED)
locations=np.where(match>=0.9)

w, h =template.shape[0:2]
for p in zip(*locations[::-1]):
    x1, y1 =p[0],p[1]
    x2, y2 =x1+w, y1+h
    cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

cv.imshow("image",img)
cv.waitKey()