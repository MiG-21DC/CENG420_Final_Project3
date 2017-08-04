import numpy as np


def xrange(x):
    return iter(range(x))


def nonlin(x, deriv=False):

    if deriv == True:
        return x*(1-x)

    return 1/(1+np.exp(-x))


X = np.array([[6401430239422062,0.4], [6401430239422064,0.2], [6401430239422068,0.8], [6401430239422024,0.6]])

y = np.array([[0,0,1,1]]).T

np.random.seed(1)

syn0 = (2*np.random.random((2, 1)) - 1)/100000000000000

for iter in xrange(100000):

    l0 = X
    print(l0)
    print('syn0')
    print(syn0)

    l1 = nonlin(np.dot(l0, syn0))
a

    l1_error = y - l1

    l1_delta = l1_error * nonlin(l1, True)

    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")

print(l1)

print('Training Weight')
print(syn0)