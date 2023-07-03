# girilen 2 sayıdan hangisi büyüktür

a = int(input("a: "))
b = int(input("b: "))

result = (a > b)

print(f"{a} {b} sayınından büyüktür: {result}")

# kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalma alınız
#   eğer ortalama 50 ve üzerindeyse geçti değilse kaldı yazdırın
x = int(input("vize notu1: "))
y = int(input("vize notu2: "))
z = int(input("final notu: "))

ort = (((x + y)/2) * 0.6 + z * 0.4)

result = (ort >= 50)

print(f"dersten geçme durumunuz: {result}")


# girilen bir sayının çift mi tek mi olduğunu yazdırın
a = int(input("sayı giriniz: "))

z = a % 2
result = z == 0 

print(f"girilen sayının çift olma durumu: {result}")

# girilen bir sayının negatif pozitif durumunu yazdırın
d = int(input("sayı giriniz: "))
 
result = d > 0 

print(f"girilen sayının pozitif olma durumu: {result}")

# parola ve email bilgisini isteyip doğrulama kontrol ediniz
# (email: edacakmak92@gmail.com parola: 123456789)
email = "edacakmak92@gmail.com"
parola = "123456789"

mail = input("mail adresinizi giriniz: ")
password = input("parolanızı giriniz: ")

result1 = mail == email 
result2 = password == parola

print(f"girilen email doğruluğu : {result1}, girilen parola doğruluğu: {result2}")

