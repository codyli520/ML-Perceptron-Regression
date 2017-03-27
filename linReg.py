'''
Author:Longfei Li
       Sudan Zhang
'''
import numpy

file=open('linear-regression.txt','r')
lines=file.readlines()
data=[]
label=[]
for line in lines:
    line = line.split(',')
    line = map(float, line)
    nline=[1]
    nline.extend(line[0:2])
    data.append(nline)
    label.append(line[2])

datamat=numpy.matrix(data)
labelmat=numpy.matrix(label)
weight=(((datamat.T*datamat).I*datamat.T)*labelmat.T).T
print weight