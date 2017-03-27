'''
Author:Longfei Li
       Sudan Zhang
'''
import random
import matplotlib.pyplot as plt

fp = open('classification.txt','r')

data, label = [],[]
for line in fp.readlines() :
    line = line.strip().split(",")
    data.append([1,float(line[0]),float(line[1]),float(line[2])])
    label.append(int(line[4]))

w = [0]
for i in range(3):
	w.append(random.random())

best_w = [0,0,0,0]

print "Initial weight: "+str(w)
alpha = 0.01

iteration = 0
v = []

while iteration < 7000:
	violation = 0
	iteration += 1
	#print iteration,
	for i in range(len(data)):
		value = sum([x*y for x,y in zip(data[i],w)])
		step = [ j * alpha for j in data[i]]
		if label[i] == 1 and value <= 0:
			w = [sum(x) for x in zip(w,step)]
			violation += 1
			break

		elif label[i] == -1 and value >= 0:
			w = [x - y for x,y in zip(w,step)]
			violation += 1
			break

	for i in range(len(data)):
		value_2 = sum([x*y for x,y in zip(data[i],w)])
		if label[i] == 1 and value_2 <= 0:
			violation += 1

		elif label[i] == -1 and value_2 >= 0:
			violation += 1


	if len(v) > 0 and violation <= min(v):
		best_w = w
		#print "IM AT IT: "+ str(iteration)

	v.append(violation)

print "Best weight: "+str(best_w)
# print v

plt.plot(v)
plt.show()


