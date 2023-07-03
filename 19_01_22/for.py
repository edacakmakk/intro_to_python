sayilar = [1,3,5,7,9,12,19,21]

# sayılar listesindeki hangi sayılar 3 ün katıdır 
for sayı in sayilar:
    if (sayı %3 == 0):
        print(sayı)
    
# sayılar listesindeki sayıların toplamı kaçtır 
toplam = 0
for sayı in sayilar:
    toplam += sayı
print("toplam:",toplam)

# sayılar listesindeki tek sayıların karesini alınız 
for sayı in sayilar:
    if (sayı %2 == 1):
        sayı **= 2
        print(sayı)

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# sehirlerden hangileri en fazla 5 karakterlidir 
for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)

urunler = [
    {"name":"samsung s6", "price":"3000"},
    {"name":"samsung s7", "price":"4000"},
    {"name":"samsung s8", "price":"5000"},
    {"name":"samsung s8", "price":"6000"},
]

# ürünlerin fiyatının toplamı nedir
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat
print(toplam)

# ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    fiyat = int(urun["price"])
    if fiyat <= 5000:
        adı = urun["name"]
        print(adı)

# for urun in urunler:
#     if (int(urun["price"]) <= 5000):
#         print(urun["name"])


