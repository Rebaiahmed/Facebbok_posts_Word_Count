import nltk
import urllib.request
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer



response = urllib.request.urlopen('http://php.net/')
nltk.download()
html = response.read()

#print (html)

#print("ok it's work")
#scrap web page content
response = urllib.request.urlopen('http://php.net/')
#***************************
html = response.read()

soup = BeautifulSoup(html,"html5lib")
#scrap the text************
text = soup.get_text(strip=True)
#*********************
tokens = [t for t in text.split()]

#print (tokens)
freq = nltk.FreqDist(tokens)

'''for key,val in freq.items():

    print (str(key) + ':' + str(val))


freq.plot(20, cumulative=False)'''

#***********************//
#*******clean the tokens***********
clean_tokens = tokens[:]
'''sr = stopwords.words('english')

for token in tokens:

    if token in stopwords.words('english'):

        clean_tokens.remove(token)'''



mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

print(sent_tokenize(mytext))
print(word_tokenize(mytext))


#**********tokenize frensh text***************
mytext = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."

print(sent_tokenize(mytext,"french"))



syn = wordnet.synsets("pain")

print(syn[0].definition())

print(syn[0].examples())



#************Stemming process*************

stemmer = PorterStemmer()

print(stemmer.stem('working'))


#***************Leamtize process*************
lemmatizer = WordNetLemmatizer()

print(stemmer.stem('stones'))

print(stemmer.stem('speaking'))

print(stemmer.stem('bedroom'))

print(stemmer.stem('jokes'))

print(stemmer.stem('lisa'))

print(stemmer.stem('purple'))

print('----------------------')

print(lemmatizer.lemmatize('stones'))

print(lemmatizer.lemmatize('speaking'))

print(lemmatizer.lemmatize('bedroom'))

print(lemmatizer.lemmatize('jokes'))

print(lemmatizer.lemmatize('lisa'))

print(lemmatizer.lemmatize('purple'))
