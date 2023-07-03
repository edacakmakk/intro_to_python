import requests
import json


api_url = "https://api.apilayer.com/exchangerates_data/live?base="

bozulan_doviz = input("bozulan dööviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?: "))

result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * result["rates"][alinan_doviz], alinan_doviz))


#NOT: kod çalışmıyor çünkü gidilen site ücretli hale gelmiş bilgiilere ulaşamıyoruz. 
#ama mantıkk aynı
