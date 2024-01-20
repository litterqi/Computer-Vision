import cv2 as cv

capture=cv.VideoCapture(0)

while True:
    ret, frame =capture.read()
    cv.imshow("camera",frame)
    key=cv.waitKey(1)
    if key!=-1:
        break

capture.release()