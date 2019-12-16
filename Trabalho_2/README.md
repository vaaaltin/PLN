# LSTM approach for english-portuguese translation

## Dataset

The dataset is a alligned corpus, constructed from all song of the [Letras](https://www.letras.mus.br/).

Patterns were founded in the HTML, so they were reached utilizing BeautifulSoup4 library in Python.


1. A total of 936 artists of all languages
2. Then to get only the songs of interest, which is, musics with already translated "x" to "portuguese" languages, and, with alligned corpus
3. With all this songs a filter has to be made, since this website contains songs from artits from all around the world, this filter used Polyglot library, to identifies which language the musics are.

The code sequence are as follows:

`python3 pega_artista.py <caminho para salvar>`

`python3 pega_musica.py <caminho onde os artistas foram salvos>`

`python3 pega_letra.py <caminho onde as musicas foram salvas>`


The dataset used in all models contains 20k setences, 80/20 train/test split and a random state of 12.


## RNN Model

The LSTM with the bests results is as follows:

### Defined NMT layers
> model = Sequential()
> model.add(Embedding(src_vocab, n_units, input_length=src_timesteps, mask_zero=True))
> model.add(Dropout(rate=0.7))
> model.add(LSTM(n_units))
> model.add(RepeatVector(tar_timesteps))
> model.add(LSTM(n_units, return_sequences=True))
> model.add(TimeDistributed(Dense(tar_vocab, activation='softmax')))


### Algorithm training model:
* 50 epochs
* Batch size of 64
* Validation set of 30%
* Checkpoint saving only the best epoch
* Model = min
