'''
Created on Feb 24, 2021

@author: shalomc
'''


# sudo apt install python3-nltk wordnet-dev wordnet-base wordnet-gui



import random

import nltk
from nltk.corpus import wordnet as wn
from nltk.text import Text

print('Downloading word lists - please wait')

nltk.download('wordnet')
nltk.download('words')
nltk.download('punkt')
nltk.download('universal_tagset')

print('Building word lists - please wait')
verbs = [a[0] for a in nltk.corpus.brown.tagged_words(tagset='universal') if a[1] == 'VERB']
nouns = [a[0] for a in nltk.corpus.brown.tagged_words(tagset='universal') if a[1] == 'NOUN']
dets  = [a[0] for a in nltk.corpus.brown.tagged_words(tagset='universal') if a[1] == 'DET']
pronouns = [a[0] for a in nltk.corpus.brown.tagged_words(tagset='universal') if a[1] == 'PRON']
prts = [a[0] for a in nltk.corpus.brown.tagged_words(tagset='universal') if a[1] == 'PRT']
# CONJ, ADP
class GrammarRule:
    def __init__(self):
        self.alternatives = []
        
    
startSymbol = 'Sentence'
finalsSymbols=['*PRON', '*NOUN', '*DET', '*VERB', '*PRT']
wordLists = {'*PRON':pronouns, '*NOUN':nouns, '*DET':dets, '*VERB':verbs, '*PRT':prts}
rules = {
    'Sentence' : ['NP+VP'],
    'NP' :  ['*PRON', '*DET+Nominal'],
    'Nominal' : ['Nominal+*NOUN', '*NOUN'],
    'VP' : ['*VERB', '*VERB+NP', '*VERB+NP+PP', '*VERB+PP'],
    'PP' : ['*PRT', 'NP']
    }

def generate(symbol = startSymbol):
    words = []
    rule = rules[symbol]
    choice = random.choice(rule)
    sequence = choice.split('+')
    
    for item in sequence:
        if item in finalsSymbols:
            wordList = wordLists[item]
            word = random.choice(wordList)
            words.append(word)
        else:
            words.extend(generate(item))
    
    return words

def sentence():
    words = generate()
    result = words[0].capitalize()
    for w in words[1:]:
        result = result + ' ' + w.lower()
        
    result = result + '.'
    return result 
    


if __name__ == '__main__':
    for sents in range(20):
        print(sentence())

