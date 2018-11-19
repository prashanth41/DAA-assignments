import math
import numpy as np
import random
from random import randint


#n is the number of shifts
n=30
dic={}

def testCases(n):

	

	for i in range(1,n+1):

		start=randint(1,120)
		end=start+5

		dic[i]=[start,end]

	return dic

#print(testCases(20))



# intervals=[]

# for i in dic.values():
# 	intervals.append(i)

# #print(intervals)

# sortedIntervals=sorted(intervals, key=lambda x: (x[1]))
# #print(sortedIntervals)

# committeeCount=0
# temp=sortedIntervals

# supervisoryCommittee=[]


def main():

	dic=testCases(n)
	intervals=[]

	for i in dic.values():
		intervals.append(i)

	#print(intervals)

	sortedIntervals=sorted(intervals, key=lambda x: (x[1]))

	#sortedIntervals=[[1, 6], [3, 8], [11, 16], [12, 17], [17, 22], [17, 22], [17, 22], [21, 26], [25, 30], [25, 30]]
	print(sortedIntervals)

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


	return supervisoryCommittee




for i in range(1000):

	print(i)
	print(main())

