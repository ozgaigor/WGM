from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import math as m

def zakres(w, h): 
    return [(i, j) for i in range(w) for j in range(h)]


def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    for i, j in zakres(w,h):
        if inicjaly.getpixel((i,j))==0:
            obraz.putpixel((i + m, j + n), kolor)
        else:
            obraz.putpixel((i + m, j + n), (255,255,255))
    obraz.save("utworzone_obrazy\obraz1.jpg")
    obraz.show()

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if inicjaly.getpixel((i, j)) == 0:
            p = obraz.getpixel((i + m, j + n))
            obraz.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    obraz.save("utworzone_obrazy\obraz2.jpg")
    obraz.show()

def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    pix = inicjaly.load()
    pix2 = obraz.load()
    for i, j in zakres(w,h):
        if pix[i,j]==0:
           pix2[i+m,j+n]=kolor
        else:
            pix2[i+m,j+n]=(255,255,255) 
    obraz.show()

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    w0, h0 = inicjaly.size
    pix = inicjaly.load()
    pix2 = obraz.load()
    for i, j in zakres(w0, h0):
        if pix[i,j]==0:
            p = pix2[i+m,j+n]
            pix2[i+m,j+n]=(p[0] + x, p[1] + y, p[2] + z)
    obraz.show()

def kontrast(obraz, wsp_kontrastu):
    if wsp_kontrastu>=0 and wsp_kontrastu<=100:
        mn =  (( 255 + wsp_kontrastu) /255) **2
        obraz = obraz.point(lambda i: 128+(i-128)*mn)
        obraz.show()
    else:
        print("Współczynnik kontrastu musi mieścić się w przedziale <0,100>")

def transformacja_logarytmiczna(obraz):
    obraz = obraz.point(lambda i: 255*np.log(1+i/255))
    obraz.show()

def transformacja_gamma (obraz, gamma):
    if gamma >0:
        obraz = obraz.point(lambda i: (i/255)**(1/gamma)*255)
        obraz.show()
    else:
        print("Gamma musi być >0")
    
    
def zad4(obraz):
    obraz = obraz.point(lambda i:i+100)
    obraz.show()

def zad5(obraz):
    T = np.array(obraz,dtype='uint8')
    T +=100
    obraz_wynik = Image.fromarray(T,"RGB")
    obraz_wynik.show()

im = Image.open("obraz.jpg")
im1 = im.copy()
im2 = im.copy()
im3 = im.copy()
im4 = im.copy()
im5 = im.copy()
im6 = im.copy()
im7 = im.copy()
im8 = im.copy()
im9 = im.copy()
inicjaly = Image.open("inicjaly.bmp")
wstaw_inicjaly(im1,inicjaly,628,360,(255,0,0))
wstaw_inicjaly_maska(im2,inicjaly,364,205,255,255,255)
wstaw_inicjaly_load(im3,inicjaly,628,360,(255,0,0))
wstaw_inicjaly_maska_load(im2,inicjaly,364,205,255,255,255)
kontrast(im5,100)
transformacja_logarytmiczna(im6)
transformacja_gamma (im7,3)
zad4(im8)
zad5(im9)