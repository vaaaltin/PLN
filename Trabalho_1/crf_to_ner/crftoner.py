import pandas as pd
import spacy

from sklearn.model_selection import train_test_split
from sklearn_crfsuite import CRF
from sklearn_crfsuite.metrics import flat_f1_score
from sklearn_crfsuite.metrics import flat_classification_report

#Reading the csv file
df = pd.read_csv('tweets.txt', sep='\t')

#Checking null values, if any.
df.isnull().sum()

df = df.fillna(method = 'ffill')

# POS Tag and Sentence Generator
def posTagging(df):
    nlp = spacy.load('pt_core_news_sm')
    sentences = []
    for tweet in df['tweet']:
        doc = nlp(tweet)
        temp_sent = []
        for token in doc:
            if token.ent_type_ != '':
                temp_sent.append( (token.text, token.pos_, '{}-{}'.format(token.ent_iob_, token.ent_type_)) )
                continue
            temp_sent.append( (token.text, token.pos_, token.ent_iob_) )

        sentences.append(temp_sent)
    return sentences

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],

        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],

        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

sentences = posTagging(df)
print(' vetor de sentencas pronto. separar conjunto de treino e teste...\n')
X = [sent2features(s) for s in sentences]
y = [sent2labels(s) for s in sentences]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
print(' conjuntos separados. iniciando treino... \n')

crf = CRF(algorithm = 'lbfgs',
         c1 = 0.1,
         c2 = 0.1,
         max_iterations = 100,
         all_possible_transitions = False)
crf.fit(X_train, y_train)

#Predicting on the test set.
y_pred = crf.predict(X_test)

f1_score = flat_f1_score(y_test, y_pred, average = 'weighted')
print(f1_score)

report = flat_classification_report(y_test, y_pred)
print(report)
