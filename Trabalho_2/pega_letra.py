import pandas as pd
import numpy as np
import sys
import progressbar
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    lista_en = []
    lista_pt = []
    links_ = []
    lista_log = []
    cont = 0
    cont2 = 0
    bar = progressbar.ProgressBar(max_value=50021)
    with open(str(sys.argv[1]+'musicas_trad.txt')) as file:
        next(file)
        for line in file:
            bar.update(cont)
            print('  ',str(cont)+") ", line)
            cont += 1
            url, temp_en, temp_pt = pega_letra(line)
            links_ += url.split()
            if len(temp_en) == len(temp_pt):
                lista_en += temp_en
                lista_pt += temp_pt
                lista_log += str("ok").split()
                print('ok')
            else:
                lista_log += str("nok").split()
                print('nok')
            cont2 += 1
            if cont2 == 1000:
                #faz dicionario, depois dataframe, aí salva no disco
                dicionario = {'en_us':lista_en, 'pt_BR':lista_pt}
                data_set = pd.DataFrame(dicionario)
                data_set.to_csv(str(sys.argv[1]+'dataset.txt'), sep='\t', mode='w', index=False)
                dicionario_log = {'link':links_, 'ok?':lista_log}
                log = pd.DataFrame(dicionario_log)
                log.to_csv(str(sys.argv[1]+'log.txt'), sep=';', mode='w', index=False)
                cont2 = 0
    

def pega_letra(url):
    url = 'https://'+url
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    list_en = []
    list_pt = []

    todo_en = soup.find("div", {"class": "cnt-trad_l"})
    todo_pt = soup.find("div", {"class": "cnt-trad_r"})

    try:
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
    except:
        print("LETRAS E UMA BOSTA")
    
    return url, list_en, list_pt

if __name__ == "__main__":
    main()