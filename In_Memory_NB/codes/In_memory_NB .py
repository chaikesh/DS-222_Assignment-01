
# coding: utf-8

# In[9]:



import string
import collections
import numpy as np
import re
import pandas as pd


f=open('full_train.txt','r')

d=f.readlines()
docs=[]
label=[]
for line in d:
    temp=line.split('\t')
    
    for l in temp[0].split(','):
        label.append(l.strip())
        docs.append(temp[1])

train_set=pd.DataFrame({})
train_set['label']=label
train_set['docs']=docs

def cleanhtml(sentence): 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    return cleantext
def cleanpunc(sentence): 
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    return  cleaned



str1=' '
final_string=[]
s=''
for sent in train_set['docs'].values:
    filtered_sentence=[]
    sent=cleanhtml(sent)
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
    
    final_string.append(str1)
train_set['CleanedDocs']=final_string 
train_set['CleanedDocs']=train_set['CleanedDocs'].str.decode("utf-8")



train_set['label']=pd.Categorical(train_set.label)
train_set['coded_label'] = train_set.label.cat.codes
decoded_label_list=train_set.label.cat.categories
total_labels=len(set(train_set.coded_label.values))




word_count_list=[]
for l in range(total_labels):
    word_count_list.append(collections.Counter([y for x in train_set[train_set['coded_label']==l].CleanedDocs.values.flatten() for y in x.split()]))

[y for x in train_set[train_set['coded_label']==l].CleanedDocs.values.flatten() for y in x.split()]


priorlist=[]
for l in range(total_labels):
    priorlist.append((train_set[train_set['coded_label']==l]).shape[0]/train_set.shape[0])









total_word_list=[]
vocab_total=[]
for l in range(total_labels):
    total_word_list.append(sum(word_count_list[l].values()))
    vocab_total.extend((word_count_list[l].keys()))
vocab_total=set(vocab_total)
vocab_total_length=len(vocab_total)





f=open('full_train.txt','r')
d=f.readlines()
docs=[]
label=[]
for line in d:
    temp=line.split('\t')
    label.append(temp[0].strip().split(','))
    docs.append(temp[1])

dev_set=pd.DataFrame({})
dev_set['label']=label
dev_set['docs']=docs












str1=' '
final_string=[]
s=''
for sent in dev_set['docs'].values:
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
    
    final_string.append(str1)
dev_set['CleanedDocs']=final_string 
dev_set['CleanedDocs']=dev_set['CleanedDocs'].str.decode("utf-8")

vocab_counter=collections.Counter(vocab_total)

smoothing=0.001


from datetime import datetime
start=datetime.now()
def log_prob(x):
    ans=[];
    for l in range(total_labels):
        if(word_count_list[l][x]!=0):
            count=word_count_list[l][x]+smoothing
        elif(vocab_counter[x]!=0):
            count=smoothing
        else:
            count=0
            return np.zeros(total_labels)
        ans.append(np.log(count/(total_word_list[l]+(smoothing*vocab_total_length))))
    return np.array(ans)

pred=[]
for d in dev_set.CleanedDocs.values:
    total_prob=np.log(priorlist)
    wordlist=d.split()
    for w in wordlist:
        total_prob=total_prob+log_prob(w)
    pred.append(decoded_label_list[np.argmax(total_prob)])
dev_set['pred']=pred
accuracy
correct=0
for i in range(dev_set.shape[0]):
    if(dev_set['pred'][i] in dev_set['label'][i]):
        correct=correct+1








