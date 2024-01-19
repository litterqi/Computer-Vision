# OpenCV使用入门
## 简单介绍
OpenCV是一个开源的计算机视觉库，提供了超过2500个算法和函数，涵盖了计算机视觉和机器学习的各个领域。OpenCV支持多种编程语言，包括C++、Python、Java等。它可以在多个操作系统上运行，包括Windows、Linux、macOS等。OpenCV的主要功能包括图像处理、计算机视觉、机器学习等，它可以用于图像处理、目标检测、人脸识别、手势识别、运动跟踪等多个领域。
## 安装OpenCV
目前使用的IDE为VScode，直接在终端输入`pip install opencv-python`即可安装。
## 基本功能
### 读取图像
使用OpenCV中的库函数读取图片并打印其类型和形状：
```
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../kaggle/wallpaper2.jpg')

print(type(img))
print(img.shape)
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/b11d1763-c7a3-44d1-b09a-ef032f88c206)

250–图像高度 400–图像宽度 3–通道数(在RGB颜色模式下，一张图片的通道数为3，分别代表红色、绿色和蓝色的信息。在灰度颜色模式下，一张图片的通道数为1，代表亮度信息)
### 显示图像
使用imshow函数显示图像(此时发现图像一闪而过，使用waitKey函数，使窗口等待有键盘输入任意键再关闭)
```
cv.imshow("image",img)
cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/fb92dba9-085a-4924-b3a8-2eea4ab452a6)
### 图像的彩色通道BGR
计算机处理图像时认为任何颜色都是由红、绿、蓝(RGB)三种颜色按一定比例混合而成的。OpenCV对三种颜色的存储顺序是BGR，与常见的RGB相反。

![image](https://github.com/litterqi/Computer-Vision/assets/123362884/aed5ac75-a7ad-4d9f-832b-1de360244cfe)

提取三张灰度图：
```
cv.imshow("blue",img[:, :, 0])
cv.imshow("green",img[:, :, 1])
cv.imshow("red",img[:, :, 2])
cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/223520a2-6369-4808-94a5-0906cf273ac7)
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/58c9bd56-b2f0-4381-b47b-4addc8c8503f)
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/c4dca55b-5a2e-4d56-b625-3964d7e454ff)


