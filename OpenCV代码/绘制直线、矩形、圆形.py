import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=np.zeros([300,300,3],dtype=np.uint8)

cv.line(img,(100,100),(200,200),(255,0,0),2)
cv.rectangle(img,(30,100),(60,150),(0,255,0),2)
cv.circle(img,(150,100),20,(0,0,255),2)     
cv.putText(img,"hello",(100,50),0,1,(255,255,255),2,1)                
cv.imshow("image",img)
cv.waitKey()