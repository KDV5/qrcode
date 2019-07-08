import cv2
import pyzbar.pyzbar as pyzbar
# import matplotlib.pyplot as plt

file_path = "./1.mp4"
SavePath = ""
vc = cv2.VideoCapture(file_path)

x = int(vc.get(3))
y = int(vc.get(4))

shift = 0                                   # 像素位置的偏移，左负右正
position = int(x/2) + shift                 # 中间像素的位置
colPerFrame = 1                             #
count = 0
num = []
cap = cv2.VideoCapture("../1.mov")


def detecte(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)
    return gray


def decode(image):
    # 找到图像中的条形码并进行解码
    barcodes = pyzbar.decode(image)
    flag = 0
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
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, .8,
                    (255, 0, 0), 2)

        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        flag = 1
    if flag:
        return True
    else:
        return False


def cut(a):
    first = a[0]
    last = a[0]
    for i in range(1, len(a)):
        if a[i]-a[i-1] > 200:
            last = a[i]
    return first, last


while():
    ret, frame = cap.read()
    count += 1
    if ret is True:
        # 获取二维码或条形码
        temp = detecte(frame)
        temp = temp[550:750, 1000:1200]
        temp = cv2.resize(temp, (400, 400))
        if decode(temp):
            num.append(count)
        # 显示图片
        cv2.imshow('frame', temp)
        # 按q退出
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
first, last = cut(num)
print(first, last)
