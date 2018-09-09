#!/usr/bin/env python3

import sys
import math


# In[38]:
f = open("train_dict", 'r')
prior_dict={}
lines = f.readlines();
for line in lines:
    line=line.strip()
    word,label,count = line.split('\t')
    if(word=="PR_ANY"):
        prior_dict[label]=int(count)
        
    elif (word[0]>='a'):
        break;
total=sum(prior_dict.values())
for key,value in prior_dict.items():
    prior_dict[key]=value/total
final_dict={}
indexprev=None
for line in sys.stdin:
    line=line.strip()
    index,label,score= line.split('\t')
    score=float(score)+math.log(prior_dict[label])
    if(index!=indexprev):
        indexprev=index
        maxscore=score
        final_dict[index]=label
    if(score>maxscore):
        maxscore=score
        final_dict[index]=label
for key,value in final_dict.items():
    print('%s\t%s' % (key,value))
    
