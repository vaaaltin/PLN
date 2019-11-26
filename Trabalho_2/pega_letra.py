import pandas as pd
import numpy as np
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    lista_en = []
    lista_pt = []
    links_ = []
    lista_log = []
    cont = 0
    with open(str(sys.argv[1]+'links.txt')) as file:
        for line in file:
            print(cont,") ", line)
            cont += 1
            url, temp_en, temp_pt = pega_letra(line)
            links_ += url.split()
            if len(temp_en) == len(temp_pt):
                lista_en += temp_en
                lista_pt += temp_pt
                lista_log += str("ok").split()
            else:
                lista_log += str("nok").split()
    
    #faz dicionario, depois dataframe, aí salva no disco
    dicionario = {'en_us':lista_en, 'pt_BR':lista_pt}
    data_set = pd.DataFrame(dicionario)
    data_set.to_csv(str(sys.argv[1]+'dataset.txt'), sep='\t', mode='w', index=False)
    print(links_)
    print(lista_log)
    dicionario_log = {'link':links_, 'ok?':lista_log}
    log = pd.DataFrame(dicionario_log)
    log.to_csv(str(sys.argv[1]+'log.txt'), sep=';', mode='w', index=False)
    print(lista_log)

def pega_letra(url):
    #print(url)
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
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

    return url, list_en, list_pt

if __name__ == "__main__":
    main()