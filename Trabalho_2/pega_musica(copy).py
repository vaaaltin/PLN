import pandas as pd
import numpy as np
import sys
import progressbar
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    lista_musicas_trad = []
    bar = progressbar.ProgressBar(max_value=937)
    i = 0
    # with open(str(sys.argv[1]+'artistas.txt')) as file:
    #     for line in file:
    #         bar.update(i)
    #         print(line)
    #         lista_musicas_trad += pega_musicas(line)
            
    #         dicionario = {'links_musicas_trad':lista_musicas_trad}
    #         data_set_musicas = pd.DataFrame(dicionario)
    #         data_set_musicas.to_csv(str(sys.argv[1]+'/musicas_trad.txt'), sep='\t', mode='w', index=False)
    #         i+=1

    pega_musicas('https://www.letras.mus.br/avioes-do-forro/')

def pega_musicas(url):
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')

    lista_mus_trad = []

    todo_en = soup.findAll("a", {"data-action": "translation"})
    
    if(todo_en):
        print(todo_en)
        url2 = url+'traducoes.html'
        html2 = urlopen(url2)
        soup2 = BeautifulSoup(html.read(), 'html.parser')

        todo_tr = soup.findAll("a", {"class": "song-name"})
        for a in todo_tr:
            print(a)
            
    #return lista_mus_trad


if __name__ == "__main__":
    main()