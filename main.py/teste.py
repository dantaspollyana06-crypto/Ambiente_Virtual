import numpy as np
import time
import sys
print("----------------------------------")
s = range(1000)
print(sys.getsizeof(5)*len(s))
print("----------------------------------")
d = np.arange(1000)
print(d.size*d.itemsize)
print("----------------------------------")
a = np.array([1,2,3,4,5])
print(a)
print("----------------------------------")
SIZE = 1000000
L1 = range(SIZE)
L2 =range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)
start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)

start =time.time()
result = A1+A2
print((time.time()-start)*1000)
print("----------------------------------")
minha_matriz = np.array([[1,2,3],[4,5,6]])
print(minha_matriz)
print(minha_matriz.shape)
print("----------------------------------")
meu_tensor = np.array([[[1,2,3],[0,1,0]],[[1,2,3],[0,1,0]],[[1,2,3],[0,1,0]]])
print(meu_tensor)
print(meu_tensor.shape)
