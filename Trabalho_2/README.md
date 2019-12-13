# LSTM approach for english-portuguese translation

## Dataset

 The dataset is a alligned corpus, constructed from all song of the [Letras](https://www.letras.mus.br/). This songs were reached utilizing BeautifulSoup4 library in Python.

python3 pega_artista.py <caminho para salvar>
python3 pega_musica.py <caminho onde os artistas foram salvos>
python3 pega_letra.py <caminho onde as musicas foram salvas>

O melhor modelo da LSTM ficou:
Dataset com 20k sentenças, split de 80/20 e random_state = 12

### Defined NMT layers
> model = Sequential()\
> model.add(Embedding(src_vocab, n_units, input_length=src_timesteps, mask_zero=True))\
> model.add(Dropout(rate=0.7))\
> model.add(LSTM(n_units))\
> model.add(RepeatVector(tar_timesteps))\
> model.add(LSTM(n_units, return_sequences=True))\
> model.add(TimeDistributed(Dense(tar_vocab, activation='softmax')))\

### Treinamento
filename = 'model1.h5'\
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')\
history = model.fit(trainX, trainY, epochs=50, batch_size=64, validation_data=(testX, testY), callbacks=[checkpoint], verbose=2)\