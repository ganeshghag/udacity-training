import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB

from time import time
clf = GaussianNB()
t0 = time()
clf.fit(X, Y)
print("training time:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print("predict time:", round(time()-t0, 3), "s")


print(pred)


from sklearn.metrics import accuracy_score
print(accuracy_score([1, 1, 1, 2,2,2],pred))


import matplotlib.pyplot as plt
plt.scatter([row[0] for row in X],[row[1] for row in X])

"""
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc_min_samples_split_2 = accuracy_score(labels_test,pred)
"""


