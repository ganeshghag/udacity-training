# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:53:57 2018

@author: Ganesh1.Ghag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import tree

xlsx = pd.ExcelFile('classifier1.xlsx')
training_features = pd.read_excel(xlsx, 'training_features')
print("training_features",training_features.values)

training_labels = pd.read_excel(xlsx, 'training_labels')
training_labels = training_labels.values[:,0]
print("training_labels",training_labels)

test_features = pd.read_excel(xlsx, 'test_features')
print("test_features",test_features.values)

test_labels = pd.read_excel(xlsx, 'test_labels')
test_labels = test_labels.values[:,0]
print("test_labels",test_labels)

plt.scatter([row[0] for row in training_features.values],[row[1] for row in training_features.values])

#change this for variety of algos
#clf = GaussianNB()
#clf.fit(training_features, training_labels)
#pred = clf.predict(test_features.values)
#accuracy_score 0.8333333333333334

clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_features, training_labels)
pred = clf.predict(test_features.values)
#accuracy_score 0.8333333333333334

print("preds.raw",pred)
from sklearn.metrics import accuracy_score
print("accuracy_score",accuracy_score(test_labels,pred))