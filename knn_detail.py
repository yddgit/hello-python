#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import csv
import random
import operator
from sklearn import datasets

'''
生成数据集文件
'''
def generateDataSet() :
    with open('iris.txt', 'w') as f:
        iris = datasets.load_iris()
        num = len(iris.data)
        for x in range(num):
            line = '%s,%s,%s,%s,%s\n' % (iris.data[x][0], iris.data[x][1], iris.data[x][2], iris.data[x][3], iris.target_names[iris.target[x]])
            f.write(line)

'''
计算两个结点的距离
'''
def distance(i1, i2):
    distance = 0
    for x in range(4):
        distance += pow((i1[x] - i2[x]), 2)
    return math.sqrt(distance)

'''
获取测试数据在训练集合中的k个邻居
'''
def getNeighbors(trainingSet, testInstance, k):

    distances = []
    for i in range(len(trainingSet)):
        dis = distance(testInstance, trainingSet[i])
        distances.append((trainingSet[i], dis))
    distances.sort(key=operator.itemgetter(1))

    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    
    return neighbors

'''
获取测试数据的结果种类
'''
def getResult(neighbors):
    
    votes = {}
    for i in range(len(neighbors)):
        result = neighbors[i][-1]
        if result in votes:
            votes[result] += 1
        else:
            votes[result] = 1
    
    sortedVotes = sorted(votes, key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0]

'''
验证knn算法的正确率
'''
def knn():
    trainingSet = []
    testSet = []
    splitRatio = 0.75
    filename = 'iris.txt'
    with open(filename, 'r') as datafile:
        lines = csv.reader(datafile)
        dataSet = list(lines)
        for x in range(len(dataSet) - 1):
            for y in range(4):
                dataSet[x][y] = float(dataSet[x][y])
            if(random.random() < splitRatio):
                trainingSet.append(dataSet[x])
            else:
                testSet.append(dataSet[x])
    print 'trainingSet len: %s' % len(trainingSet)
    print 'testSet len: %s' % len(testSet)

    results = []
    for i in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[i], 3)
        result = getResult(neighbors)
        results.append(result)
        print ('expected: %s, predicted: %s' % (testSet[i][-1], result))

    correct = 0
    for i in range(len(results)):
        if(results[i] == testSet[i][-1]):
            correct += 1
    print 'percentage of correction: ', correct/float(len(results))

knn()