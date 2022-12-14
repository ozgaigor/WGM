from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

hat = Image.open("obraz.png")
hat2 = hat.convert("RGB")

r,g,b,a = hat.split()

hat3 = Image.new('RGB', hat2.size, (255,255,255)) # nowy obraz wypełniony na biało
hat3.paste(hat, (0, 0), a)

hat3.show()
hat3.save("obraz3.png")

diff = ImageChops.difference(hat2,hat3)
if diff.getbbox():
    print("Takie same")
else:
    print("Rozne")

print("CMYK - Cyan, Magenta, Yellow, Black - format kolorow stosowany w drukarkach")
print("YCbCr - model przestrzeni kolorow, uzywany do cyfrowego przesylania oraz przechowywania obrazow i wideo.")
print("HSV - model opisu przestrzeni barw")

hatCMYK = hat.convert("CMYK")
hatYCbCr = hat.convert("YCbCr")
hatHSV = hat.convert("HSV")

tryby = ['RGB','CMYK','YCbCr','HSV']

plt.figure(figsize=(16, 16))
i=1
for t in tryby:
    file_name = "tryb_"+ str(t)
    im_c = hat3.convert(t)
    plt.subplot(2, 2, i)
    plt.title(str(file_name))
    plt.imshow(im_c, "gray")
    plt.axis('off')
    i +=1
plt.show()
plt.savefig("fig1.png")

c,m,y,k = hatCMYK.split()
y,cb,cr = hatYCbCr.split()
h,s,v = hatHSV.split()

kanal_cmyk = [c,m,y,k]
kanal_ycbcr = [y,cb,cr]
kanal_hsv = [h,s,v]