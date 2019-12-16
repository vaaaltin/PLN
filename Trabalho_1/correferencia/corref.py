import pandas as pd
import spacy
import neuralcoref

def readData(filename):
    try:
        f = open(filename, 'r')
        sentences = [line for line in f.readlines()] 
        f.close()
        return sentences
    except:
        raise SystemExit('cant read data')

def writeResults(results):
    f = open('results.txt', 'w')

    for result in results:
        f.write('{}\n'.format(result))

    f.close()

if __name__ == '__main__':
    sentences = readData('translated_sentences.txt')
    nlp = spacy.load('en_core_web_sm')
    neuralcoref.add_to_pipe(nlp)
    processed_sentences = []

    for sentence in sentences:
        doc = nlp(sentence)

        if doc._.coref_clusters != []:
            print('Given text: {}'.format(sentence))
            print(doc._.coref_clusters)
            processed_sentences.append(doc._.coref_clusters)

    # writeResults(processed_sentences)
