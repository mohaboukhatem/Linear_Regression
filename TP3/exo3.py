import numpy as np

np.random.seed(200)
A=np.random.randint(1,2,[3 ,3])

print(A)



print(A.mean(axis=0))

print(A.std(axis=0))