
# coding: utf-8

# In[36]:


from pyzbar import pyzbar
import cv2


# In[37]:


# 读取图片
image = cv2.imread('1.jpg')
temp = cv2.resize(image, (300,300))

cv2.waitKey(0)
# 找到图像中的条形码并进行解码
barcodes = pyzbar.decode(temp)

# In[39]:


def decode(image, barcodes):
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

    # 展示输出图像
    cv2.imshow("Image", image)
    cv2.waitKey(0)


# In[40]:


#. 识别二维码
decode(temp, barcodes)


# In[42]:


# # 读取图片
# image = cv2.imread('5.png')
#
# # 找到图像中的条形码并进行解码
# barcodes = pyzbar.decode(image)
#
# # 识别条形码
# decode(image, barcodes)

