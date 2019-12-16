# LSTM approach for english-portuguese translation

## Dataset

The dataset is an alligned corpus, constructed from all song from [Letras](https://www.letras.mus.br/) website.

Patterns were founded in the HTML, so they were reached utilizing BeautifulSoup4 library in Python.


1. A total of 936 artists of all languages.
2. Then to get only the songs of interest, which is, musics with already translated "x" to "portuguese" languages, and, with alligned corpus.
3. With all this songs a filter has to be made, since this website contains songs from artits from all around the world, this filter used Polyglot library, to identifies which language the musics are.

The code sequence are as follows:

`python3 pega_artista.py <path to save>`

`python3 pega_musica.py <same path as above>`

`python3 pega_letra.py <same path as above>`


The dataset used in all models contains 20k sentences, 80/20 train/test split and a random state of 12.


## RNN Model

The LSTM with the bests results is as follows:

### Defined NMT layers
> ![NMT Layers](https://github.com/vaaaltin/PLN/blob/master/Trabalho_2/model1.png)


### Algorithm hyper-parameters:
* 50 epochs
* Batch size of 64
* Validation set of 30%
* Checkpoint saving only the best epoch
* Model = min
