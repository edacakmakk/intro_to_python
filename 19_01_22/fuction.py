#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("selam ", 5)


# kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazınız.
def listeyeCevir(*args):
    liste = []

    for arg in args:
       liste.append(arg)

    return liste 

result = listeyeCevir(10,50,40,60, "hahahaha")

print(result)

# göderilen 2 sayı arasındaki tüm asal sayıları bulun.
sayi1 = int(input("sayı1: "))
sayi2 = int(input("sayı2: "))

def asalBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalBul(sayi1, sayi2)


# kendisine gönderilen bir sayının tam bölenlerini bir liste şekline döndürün.

def tamBolen(sayi):
    tamBolenler = []

    for say in range(2, sayi):
        if (sayi %say == 0):
            tamBolenler.append(say)
    
    return tamBolenler 

print(tamBolen(32))



