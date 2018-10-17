# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:53:57 2018

@author: Ganesh1.Ghag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])
print("TRAINING DATA",X)
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print("LABELS IDENTIFIED:",kmeans.labels_)

testdata = [[0, 0], [4, 4]]
print("TESTDATA",testdata)

print("")
print("*********** OUTPUTS *********")
pred = kmeans.predict(testdata)
print("PREDICTED LABELS",pred)
print("CLUSTER CENTRES",kmeans.cluster_centers_)

