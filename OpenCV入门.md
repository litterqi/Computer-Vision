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

250–图像高度，400–图像宽度，3–通道数
