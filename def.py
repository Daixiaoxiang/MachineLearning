import operator 
from numpy import *

def classify(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	sqDistance = tile(inX,(dataSetSize,1))-dataSet
	sqDistMat = sqDistance**2
	sqDistSigma = sqDistMat.sum(axis = 1)
	distance = sqDistSigma**0.5
	distSorted= distance.argsort()
	classCount = {}
	for i in range(k):
		labelVote = label[distSorted[i]]
		classCount[labelVote] = classCount.get(labelVote,1)+1
	sortedClassCount = sorted(classCount.iteritems(),key = opeerator.itemgetter(1),reverse = True)
	return sortedClassCount

