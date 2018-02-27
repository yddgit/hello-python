#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
安装类库
  pip install numpy
  pip install scipy
  pip install sklearn
使用KNN分类算法在iris数据集上进行学习
'''
from sklearn import neighbors
from sklearn import datasets

# get knn
knn = neighbors.KNeighborsClassifier()
# load iris dataset
iris = datasets.load_iris()
#print iris
# use knn
knn.fit(iris.data, iris.target)
# predict
predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
# show predicted result
print predictedLabel