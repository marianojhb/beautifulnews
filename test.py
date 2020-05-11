from bs4 import BeautifulSoup
import requests

url = "https://www.lanacion.com.ar/"
req = requests.get(url)

respdata = req.content
html_doc = respdata

# file = open("lanacion4.html","w")

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# file.write(str(soup))
# file.close()

