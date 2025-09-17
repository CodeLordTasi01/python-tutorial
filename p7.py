'''
#program no.7
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sent = """This is a sample sentence,
showing off the stop words filtration."""
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print(word_tokens)
print(filtered_sentence)'''








'''#program no.8
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps =PorterStemmer()
sentence ="Programmers program with programming languages"
words =word_tokenize(sentence)
for w in words:
    print(w, " : ", ps.stem(w))'''







'''
#program no.9
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
txt ="Sukanya, Rajib and Naba are my good friends. "
"Sukanya is getting married next year. "
"Marriage is a big step in one’s life."
"It is both exciting and frightening. "
"But friendship is a sacred bond between people."
"It is a special kind of love between us. "
"Many of you must have tried searching for a friend "
"but never found the right one."
tokenized = sent_tokenize(txt)
for i in tokenized:
    wordsList=nltk.word_tokenize(i)
    wordsList=[w for w in wordsList if not w in stop_words]
    tagged=nltk.pos_tag(wordsList)
    print(tagged)'''






'''#program no.10
from nltk.stem import WordNetLemmatizer
lemmatizer =WordNetLemmatizer()
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("better :", lemmatizer.lemmatize("better", pos ="a"))'''







#program no.11
import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

print(documents[1])
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])


