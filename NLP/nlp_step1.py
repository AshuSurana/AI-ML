import contractions
import re
from string import punctuation

def clean_text(text):
    # remove contractions
    text=contractions.fix(text)

    # make lowercase
    text=text.lower()

    # remove punctuations
    text=re.sub('[%s]'%re.escape(punctuation),'',text)

    # remove numbers
    text = re.sub(r'\w*\d\w*', '', text)

    # remove stopwords
    stopword=[stopword.strip()for stopword in open('./data/stopword_en.txt','r')]

    # return string
    return ' '.join([word for word in text.split() if word not in stopword])

text = "I read this book for the first time in 1987, and it's still one of my favorites !"

cleaned_text = clean_text(text)
print(cleaned_text)

#fixed=contractions.fix(text)
#print(fixed) 

#for stopword in open('./data/stopword_en.txt','r'):
#    print(stopword.strip())