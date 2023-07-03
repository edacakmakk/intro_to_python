print("hello world")
print("merhaba")

name = "arin"
message = f"merhaba {name} " # message = "merhaba" + name olarakta yazılabilir

print(message)

message = "merhaba {}"

print(message.format(name)) #yukarıdaki ile aynı sonucu verir, çok fazla 
                            #kullanılan yöntem değildir.

name = "yildiz teknik"

print(len(name)) #len boşluk dahil olmak üzere karakter sayısını sayar

print(name[0]) # 0. karakterin ne olduğunu verir. 0. karakter y harfine eşittir

print(name[0:7]) # 0'dan 7'ye kadar olan karakterleri yazar. 7. karakter yazılmaz.
                 # boşlukları sayar.
# print(name[:7]) yukarıdakinin kısaltılmış halidir


print(name.title()) # tanımlı str'nin başş harflerini büyük yazar

print(name.upper()) # tanımlı karakterin tüm harflerini büyük yazar

print(name.lower()) # tanımlı karakterlerin tüm harfleriniküçük yazar

print(name.count('i')) # tanımlı karakterde kaç tane i olduğunu verir

print(name.replace("teknik", "universitesi")) # ilk yazılanla ikinci yazılanı değiştirir

print(dir(name)) # string''te kullanabileceğimiz tüm metotları gösterir

print(help(str)) # tüm metotların ne işe yaradığını söyler



