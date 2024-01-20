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

将三张图像的平方和做加权平均，即得到灰度图：
```
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/72f09874-0b78-420c-b984-27738ab5570d)

### 图像裁剪
使用索引(先行后列)对图片进行裁剪，等价于画图软件中的裁剪工具：
```
cut=img[50:200,100:300]
cv.imshow("cut",cut)
cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/5d3a75ca-d9d3-4030-b5c1-e8d1409ea7a7)

### 绘制直线、矩形、圆形、字符串
使用numpy库创建了一个大小为300x300、颜色通道数为3的黑色图像。再用line函数绘制一条起点坐标为(100,100)，终点坐标为(200,200)，颜色为蓝色(255,0,0)，线宽为2的直线。

使用类似的方式绘制矩形、圆形和字符串：
```
img=np.zeros([300,300,3],dtype=np.uint8)

cv.line(img,(100,100),(200,200),(255,0,0),2)
cv.rectangle(img,(30,100),(60,150),(0,255,0),2)
cv.circle(img,(150,100),20,(0,0,255),2)
cv.putText(img,"hello",(100,50),0,1,(255,255,255),2,1)                 
cv.imshow("image",img)
cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/48e8c2a2-4763-4510-89b4-43b28284d046)

### 图像特征点提取
对灰度图中的转角点进行识别，返回检测到的500个角点的坐标。对于每个角点在对应位置绘制小的圆形作为标记：
```
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners=cv.goodFeaturesToTrack(gray,500,0.1,10)
for corner in corners:
    x, y =corner.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,255,0),-1)

cv.imshow("corners",img)
cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/1c77b024-bbd0-4015-adec-eddc2d02bdf9)

### 模板匹配
使用OpenCV中的标准相关匹配算法，匹配图片中扑克牌上的菱形，找出匹配系数大于等于0.9的匹配点：

这里的匹配算法对图片大小敏感(图中较小的菱形没有匹配)，可以通过改变图片大小的方法匹配多次。
```
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
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/fcc41193-3bc4-4e22-b291-1cd874233d41)

### 边缘检测
使用Canny算法进行边缘检测。使用梯度区间(100,200)来定义边缘。如果梯度大于200，则可确定其是一个边缘，即有明显的明暗变化；如果梯度小于100，则可确定其不是边缘；如果梯度在100~200之间，则要看这个像素是否与已知的像素相连，如果相连则判断其是边缘，否则不是。
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/5c0b6d15-8d2c-41c4-8449-5a417e7bddf1)
```
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny=cv.Canny(gray,100,200)

cv.imshow("canny",canny)
cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/fe2d9477-93c3-4cf5-b1c2-49902b833cc9)

### 图像二值化
阈值算法把灰度图片根据阈值分为黑与白。最简单的二值化处理是定义一个固定的阈值。

对于灰度分布不均匀的图片，可以调用adaptiveThreshold函数来使用自适应阈值算法，也就是把图片分成很多区域，每个区域独立计算阈值。可以看到更多的文字显示了出来。

还可以使用大津算法(ostu)来自动计算适当的阈值，即不需要人为定义阈值，使得分离出的两个灰度分布差异最大化。
```
gray=cv.imread("../kaggle/bookpage.jpg",cv.IMREAD_GRAYSCALE)
ret, binary =cv.threshold(gray,10,255,cv.THRESH_BINARY)

binary_adaptive=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)

ret1, binary_otsu =cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("gray",gray)
cv.imshow("binary",binary)
cv.imshow("binary_adaptive",binary_adaptive)
cv.imshow("otsu",binary_otsu)

cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/80af1956-d266-472c-b1ed-102c9a80e817)
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/a47d692b-cf41-405c-8caf-ccf0676dd0dc)
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/ee34f10e-390d-4ab2-8d01-993815ea5dff)
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/6c30325e-eb8c-4804-b284-ca6bfc7cbda1)

### 图像形态学之腐蚀和膨胀
首先对灰度图进行二值化操作得到binary图，然后定义一个操作和kernel为5*5像素的正方形。使用该kernel腐蚀binary图像。可以发现图标的边缘瘦了一圈，就像被腐蚀了一样。使用类似是方法可以进行图像的膨胀操作，可以发现图标的边缘胖了一圈，即为膨胀。
```
gray=cv.imread("../kaggle/opencv_logo.jpg",cv.IMREAD_GRAYSCALE)

_, binary =cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)

kernel=np.ones((5,5),np.uint8)

erosion=cv.erode(binary,kernel)
dilation=cv.dilate(binary,kernel)

cv.imshow("binary",binary)
cv.imshow("erosion",erosion)
cv.imshow("dilation",dilation)

cv.waitKey()
```
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/2fb1a009-5b8c-43e1-9fe0-38c1d5c0a92c)
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/210e5463-c490-48ea-b4cf-fd7fcde9848d)
![image](https://github.com/litterqi/Computer-Vision/assets/123362884/5c5509c9-191e-46c8-a0a3-db17784eae0a)

通过交替使用腐蚀和膨胀，可以实现更多的图形学变化。
### 调用电脑摄像头
使用VideoCapture函数获取摄像头的指针，需要传入调用的摄像头的序号(第一个摄像头的序号为0)。与读取静态图片不同，对摄像头画面的采集是连续的，即要循环读取每一帧的画面。

在while循环中，使用read函数读取画面并将其展示出来。等待键盘输入一毫秒，如果键盘输入任意键，即跳出循环。最后释放capture指针。
```
capture=cv.VideoCapture(0)

while True:
    ret, frame =capture.read()
    cv.imshow("camera",frame)
    key=cv.waitKey(1)
    if key!=-1:
        break

capture.release()
```
