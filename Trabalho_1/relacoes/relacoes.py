import pandas as pd
import spacy

def readData():
    try:
        data = pd.read_csv('harem.csv', sep=';')
        return data
    except:
        raise SystemExit('cant read csv')

if __name__ == '__main__':
    harem = readData()
    nlp = spacy.load('pt_core_news_sm')
    i = 0
    f = open('result.txt', 'w')
    
    for sentence in harem['SENTENCE']:
        rawSentence = sentence.replace('_', ' ')
        arg1 = harem["ARGUMENT_1"][i]
        arg2 = harem["ARGUMENT_2"][i]
        doc = nlp(rawSentence)
        hasFoundRelation = False
        result = ''
        for token in doc:
            if hasFoundRelation:
                print('{} -- {} -- {}'.format(arg1, result, arg2))
                f.write('{}\n'.format(result))
                break
            
            # arg1
            if token.head.text in arg1:
                for token2 in doc:
                    if token2.head.text in arg2 and token.text not in arg2 and (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result = token2.text
                        hasFoundRelation = True 
                        break
                    if token2.text in arg2 and token.head.text not in arg2 and  (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result = token2.head.text
                        hasFoundRelation = True
                        break

            if token.text in arg1:
                for token2 in doc:
                    if token2.head.text in arg2 and token.text not in arg2 and  (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result = token2.text
                        hasFoundRelation = True
                        break
                    if token2.text in arg2 and token.head.text not in arg2 and  (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result= token2.head.text
                        hasFoundRelation = True
                        break

            # arg2
            if token.head.text in arg2:
                for token2 in doc:
                    if token2.head.text in arg1 and token.text not in arg1 and  (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result = token2.text
                        hasFoundRelation = True 
                        break
                    if token2.text in arg1 and token.head.text not in arg1 and  (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result = token2.head.text
                        hasFoundRelation = True
                        break

            if token.text in arg2:
                for token2 in doc:
                    if token2.head.text in arg1 and token.text not in arg1 and  (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result = token2.text
                        hasFoundRelation = True
                        break
                    if token2.text in arg1 and token.head.text not in arg2 and  (token2.dep_ == 'nmod' or token2.dep_ == 'appos'):
                        result= token2.head.text
                        hasFoundRelation = True
                        break

        i += 1

    f.close()
