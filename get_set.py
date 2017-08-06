import csv

from random import Random
import numpy as np

random = Random()
pointset = []
data = ()
key = []
dataset = []

def get_data():
    random = Random()
    dataset = []
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            point = [float(row[1]), float(row[2])]
            if row[3] == '0':
                key = [1,0]
            else:
                key = [0,1]
            dataset.append([point,key])

    random.shuffle(dataset)
    # print(dataset)
    dataset = np.array(dataset)

    test_size = 0.1

    testing_size = int(test_size*len(dataset))

    train_x = list(dataset[:, 0][:-testing_size])
    train_y = list(dataset[:, 1][:-testing_size])

    test_x = list(dataset[:, 0][-testing_size:])
    test_y = list(dataset[:, 1][-testing_size:])
    return train_x,train_y,test_x,test_y


