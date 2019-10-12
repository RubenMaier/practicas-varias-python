import requests # nos permite poder hacer solitudes a internet
from bs4 import BeautifulSoup # nos permite parsear el texto html y acceder a el como un arbol
import urllib # me permite guardar las imagenes que queremos extraer

def ejecutar():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser') #parseamos la respeuesta
        # queremos acceder al tag img que esta en el div comic
        img_container = soup.find(id='comic')
        img_url = img_container.find('img')['src'] # acceso al tag de la imagen
        img_name = img_url.split('/')[-1] # accedemos al nombre original, pero al ultimo por eso -1
        urllib.request.urlretrieve('https:{}'.format(img_url), img_name)

if __name__ == '__main__':
    ejecutar()