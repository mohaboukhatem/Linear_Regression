import numpy as np

X = np.random.randint(100,size=(3, 2))

X = np.concatenate((X,np.ones((X.shape[0],1))), axis = 1)
print(X)
print(X.shape[0])