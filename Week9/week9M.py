from __future__ import division
import nltk 
from urllib import urlopen
from nltk.tokenize import word_tokenize
from nltk import FreqDist


url="http://www.gutenberg.org/files/863/863-0.txt"
response=urlopen(url)
raw=response.read().decode('utf8')

# print raw[:100000]
begin= raw.rfind("CHAPTER I. ")
end= raw.rfind("THE END")
# print begin ; print end
raw= raw[begin:end:]
# print raw 

#sentence tokenizer / frequency distribution / stripping punctuation and _
tokens= nltk.word_tokenize(raw)
text=nltk.Text(tokens)

#using concordance to see differnet usages of the word "point"
print text.concordance("point")

words=[w.lower() for w in text if w.isalpha()]

porter=nltk.PorterStemmer()
stems=[porter.stem(t) for t in words]

# calculating occurrences of stems (post stemming)
fdist=FreqDist(stems)
#print fdist.items()

#calculating the 30 most common words (not stems)
fdist1=FreqDist(words)
print fdist1.most_common(30)

fdist2=FreqDist(words)
fdist3= sorted(fdist2.items(),key=lambda x:x[1], reverse=True)
print fdist3[:30]

#calculating lexical diversity 
print len(fdist)/len(raw)







tokens = word_tokenize(raw)