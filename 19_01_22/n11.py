import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class":"column"},limit=3)
count = 1

for li in list:
    name = li.find("div", {"class":"proDetail"}).find("h3", {"class":"adGroupProduct"}).text
    price = li.find("div", {"class":"proDetail"}).ins.text.strip().strip("TL")
    
    print(name, price)


