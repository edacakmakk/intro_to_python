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

result = soup.prettify()  #prints the corrupted html document to the console in a corrected way
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2 # When we do it this way, it prints the first one among the multiple h2 to the screen.
result = soup.h2.name
result = soup.h2.string

result = soup.find_all("h2") #returns all h2s in list form
result = soup.find_all("h2")[0]
result = soup.find_all("h2")[1]

result = soup.div
result = soup.find_all("div")[1].ul.li # the first come
result = soup.find_all("div")[1].ul.find_all("li") # this way they all come in list form.

result = soup.div.findChildren() # who came up with this name :D Anyway, this element brings everything under the div

result = soup.div.findNextSibling() # switches to second div
#result = soup.div.findNextSibling().findNextSibling() goes from the next to the next (garip cümleler varan 1)
##result = soup.div.findNextSibling().findNextSibling().findPreviousSibling() If we do it as, the last thing I added makes it go to the previous one

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/ The remaining examples can be viewed here.
result = soup.find_all("a")
for link in result:
    print(link.get("href"))



print(result)
