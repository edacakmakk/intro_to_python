sayilar = [1,3,5,7,9,12,19,21]

# sayilar listesini while ile ekrana yazdırın
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
x = int(input("başlangıç sayısı: "))
y = int(input("bitiş sayısı: "))

while x <= y:
    if x %2 == 1:
        print(x)
    x += 1

# 1-100 arasındaki sayıları azalan şekilde yazdırın 
x = 1
y = 100

while y >= x:
    print(y)
    y -= 1

# kulanıcıdan alacağınız 5 sayıyı ekranda sıralı şekilde yazdırın 
numbers = []

i = 0

while i < 5:
    sayi = int(input("sayı giriniz: "))
    numbers.append(sayi)
    i += 1
numbers.sort()

print(numbers)

# kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın 
# *ürün sayısını kulanıcıya sorun 
# *dictionary listesi yapısı (name, price) şeklinde olsun 
# *ürünekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin 
urunler = []

adet = int(input("kaç ürün eklemk istiyorsunuz: "))
i = 0

while (i < adet):
    name = input("ürün ismi: ")
    price = input("ürün fiyatı: ")
    urunler.append({
        "name": name,
        "price": price
    })
    i += 1

for urun in urunler:
    print(f"urun adı: {urun['name']} urun fiyatı: {urun['price']}")