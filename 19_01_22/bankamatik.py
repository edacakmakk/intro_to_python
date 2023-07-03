EdaHesap ={
    "ad": "Eda Çakmak",
    "hesapNo": "12345678",
    "bakiye": 3000,
    "ekHesap": 2000
}

MeryemHesap ={
    "ad": "Meryem Gül",
    "hesapNo": "87654321",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print(f"merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if(toplam >= miktar):
            ekHesapkullanimi = input("ek hesap kullanılsın mı (e/h)")

            if ekHesapkullanimi == "e":
                ekhesapKullanılacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapKullanılacakMiktar
                print("paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("üzgünüz bakiye yetersiz")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır" )


def paraYatır(hesap, miktar):
    nereye = input("hangi hesaba yatırmak istiyorsunuz (ana hesap/ek hesap): ")
    if nereye == "ana hesap":
        if miktar >= 5000:
            ekhesapPara = input("bir kısmını ek hesaba aktarmak ister misiniz (e/h))")
            if ekhesapPara == "e":
                nekadar = int(input("ne kadar yatırmak istiyorsunuz: "))
                hesap["ekHesap"] += nekadar
                hesap["bakiye"] += (miktar - nekadar)
                print(f"ana hesabınızda toplam {hesap['bakiye']} TL, ek hesabınızda toplam {hesap['ekHesap']} TL bulunuyor.")
            else:
                print(f"tamamı ana hesaba aktarılıyor. toplam miktar {hesap['bakiye']} ")
                hesap["bakiye"] += miktar
            bakiyeSorgula(EdaHesap)       
    else:
        hesap["ekHesap"] += miktar
        print(f"tamamı ek hesaba aktarılıyor. toplam miktar {hesap['ekHesap']}")
        bakiyeSorgula(EdaHesap)


print(paraYatır(EdaHesap, 5000))
print(paraCek(EdaHesap, 4000))
bakiyeSorgula(EdaHesap)

