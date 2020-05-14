import pandas as pd
import numpy as np

df = pd.read_excel('D:/Documents/R/Sem 2 Python/Automobile_data.xlsx', sheet_name = 'Sheet1')
df.drop(['index'],axis = 1, inplace = True) 
df

df.drop_duplicates(keep = False, inplace = True)
df.duplicated().sum()

df.groupby('company').price.mean()
df["price"] = df.groupby("company")["price"].transform(lambda x: x.fillna(np.mean(x)))
df.isnull().sum()

df.groupby('company').max()['average-mileage']
df.groupby('company').max()['price']

df.loc[df['price'].idxmax()]
df.loc[df['price']>np.percentile(df['price'],80)

df.groupby('body-style').price.mean()

import nltk
nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doig today? The weather is great, and python is awesome. The sky is pinkish-blue. You sholudn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))
print(word_tokenize(EXAMPLE_TEXT))

example_sent = "This is a sample sentence, showing off the stop words filteration."

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
stop_words
word_tokens

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

filtered_sentence

filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(word_tokens)
print(filtered_sentence)

from nltk.stem import PorterStemmer
ps = PorterStemmer()
example_words = ["shop","shopping","shops"]
for w in example_words:
    print(ps.stem(w))

new_text = "Raindrops are the size of bullets thundered on the castle windoes for days on end; the lake rose, the flower beds turned into muddy streams, and Hagrid's pumpkins swelled to the size of garden sheds."

words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized[:5]:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

process_content()

from nltk.corpus import wordnet

syns = wordnet.synsets("program")
print(syns[0].name())
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))

def gender_features(word):
    return {'last_letter': word[-1]}

from nltk.corpus import names
import random

labelled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])

random.shuffle(labelled_names)
featuresets = [(gender_features(n),gender) for (n, gender) in labelled_names]
train_set,  test_set = featuresets[500:], featuresets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.classify(gender_features('Bilala'))
classifier.classify(gender_features('Rohit'))
classifier.classify(gender_features('Sita'))
classifier.classify(gender_features('Aditya'))

print(nltk.classify.accuracy(classifier, test_set))