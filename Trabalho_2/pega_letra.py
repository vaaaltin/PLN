import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    arquivo = open(str(argv[1])+'link.txt', 'r')
    letras = arquivo.read()

    for x in letras:
        pega_letra(x)

def pega_letra(url):
    html = urlopen(url)
    soup = BeautifulSoup(html.read())
    list_en = []
    list_pt = []

    todo_en = soup.find("div", {"class": "cnt-trad_l"})
    todo_pt = soup.find("div", {"class": "cnt-trad_r"})

    #pega a letra em ingles
    tit_en = str(todo_en.findNext("h3"))
    tit_en = tit_en.replace("<h3>", "")
    tit_en = tit_en.replace("</h3>", "")
    list_en.append(tit_en)

    letra_en = todo_en.findAll('span')
    for x in letra_en:
        y = str(x)
        y = y.replace("<span>","")
        y = y.replace("</span>",".")
        list_en.append(y)

    #print(list_en)

    #pega a letra em portugues
    tit_pt = str(todo_pt.findNext("h3"))
    tit_pt = tit_pt.replace("<h3>", "")
    tit_pt = tit_pt.replace("</h3>", "")
    list_pt.append(tit_pt)

    letra_pt = todo_pt.findAll('span')
    for x in letra_pt:
        y = str(x)
        y = y.replace("<span>","")
        y = y.replace("</span>",".")
        list_pt.append(y)

    #print(list_pt)

    #converte para zip, depois para lista, e depois em dataframe
    dataset = zip(list_en, list_pt)
    dataset = list(dataset)
    data_set = pd.DataFrame(dataset, columns=['en_US', 'pt_BR'])
    #data_set
    arq = open()




if __name__ == "__main__":
    main()