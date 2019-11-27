import pandas as pd
import numpy as np
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    lista_musicas = []
    with open(str(sys.argv[1]+'artistas.txt')) as file:
        for line in file:
            print(line)
            lista_musicas += pega_artista(line)

    dicionario = {'links_musicas':lista_musicas}
    data_set_musicas = pd.DataFrame(dicionario)
    data_set_musicas.to_csv(str(sys.argv[1]+'/musicas.txt'), sep='\t', mode='w', index=False)

def pega_artista(url):
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    lista_mus = []
    todo_en = soup.findAll("a", {"class": "song-name"})
    
    for a in todo_en:
        if a.text:
            lista_mus += ('https://www.letras.mus.br' + str(a['href'])).split()
    return lista_mus


if __name__ == "__main__":
    main()