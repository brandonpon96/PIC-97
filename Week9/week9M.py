from __future__ import division
import nltk 
from urllib import urlopen
from nltk.tokenize import word_tokenize
from nltk import FreqDist

url="http://www.gutenberg.org/files/863/863-0.txt"
response=urlopen(url)
raw=response.read().decode('utf8')

# print raw[:100000]
start= raw.rfind("CHAPTER I. ")
end= raw.rfind("THE END")
# print start ; print end
raw= raw[start:end:]
# print raw 

#sentence tokenizer / frequency distribution / stripping punctuation and _
tokens= nltk.word_tokenize(raw)
text=nltk.Text(tokens)

#using concordance to see differnet usages of the word "point"
print text.concordance("point")

words=[w.lower() for w in text if w.isalpha()]

port=nltk.PorterStemmer()
stems=[port.stem(t) for t in words]

# calculating occurrences of stems (post stemming)
fd=FreqDist(stems)
print fd.items()

#calculating the 30 most common words (not stems)
fd=FreqDist(words)
print fd.most_common(30)

fd2=FreqDist(words)
fd3= sorted(fd2.items(),key=lambda x:x[1], reverse=True)
print fd3[:30]

#calculating lexical diversity 
print len(fd)/len(raw)







tokens = word_tokenize(raw)