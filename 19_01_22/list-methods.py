names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]


# cenk ismini listenin sonuna ekleyin
names.append("Cenk")

# sena ismini listenin başına ekleyin
names.insert(0,"Sena")

# deniz iismini listeden silin
names.remove("Deniz")

# hakan isminin indeksi nedir
result = names.index("Hakan")

# ali listenin bir elemanı mı
result = "Ali" in names

# liste elemanlarını ters çevirin
names.reverse()

# liste elemanlarını alfabetik olarak sıralayın
names.sort()

# years listesini büyükten küçüğe sıralayın
years.sort
years.reverse()

# str = "Chevrolet,Dacia" karakter dizisini listeye çevirin
str = "Chevrolet,Dacia" 
result = str.split(",")

# years dizisinin en büyük ve en küçük elemanı nedir
result = max(years)
result = min(years)

# years dizisinde kaç tane 1998 elemanı var
result = years.count(1998)

# years dizisinin tüm elemanlarını silin
years.clear()

# kullanıcıdan alacağınız 3 tane marka bilgisini listeye ekleyin
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)


print(names)
print(result)
print(years)
print(markalar)