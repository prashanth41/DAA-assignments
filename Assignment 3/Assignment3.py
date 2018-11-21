import math
import numpy as np
import random
from random import randint
import time
import matplotlib.pyplot as plt


#n is the number of shifts

dic={}

def testCases(n):
	
	for i in range(1,n+1):

		start=randint(1,2*(n))
		end=start+4

		dic[i]=[start,end]

	return dic

#print(testCases(20))



def main(n):

	dic=testCases(n)
	intervals=[]

	for i in dic.values():
		intervals.append(i)

	#print(intervals)

	sortedIntervals=sorted(intervals, key=lambda x: (x[1]))

	# print(sortedIntervals)

	committeeCount=0
	dupe=sortedIntervals

	supervisoryCommittee=[]

	#for i in range(len(sortedIntervals)):
		#print(sortedIntervals[i][0])

	a=0

	while(a<len(dupe)):

		temp=[]

		for j in range(a+1,len(dupe)):

			if dupe[j][0]<dupe[a][1]:

				temp.append(dupe[j])

		if len(temp)==0:

			supervisoryCommittee.append(dupe[a])
			a+=1

		else:

			temp=sorted(temp, key=lambda x:(x[1]))
			supervisoryCommittee.append(temp[0])

			a+=len(temp)+1

	print("length of supervisoryCommittee is "+str(len(supervisoryCommittee)))
	return supervisoryCommittee


timeForVarInput=[]

for i in range(1,1001):

	start=time.time()
	print("for input size "+str(i))
	#print(main(i))
	main(i)	
	end=time.time()
	if i%100==0:

		timeForVarInput.append(end-start)


print(timeForVarInput)


fig = plt.figure(2)
plt.plot(np.arange(0, 1000,100), timeForVarInput, color = 'blue')

plt.xticks(np.arange(0, 1000,100))
plt.xlabel('Input size', fontsize=14)
plt.ylabel('Running Time', fontsize=14)
fig.savefig('Input size vs Running time.png')
plt.show()
