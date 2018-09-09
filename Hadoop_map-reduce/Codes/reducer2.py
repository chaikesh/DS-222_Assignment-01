#!/usr/bin/env python3

import sys
import math

f = open("train_dict", 'r')
count_dict={}
lines = f.readlines();
for line in lines:
    line=line.strip()
    word,label,count = line.split('\t')
    if(word=="ANY"):
        count_dict[label]=int(count)
        
    else:
        break;



sf=0.1
vsize=483243
prevword=None
word_class_dict={}
index_label_dict={}
word_prob={}
# input comes from STDIN (standard input)
for line in sys.stdin:
    line=line.strip()
    word,label,count = line.split('\t')
    word=word.strip();
    if(label in count_dict.keys()):
        if(word!=prevword):
            word_class_dict={}
            word_prob={}
            prevword=word
        word_class_dict[label]=int(count);
    else:
        if(bool(word_class_dict)):
            for l in count_dict.keys():
                if(word_class_dict.get(l)==None):
                    if(word_prob.get(word+'^'+l)==None):
                        word_prob[word+'^'+l]=math.log(sf/(count_dict.get(l)+sf*vsize))
                    if(index_label_dict.get(label+'^'+l)==None):
                        index_label_dict[label+'^'+l]=int(count)*word_prob[word+'^'+l]
                    else:
                        index_label_dict[label+'^'+l]=index_label_dict[label+'^'+l]+int(count)*word_prob[word+'^'+l]
                else:
                    if(word_prob.get(word+'^'+l)==None):
                        word_prob[word+'^'+l]=math.log((word_class_dict.get(l)+sf)/(count_dict.get(l)+sf*vsize))
                    if(index_label_dict.get(label+'^'+l)==None):
                        index_label_dict[label+'^'+l]= int(count)*word_prob[word+'^'+l]
                    else:
                        index_label_dict[label+'^'+l]=index_label_dict[label+'^'+l]+int(count)*word_prob[word+'^'+l]
                
for key,value in index_label_dict.items():
    index,label=key.split('^')
    score=value
 
    print('%s\t%s\t%s' % (index,label,score))
                

