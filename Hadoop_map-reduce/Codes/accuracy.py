#!/usr/bin/env python3


import sys
import string

ans=[]
f1=open('pred.txt','r')
f2=open('full_devel.txt','r')
d1=f1.readlines()
d2=f2.readlines()
true_label=[]
pred_label=[]
count=0
for line in d2:
    line=line.strip()
    temp=line.split('\t')
    true_label.append(temp[0].strip().split(','))
    count=count+1
print(count)
for line in d1:
    line=line.strip()
    temp=line.split('\t')
    pred_label.append(temp[1])
count=0
#del true_label[38577]
for i in range(len(true_label)):
        if(pred_label[i] in true_label[i]):
            count=count+1;
        
print(count/len(pred_label))



