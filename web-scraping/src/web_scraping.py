import requests  # nos permite poder hacer solitudes a internet
# nos permite parsear el texto html y acceder a el como un árbol
from bs4 import BeautifulSoup
import urllib  # me permite guardar las imágenes que queremos extraer


def ejecutar():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        # parseamos la respuesta
        soup = BeautifulSoup(response.content, 'html.parser')
        # queremos acceder al tag img que esta en el div comic
        img_container = soup.find(id='comic')
        # acceso al tag de la imagen
        img_url = img_container.find('img')['src']
        # accedemos al nombre original, pero al ultimo por eso -1
        img_name = img_url.split('/')[-1]
        urllib.request.urlretrieve('https:{}'.format(img_url), img_name)


if __name__ == '__main__':
    ejecutar()
