#!/usr/bin/env python3

# coding: utf-8

# In[25]:


import sys
import re
#import nltk
import string
#from nltk.corpus import stopwords


# In[26]:


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


# In[27]:



docs=[]
label=[]
for line in sys.stdin:
    temp=line.split('\t')
    for l in temp[0].split(','):
        label.append(l.strip())
        docs.append(temp[1])
    


# In[28]:


str1=' '
final_string=[]
s=''
for sent in docs:
    filtered_sentence=[]
    #print(sent);
    sent=cleanhtml(sent) # remove HTMl tags
    for w in sent.split():
        for cleaned_words in cleanpunc(w).split():
            if((cleaned_words.isalpha()) & (len(cleaned_words)>2)):    
                if(cleaned_words.lower()):
                    s=(cleaned_words.lower()).encode('utf8')
                    filtered_sentence.append(s)
                else:
                    continue
            else:
                continue 
    str1 = b" ".join(filtered_sentence) 
    
    final_string.append(str1.decode("utf-8"))


# In[29]:


for i in range(len(final_string)):
    count=0
    for word in final_string[i].split():
        count=count+1;
        print('%s\t%s\t%s' % (word,label[i],1))
    print('%s\t%s\t%s' % ('ANY',label[i], count))
        
for l in label:
    print('%s\t%s\t%s' % ('PR_ANY',l, 1))

