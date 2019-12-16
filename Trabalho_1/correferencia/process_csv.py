import pandas as pd

def readData():
    try:
        df = pd.read_csv('data.txt', sep = '\t', encoding = 'ISO-8859-1')
        return df

    except:
        raise SystemExit('cant read csv')


def getSentences():
    df = readData()
    sentences = []
    sentence = ''

    for index, row in df.iterrows():
        if row['Index'] == '0':
            sentences.append(sentence)
            sentence = ''

        sentence += '{} '.format(row['Coluna_1'])

    return sentences

def writeSentences():
    sentences = getSentences()
    
    f = open('sentences.txt', 'w')

    for sentence in sentences:
        f.write('{}\n'.format(sentence))

    f.close()

