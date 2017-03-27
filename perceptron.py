'''
Author:Longfei Li
       Sudan Zhang
'''
from sys import argv
import random

fp = open('classification.txt','r')

data, label = [],[]
for line in fp.readlines() :
    line = line.split(",")
    data.append([1,float(line[0]),float(line[1]),float(line[2])])
    label.append(int(line[3]))

w = [0]
for i in range(3):
	w.append(random.random())

print "Initial weight: "+str(w)
alpha = 0.01

violated = True

while violated:
	for i in range(len(data)):
		#print i
		value = sum([x*y for x,y in zip(data[i],w)])

		step = [ j * alpha for j in data[i]]
		if label[i] == 1 and value < 0:
			w = [sum(x) for x in zip(w,step)]
			break
		elif label[i] == -1 and value > 0:
			w = [x - y for x,y in zip(w,step)]
			break
		if i == len(data)-1:
			violated = False


print "Final weight: "+str(w)
		
		

		


