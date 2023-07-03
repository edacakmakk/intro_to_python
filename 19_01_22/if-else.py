# kullanıcıdan isim, yaş, eğitim bilgileri istenip ehliyet alabilme durumunu kontrol ediniz. 
# ehliyet alma koşulu en az 18 eğitim durumu lise ya da üniversite olmalıdır
isim = input("adınız: ")
yas = int(input("yaşınız: "))
eğitim = input("eğitim durumunuz: ")

if yas >= 18 and (eğitim == ("lise") or ("üniversite")):
    print("ehliyet alabilirsiniz")
else:
    print("ehliyet almaya uygun değilsiniz")


# bir öğrencinin 2 yazılı 1 sözlü notunu alıp ortalamaya göre not aralığına karşılık gelen 
# not bilgisini yazdırın 
# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 4
x = int(input("yazılı1: "))
y = int(input("yazılı2: "))
z = int(input("sözlü: "))

ort = (x+y+z)/3

if ort < 25:
    print("0")
elif ort < 45:
    print("1")
elif ort < 55:
    print("2")
elif ort < 70:
    print("3")
elif ort < 85:
    print("4")
else:
    print("5")

# trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere göre hesaplayın 
# 1.bakım => 1. yıl 
# 2.bakım => 2. yıl 
# 3. bakım => 3. yıl 
# *süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayın 
# **datetime modülünü kullanmanız gerekiyor
# (simdi) - (2018/8/1) => gün
import datetime

tarih = input("aracınız hangi tarihte trafiğe çıktı (2019/8/9): ")
tarih = tarih.split("/")

trafigecikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigecikis
days = fark.days

if days <= 365:
    print("1.servis aralığı")
elif days <= 365*2:
    print("2.servis aralığı")
elif days <= 365*3:
    print("3.servis aralığı")
else:
    print("geçersiz tarih")

