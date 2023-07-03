"""
1-100 arasında rasgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
**"random modülü" için "python random" şeklinde arama yapın.
**100 üzerinden puanlama yapın. her soru 20 puan.
**hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

"""

import random

a = random.randint(1,100)
can = int(input("istediğiniz hak sayısı: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))

    if a == tahmin:
        print (f"tebrikler {sayac}. defa da bildiniz. toplam puanınız: {100 - (100/can) * (sayac-1)}")
        break
    elif a > tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if hak == 0:
        print(f"hakkınız bitti. tutulan sayı: {a}")


