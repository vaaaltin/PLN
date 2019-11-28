import pandas as pd
import numpy as np
import sys
import string
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    lista_artistas = []
    for x in string.ascii_uppercase:
        lista_artistas += pega_artista(x)
    for x in lista_artistas:
        if '.html' in x:
            lista_artistas.remove(x)
    dicionario = {'links_artistas':lista_artistas}
    data_set_artistas = pd.DataFrame(dicionario)
    data_set_artistas.to_csv(str(sys.argv[1]+'/artistas.txt'), sep='\t', mode='w', index=False)


def pega_artista(letra):
    print(letra)
    url = 'https://www.letras.mus.br/letra/'+letra+'/'
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    lista_art = []
    todo_en = soup.find("div", {"class": "home-artistas g-1 g-fix"})
    
    for a in todo_en.find_all('a', href=True): 
        if a.text:
            lista_art += ('https://www.letras.mus.br' + str(a['href'])).split()
            print(lista_art)
    return lista_art

if __name__ == "__main__":
    main()