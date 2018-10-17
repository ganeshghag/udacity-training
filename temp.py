import pandas as pd

xlsx = pd.ExcelFile('classifier1.xlsx')
training_labels = pd.read_excel(xlsx, 'training_labels')
print("training_labels>>>",training_labels.values)

training_labels = training_labels.values[:,0]
print("training_labels 2>>>>",training_labels)

from sklearn.preprocessing import MinMaxScaler

#min max scaler fit_transform
#normalizes data to between 0 and 1
#SVM and K Means need scaling / normalizing
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler = MinMaxScaler()
print(scaler.fit_transform(data))




