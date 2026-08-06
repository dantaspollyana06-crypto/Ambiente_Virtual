import numpy as np
a= np.array(["Polly","Yasmin", "Denyse","Sara","Mariana", "Noemy"])
print (a.dtype)

b=np.array([[1,2,3,4],[5,6,7,8]])
print(b.ndim)

c=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(c.size)
#ndim só aceita até três dimensões
print(f"Tamanho {c.size}")
print(f"Número de dimensões {c.ndim}")
print(f"Formato {c.shape}")
print(f"Tipos de dados {c.dtype}")

print(".-"*40)

d= np.array([1,2,3,4,5,6,7,8,9])
new_d= d.reshape(3,3)
print(d)
print(new_d)

e=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
f= e 
f[0]=19
print(e)
print(f)

print(".-"*40)

g=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
g[0]=19
h=np.copy(g)
print(h)

print(".-"*40)

a1=np.array([1,2,3,4,])
a2=np.array([5,6,7,8,])
r1=np.concatenate((a1,a2))
r2=np.concatenate((a2,a1))
r3=np.concatenate((a1,a2,a1,a2,a1,a2))
print(r1)
print(r2)
print(r3)

print("-."*40)

b1= np.array([1,2,3,4,5,6])
result11=np.split(b1,3)
print(result11)

c1=np.array([1,2,3,4,5,6,7])
c2=np.append(a1,[8,9,10,11,12])
c2[0]=20
print(c1)
print(c2)
c1=np.delete(a1,2)
print(c1)


