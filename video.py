
# coding: utf-8

# In[ ]:

import pyzbar.pyzbar as pyzbar
import cv2


# In[ ]:


# 获取二维码或条形码
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


# In[ ]:


# 读取摄像头
cap = cv2.VideoCapture("./1.MOV")

while(True):
    ret, frame = cap.read()
    if ret==True:
        # 获取二维码或条形码
        decode(frame)
        # 显示图片
        cv2.imshow('frame',frame)
        # 按q退出
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

