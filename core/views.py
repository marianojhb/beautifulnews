from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def home(request):

    url = "https://www.lanacion.com.ar/"
    req = requests.get(url) # con el método request obtengo la home de lanacion.com
    html_doc = req.text # obtengo el contenido del sitio en formato legible
    soup = BeautifulSoup(html_doc, 'html.parser') # parseo el response con la biblioteca bs4
    articulos = soup.find_all('article') # creo una lista con los articulos de lanacion.com
    articulos = articulos[:6] # me quedo solo con los 6 primeros articulos

    # Reescribo la lista con un diccionario por noticia
    # Titulo
    # Link a foto
    # Subtitulo
    data = []
    for articulo in articulos:
        titulo = articulo.a['title']
        foto = 'https:' + articulo.source['srcset']
        try:
            subtitulo = articulo.p.a.get_text(strip=True)
        except AttributeError:
            subtitulo = ""
        link =  url[:-1] + articulo.a['href']

        data.append({"titulo" : titulo, "subtitulo" : subtitulo, "link": link, "foto": foto })
 
    return render(request,"core/index.html", {"lanacion": data})

def about(request):
    return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")

def page(request):
    return render(request,"core/page.html")