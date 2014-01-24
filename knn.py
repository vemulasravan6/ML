__author__ = 'sravan'
from numpy import *
import operator

def calcDistance(obj1,obj2):
    x1 = int(obj1[1])
    y1 = int(obj1[2])
    x2 = int(obj2[1])
    y2 = int(obj2[2])
    #print x1,x2,y1,y2
    dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    #print dist
    return dist

def getLabel(dataset,index):
    #print dataset,index
    #iterating dataset till index and returning its label
    obj = dataset[index]
    label = obj[0]
    return label

def createDataSet():
    group = [['A',1,22],['A',1,18],['B',22,0],['A',1,17],['A',1,18],['B',25,0],['B',27,0.1],['C',12,5],['C',12,4]]
    return group

def getMaxOccurLabel(label_list):
    label_dict={}
    for label in label_list:
        if label_dict.has_key(label)==False:
            label_dict[label]=1
        else:
            label_dict[label]=label_dict[label]+1
    sorted_x = sorted(label_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    max_occur_label = sorted_x[0][0]
    return max_occur_label

def knn(dataset,obj,k):
    if k>len(dataset):
        print 'Dataset size : '+str(len(dataset))
        print 'K should be less than dataset size, given K size as : '+str(k)
        return False
    distances={}
    sorted_x={}
    i=0
    for item in dataset:
        #print item
        dist = calcDistance(item,obj)
        distances[i] = int(dist)
        i+=1
    print distances
    #will have index and distance from object(index,distance)
    sorted_x = sorted(distances.iteritems(), key=operator.itemgetter(1))
    #print sorted_x
    cnt=0
    labels_list=[]
    #index,distance
    while cnt<k:
        tupple = sorted_x[cnt]
        index = tupple[0]
        label = getLabel(dataset,index)
        labels_list.append(label)
        #print label
        cnt+=1
    print getMaxOccurLabel(labels_list)
    return

dataset = createDataSet()
obj=['unknown',1,5]
knn(dataset,obj,3)
