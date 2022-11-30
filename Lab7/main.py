from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt

im = Image.open('baby_yoda.jpg')
obraz = Image.open('obraz.jpg')
im2 = im.copy()
im3 = im.copy()

def filtruj(obraz, kernel, scale):
    x = obraz.filter(ImageFilter.Kernel((3,3),kernel,scale))
    #x.show()
    return x
def filtruj2(obraz,kernel,scale):
    x2 = obraz.filter(ImageFilter.Kernel((5,5),kernel,scale))
    #x2.show()
    return x2

#print(ImageFilter.BLUR.filterargs)












filtruj(im,(-1, -1, -1, -1, 8, -1, -1, -1, -1),1)
blur = filtruj2(im2,(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1),16)
blur1 = im3.filter(ImageFilter.BLUR())

plt.figure(figsize=(32, 16))
plt.subplot(1,3,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(blur, "gray")
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(blur1, "gray")
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(ImageChops.difference(blur1,blur), "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
plt.show()
