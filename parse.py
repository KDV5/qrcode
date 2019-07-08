import zxing

reader = zxing.BarCodeReader()
print(reader)
barcode = reader.decode("4.png")
print(barcode)