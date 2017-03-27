'''
Author:Longfei Li
       Sudan Zhang
'''
from math import *
import numpy

file=open('classification.txt','r')

data=[]
label=[]

for line in file.readlines():
    line=line.split(',')
    line=map(float,line)
    nline=[1]
    nline.extend(line[0:3])
    l=line[4]
    data.append(nline)
    label.append(l)
    
weight=[1,1,1,1]
alpha=0.01

def cal_weight(weight,data,label,alpha):
    w = numpy.matrix(weight)
    for i in range(len(data)):
        x=numpy.matrix(data[i])
        y=label[i]
        acc=1/(1+exp(y*w*x.T))
        w=(w+(alpha*acc*y*x)/len(data))
    return w

for time in range(7000):
    weight=cal_weight(weight,data,label,alpha)

print weight