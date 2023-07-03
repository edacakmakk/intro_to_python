# Bmw, Mercedes, Opel, mazda elemanlaarıyla liste oluştur 
arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]


# liste kaç elemanlı
result = len(arabalar)


# listenin ilk ve son elemanı ne
result = arabalar[0]
result = arabalar[-1]

# mazda değerini toyota ile değiştirin
arabalar[-1] = "toyota"

# listenin -2 indeksteki değeri ne
result = arabalar[-2]

# listenin ilk 3 elemanını alın
result = arabalar[:3]

# llistenin son iki elemanı yerine toyota ve renault değerlerini ekleyin 
arabalar[-2:] = "toyota", "renault"

# listenin üzerine audi ve nissan değerini ekleyin
result = arabalar + ["audi", "nissan"]

# listenin son elemanını silin
del arabalar[-1]

# liste elemanlarını tersten yazın
result = arabalar[::-1]

# mercedes listenin bir elemanı mı
r = "Mercedes" in arabalar
print(r)

# aşağıdaki verileri liste içinde saklayın 
    # studentA: yiğit bilgi 2010, (70,60,70)
    # studentB: sena turan 1999, (80,80,70)
    # studentC: ahmet turan 1998, (80,70,90)
studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

# liste elemanlarını ekrana yazdırın
print(studentA, studentB, studentC)

result = f"{studentB[0]} {studentB[1]} {2022-studentB[2]} yaşında ve not ortalaması {(studentB[3][0] + studentB[3][1] + studentB[3][2])/3}"


print(result)
print(arabalar)