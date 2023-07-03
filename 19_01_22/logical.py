# girilen saayının 0-100 arasında olup olmadığını kontrol encodings
x = int(input("sayı giriniz: "))
result = 0 < x < 100


# girilen sayının pozitif çift sayı olup olmadığını kontrol edin 
x = int(input("sayı giriniz: "))
result = (x > 0) and (x %2 == 0 )

# e mail ve parola bilgileriyle giriş kontrolü yapın
email = "edacakmak92@gmail.com"
parola = "123456789"

mail = input("email adresinizi giriniz: ")
şifre = input("şifrenizi giriniz: ")

result = (email == mail) and (parola == şifre)

# girilen 3 sayıyı büyüklük olarak karşılaştırın
x = int(input("sayı1: "))
y = int(input("sayı2: "))
z = int(input("sayı3: "))

result = x < y < z

# kullanıcıdan 2 vize (%60) ve final (%40) notu alıp ortalama hesaplayın
# eğer ortalama 50 üstü ise geçti değilse kaldı yazdırı
#     -ortalama 50 olsa bile final en az 50 olmalı
#     -finalden 70 alındığında ortalamanın önemi yok
x = int(input("vize1: "))
y = int(input("vize2: "))
z = int(input("final: "))

ort = (((x + y)/2) * 0.6 + z * 0.4)

result = (z >= 70) or ((ort >= 50) and (z >= 50))


# kişinin ad, kilo ve boy bilgilerini alarak kilo indekslerini hesaplayın
# formül: (kilo/boy^2)
# aşağıdaki tabloya göre kişi girmeli
# 0-18.4 => zayıf
# 18.5-24.9 => normal
# 25-29.9 => fazla kilolu
# 30.0-34.9 => şişman (obez)
ad = input("adınız: ")
kilo = int(input("kilonuz: "))
boy = float(input("boyunuz: "))

indeks = (kilo/(boy*boy))

0 < indeks < 18.4 == "zayıf"
18.5 < indeks < 24.9 == "normal"
25 < indeks < 29.9 == "fazla kilolu"
30.0 < indeks < 34.9 == "şişman (obez)"

print(indeks)

print(result)

