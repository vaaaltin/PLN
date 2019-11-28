import pandas as pd
import numpy as np
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    lista_musicas = []
    with open(str(sys.argv[1]+'artistas.txt')) as file:
        next(file)
        for line in file:
            lista_musicas += pega_musicas(line)
    
    dicionario = {'links_musicas_trad':lista_musicas}
    data_set_musicas = pd.DataFrame(dicionario)
    data_set_musicas.to_csv(str(sys.argv[1]+'/musicas_trad.txt'), sep='\t', mode='w', index=False)

def pega_musicas(url):
    lista_mus_trad = []

    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    todo_en = soup.findAll("a", {"data-action": "translation"})
    
    if(todo_en):
        
        url2 = url.replace("\n","")+'traducoes.html'
        html2 = urlopen(url2)
        soup2 = BeautifulSoup(html2.read(), 'html.parser')
        todo_tr = soup2.findAll("a", {"class": "song-name"})
        for a in todo_tr:
            musica = ('https://www.letras.mus.br'+str(a['href'])).split()
            lista_mus_trad += musica
            print(musica)
    return lista_mus_trad


if __name__ == "__main__":
    main()