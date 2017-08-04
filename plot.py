from sklearn import datasets
import matplotlib.pyplot as plt
import csv

pointset = []
data = ()
key = []
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        point = [row[1], row[2]]
        pointset.append(point)
        key.append(row[3])

data = (pointset,key)
x, y = data
print(x)
print(y)

plt.scatter(pointset[:,0], pointset[:,1], s=40, c=key, cmap=plt.cm.Spectral)