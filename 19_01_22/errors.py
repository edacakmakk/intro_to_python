from unittest import result


liste = ["1","2","5a","10b","abc","10","50"]

# liste elemanları içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
        result = int(x)
        print(result)
    except:
        continue

# kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğunda emin olunuz

while True:
    x = input("x: ")
    if x == "q":
        break
    
    try:
        result = float(x)
        print(f"girdiğiniz sayı {result}")
        break
    except:
        print("geçersiz sayı")
        continue


# girilen parolanın içinde türkçe karakter hatası veriniz.
def chekpassword(parola):
    turkce_karakterler = "ğüşİöç"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez")
        else:
            pass
    print("geçerli parola")

parola = input("parola: ")

try:
    chekpassword(parola)
except TypeError as err:
    print(err)

# faktöriyel fonksiyonu oluşturup fonksiyona gelen değerler için hata mesajları verin 
def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("negatif sayı")

    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
