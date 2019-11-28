import pandas as pd
import numpy as np
import sys
import progressbar
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    lista_musicas_trad = []
    i = 0
    with open(str(sys.argv[1]+'artistas.txt')) as file:
        for line in file:
            lista_musicas_trad += pega_musicas(line)

            dicionario = {'links_musicas_trad':lista_musicas_trad}
            data_set_musicas = pd.DataFrame(dicionario)
            data_set_musicas.to_csv(str(sys.argv[1]+'/musicas_trad.txt'), sep='\t', mode='w', index=False)
            i+=1

def pega_musicas(url):
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')

    lista_mus_trad = []
    todo_en = soup.findAll("a", {"data-action": "translation"})
    if(todo_en):
        url2 = url.replace("\n","")+'traducoes.html'
        html2 = urlopen(url2)
        soup2 = BeautifulSoup(html.read(), 'html.parser')
        todo_tr = soup2.findAll("a", {"class": "song-name"})
        print(url2)
        for a in todo_tr:
            print(a)
            if a.text:
                link = ('https://www.letras.mus.br' + str(a['href'])).split()
                print(link)
                html2 = urlopen(link[0])
                soup2 = BeautifulSoup(html2.read(), 'html.parser')
                todo_en_trad = soup2.findAll("a", {"data-tt": "Tradução"})
                for a_trad in todo_en_trad:
                    link_trad = ('https://www.letras.mus.br' + str(a_trad['href'])).split()

                    if '/traducao.html' in link_trad[0]:
                        lista_mus_trad += link_trad
                        print(link_trad)
            
    return lista_mus_trad


if __name__ == "__main__":
    main()