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

xlsx = pd.ExcelFile('regression-sample1.xlsx')

training_features = pd.read_excel(xlsx, 'training_features').values
#print("training_features",training_features)

training_labels = pd.read_excel(xlsx, 'training_labels').values
#print("training_labels",training_labels)

test_features = pd.read_excel(xlsx, 'test_features').values
#print("test_features",test_features)

test_labels = pd.read_excel(xlsx, 'test_labels').values
#print("test_labels",test_labels)

#plt.scatter([row[0] for row in training_features],[row[0] for row in training_labels])
#plt.plot([row[0] for row in training_features],[row[0] for row in training_labels])

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(training_features,training_labels)
pred = reg.predict(test_features)




print("************ RESULTS **********")
print("pred",pred)
print("coef of lin regres, slope=",reg.coef_)
print("intercept of lin regres, intercept=",reg.intercept_)
print("r-squared score for training data=",reg.score(training_features,training_labels))
print("r-squared score for pred data=",reg.score(test_features,pred))  #will always be 1

#x = [row[0] for row in training_features]
#y = [row[0] for row in training_features]
#for idx, val in enumerate(x):
#    y[idx] = val * reg.coef_[0][0] + reg.intercept_[0]

#plt.plot(x,y)

#new way of output
plt.scatter([row[0] for row in test_features],[row[0] for row in test_labels])
plt.plot([row[0] for row in test_features],pred)
plt.xlabel("days in 2018")
plt.ylabel("sensex close value")
plt.show()
