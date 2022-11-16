from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

def zakres(w,h):
    return [(i,j) for i in range (w) for j in range(h)]

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    for i, j in zakres(w,h):
        if inicjaly.getpixel((i,j))==0:
            obraz.putpixel((i + m, j + n), kolor)
        else:
            obraz.putpixel((i + m, j + n), (255,255,255))
    obraz.save("obraz1.jpg")
    obraz.show()

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    w, h = inicjaly.size
    for i, j in zakres(w, h):
        if inicjaly.getpixel((i,j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return obraz

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


im = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")
im1 = im.copy()
wstaw_inicjaly(im1,inicjaly,1820,1230,(255,0,0))


'''

2.2 Analogicznie do funkcji rozjasnij_obraz_z_maska, napisz funkcję
wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z), gdzie m, n są
współrzędnymi punktu, w którym traktując inicjały jako maskę
zmienimy piksele (a, b, c) odpowiadające czarnym pikselom z maski na
(a+x, b+y, c+z). Utwórz i zapisz obraz2, w którym maska jest wstawiona
mniej więcej na środku obrazu.
3. Stosując metodę load napisz funkcje
wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor) oraz
wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z) działające identycznie
jak funkcje z pkt. 2.1, 2.2. Przetestuj te funkcje, ale nie zapisuj obrazów.
4. Stosując metodę point i funkcję lambda:
4.1 Napisz funkcję kontrast(obraz, wsp_kontrastu), która działa tak, że
każdy piksel i zmienia wartość zgodnie z funkcją kontrastu
f(i) = 128 + (i -128) * mn, gdzie
mn = (( 255 + wsp_kontrastu) /255) **2, a wsp_kontrastu przyjmuje
wartości o 0 do 100
Przetestuj różne wartości wsp_kontrastu i napisz w raporcie jak wartości
wsp_kontrastu wpływają na uzyskany efekt (słownie i wklejając obrazek)
4.3 Napisz funkcję transformacja_logarytmiczna(obraz), która działa tak,
że każdy piksel i zmienia wartość zgodnie z funkcją
f(i) = 255 * np.log(1 + i / 255)
Przetestuj i napisz w raporcie jaki jest efekt (słownie i wklejając obrazek)
4.4 Napisz funkcję transformacja_gamma (obraz, gamma), która działa
tak, że każdy piksel i zmienia wartość zgodnie z funkcją
f(i) = (i / 255) ** (1 / gamma) * 255), gdzie gamma jest współczynnikiem
większym od zera.
Przetestuj różne wartości gamma i napisz w raporcie jak wartości gamma wpływają na uzyskany efekt (słownie i wklejając obrazek)
4. Napisz, dlaczego obraz powstały z zastosowania poleceń
T = np.array(obraz, dtype='uint8')
T += 100
obraz_wynik = Image.fromarray(T, "RGB")
jest inny niż obraz powstały z zastosowania funkcji
obraz.point(lambda i: i + 100)
Wskazowka: co się dzieje, gdy wartość elementu tablicy przekracza 255 w typie uint8, oraz co się dzieje w przypadku obrazu.
5. Napisz funkcje, która działa na tablicy obrazu i daje taki sam efekt, co obraz.point(lambda i: i + 100)
Raport, plik z kodem oraz wszystkie obrazy zaznaczone na czerwono wstaw na Moodle.
'''