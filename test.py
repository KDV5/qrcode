import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
# import matplotlib.pyplot as plt

FilePath = "./1.mp4"
SavePath = ""
vc = cv2.VideoCapture(FilePath)

x = int(vc.get(3))
y = int(vc.get(4))

shift = 0                                   # 像素位置的偏移，左负右正
position = int(x/2) + shift                 # 中间像素的位置
colPerFrame = 1                             #
count = 0

cap = cv2.VideoCapture("./1.mov")

def edge(src):
    kernel1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], np.float32)
    kernel2 = np.array([[-0.25,0,0.25],[-0.5,0,0.5],[-0.25,0,0.25]], np.float32)
    temp1 = cv2.filter2D(src, -1, kernel1)
    temp2 = cv2.filter2D(src, -1, kernel2)
    result = temp1[:, position]
    return temp1,temp2

def detecte(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,gray = cv2.threshold(gray, 0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
    return gray
    #i,contours=cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #return i,contours

def decode(image):
    # 找到图像中的条形码并进行解码
    barcodes = pyzbar.decode(image)
    # 循环检测到的条形码
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)

        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,.8, (255, 0, 0), 2)

        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

while(True):
    ret, frame = cap.read()
    if ret == True:
        # 获取二维码或条形码
        temp = detecte(frame)
        temp = temp[550:750, 1000:1200]
        temp = cv2.resize(temp,(400,400))
        decode(temp)
        # 显示图片
        cv2.imshow('frame', temp)
        # 按q退出
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

# if vc.isOpened():                           # 读取视频
#     a, b = vc.read()
#     b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
#     result1, result2 = edge(b)
#     x = cv2.Sobel(b, cv2.CV_16S, 1, 0)
#     y = cv2.Sobel(b, cv2.CV_16S, 0, 1)
#
#     absX = cv2.convertScaleAbs(x)
#     absY = cv2.convertScaleAbs(y)
#     dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
#     cv2.imshow("sobel", dst)
#
#     img = cv2.GaussianBlur(b, (3, 3), 0)
#     canny = cv2.Canny(img, 50, 150)
#     cv2.imshow("canny", canny)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("打开视频文件失败")

# while vc.isOpened():
#     a, b = vc.read()
#     if a:
#         temp = b[0:y, position:position + colPerFrame]      # 截取帧中间一列像素值
#         result = np.hstack((result, temp))                  # 水平排列
#         print(count)
#         count+=1
#     else:
#        break
    
# cv2.imwrite(SavePath, result)
# result = cv2.resize(result, (int(x*2),y))
# cv2.imwrite(SavePath,result)
# vc.release()