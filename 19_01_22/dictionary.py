"""
ogrenciler = {
    '120':{
        'ad': 'Ali'
        'soyad': 'Yılmaz'
        'telefon': '532 000 00 01'
    },
    '125':{
        'ad': 'Can'
        'soyad': 'Korkmaz'
        'telefon': '532 000 00 02' 
    },
    '128':{
        'ad': 'Volkan'
        'soyad': 'Yükselen'
        'telefon': '532 000 00 03'
    },
}

1- bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary
içinde saklayınız


2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin

"""

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı : ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci tel no: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon':phone 
# }

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı : ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci tel no: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı : ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci tel no: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})

# print(ogrenciler)

# ogrNo = input('öğrenci no: ')
# ogrenci = ogrenciler[ogrNo]

# print(ogrenci)


print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']}, soyadı: {ogrenci['soyad']}, tefefon numarası: {ogrenci['telefon']}")