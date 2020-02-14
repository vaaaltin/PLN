# LSTM approach for english-portuguese translation

## Dataset

The dataset is an alligned corpus, constructed from all song from [Letras](https://www.letras.mus.br/) website.

Patterns were founded in the HTML, so they were reached utilizing [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) library in Python.


1. The full dataset have 936 artists of all languages.
2. Then to get only the songs of interest, which is, musics with already translated "x" to "portuguese" languages, and, with alligned corpus a filter was made.
3. Since the website contains songs from artits from all around the world, I used [Polyglot](https://polyglot.readthedocs.io/en/latest/Installation.html) library, to identifies which language the musics are.

The code sequence to get the dataset are as follows:

`python3 pega_artista.py <path to save>`

`python3 pega_musica.py <same path as above>`

`python3 pega_letra.py <same path as above>`


The dataset used in all models contains 20k sentences, 80/20 train/test split and a random state of 12.


## RNN Model

The LSTM with the bests results is as follows:

### Defined NMT layers
> model = Sequential()\
> model.add(Embedding(src_vocab, n_units, input_length=src_timesteps, mask_zero=True))\
> model.add(Dropout(rate=0.7))\
> model.add(LSTM(n_units))\
> model.add(RepeatVector(tar_timesteps))\
> model.add(LSTM(n_units, return_sequences=True))\
> model.add(TimeDistributed(Dense(tar_vocab, activation='softmax')))


### Algorithm hyper-parameters:
* 50 epochs
* Batch size of 64
* Validation set of 30%
* Checkpoint saving only the best epoch
* Model = min
