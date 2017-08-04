from sklearn import datasets
import matplotlib.pyplot as plt
import csv
import numpy as np

pointset = []
data = ()
key = []
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        point = [row[1], row[2]]
        pointset.append(point)
        key.append(row[3])

pointsetarray = np.array(pointset)
keyarray = np.array(key)
data = (pointset,key)
x, y = data
print(pointsetarray)
print(keyarray)
plt.scatter(pointsetarray[:,0], pointsetarray[:,1], s=40, c=keyarray, cmap=plt.cm.Spectral)