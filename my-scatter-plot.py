# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:53:57 2018

@author: Ganesh1.Ghag
"""

import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('scatter-sample2.xlsx')
training_features = pd.read_excel(xlsx, 'training_features')
print("training_features",training_features.values)

plt.figure(figsize=(12,10))
plt.scatter([row[0] for row in training_features.values],[row[1] for row in training_features.values])

