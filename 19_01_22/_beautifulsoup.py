html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ilk web sayfam</title>
</head>
<body>

<h1 id = "header">
        Python öğrenirken kendimi burada buldum :)
    </h1>

    <div class = "grup1">

        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class = "grup2">

        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="t.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>
    
</body>
</html>

"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()  #bozulmuş olan html dökümanını düzeltilmiş bir şekilde konsola yazdırır
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2 # bu şekilde yaptığımızda birden fazla olan h2 arasından ilk olanı eekrana yazdırır
result = soup.h2.name
result = soup.h2.string

result = soup.find_all("h2") #liste şeklinde olarak bütün h2 lerii getirir
result = soup.find_all("h2")[0]
result = soup.find_all("h2")[1]

result = soup.div
result = soup.find_all("div")[1].ul.li # en baştaki gelir
result = soup.find_all("div")[1].ul.find_all("li")# bu şekilde hepsi liste şeklinde gelir.

result = soup.div.findChildren() # bu ismi kim bulmuş ya :D Neyse bu eleman div altındaki her şeyi getirir

result = soup.div.findNextSibling() # ikinci div'e geçer
#result = soup.div.findNextSibling().findNextSibling() sonrakinin sonrakisine geçer (garip cümleler varan 1)
##result = soup.div.findNextSibling().findNextSibling().findPreviousSibling() olarak yapasak en spn eklediğim şey bir öncekine gitmesini sağlar

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/ geri kalan örnekler buradan incelebilir.

result = soup.find_all("a")
for link in result:
    print(link.get("href"))



print(result)