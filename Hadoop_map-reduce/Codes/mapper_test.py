#!/usr/bin/env python3

import sys
import re
#import nltk
import string
#from nltk.corpus import stopwords


# In[12]:


#stop = set(stopwords.words('english')) #set of stopwords
#sno = nltk.stem.SnowballStemmer('english') #initialising the snowball stemmer
def cleanhtml(sentence): #function to clean the word of any html-tags
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    return cleantext
def cleanpunc(sentence): #function to clean the word of any punctuation or special characters
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    return  cleaned


# In[13]:



docs=[]
label=[]
for line in sys.stdin:
    temp=line.split('\t')
    label.append(temp[0].strip().split(','))
    docs.append(temp[1])


# In[14]:


str1=' '
final_string=[]
s=''
for i in range(len(docs)):
    filtered_sentence=[]
    sent=cleanhtml(docs[i]) # remove HTMl tags
    for w in sent.split():
        for cleaned_words in cleanpunc(w).split():
            if((cleaned_words.isalpha()) & (len(cleaned_words)>2)):    
                if(cleaned_words.lower()):
                    s=(cleaned_words.lower())
                    print('%s\t%s\t%s' % (s+' ',str(i),1))
                else:
                    continue
            else:
                continue 


