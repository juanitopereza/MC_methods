import numpy as np
import matplotlib.pyplot as plt

def funcion (n):
    x= []
    y= []
    x.append(0)
    y.append(0)
    dx = []
    dy = []
    for i in range(1,n):
        np.random.seed(None)
        numx=(np.random.random()- 0.5) * 2
        numy=(np.random.random() - 0.5) * 2
        deltax= numx/np.sqrt(numx ** 2 + numy **2)
        deltay= numy/np.sqrt(numx ** 2 + numy **2)
        dx.append(deltax)
        dy.append(deltay)
        x.append(x[i -1] + deltax)
        y.append(y[i -1] + deltay)
    return np.array(x),np.array(y), np.array(dx), np.array(dy)

#%%
for i in range(31):
    x, y, dx, dy = funcion(1000)
    plt.plot(x,y)
plt.show()

#%%
print("Si es la esperada, ya que la mayoria de caminatas aleatorias quedaron alrededor de cero. Hay casos especiales que de igual manera se pueden entender como propios de la caminata aleatoria.")
def r_cuadrado (n):
    list_R2=[]
    k = int(np.sqrt(n))
    for i in range (k):
        x,y, dx, dy= funcion(n)
        R2 = np.sum(dx)**2 + np.sum(dy)**2
        # print(r2)
        list_R2.append(R2)
    return np.mean(np.array(list_R2))

mean_R2 = r_cuadrado(1000)
print(mean_R2)

#%%

def funcion3D (n):
    x= []
    y= []
    z= []
    x.append(0)
    y.append(0)
    z.append(0)
    dx = []
    dy = []
    dz = []
    for i in range(1,n):
        np.random.seed(None)
        numx=(np.random.random()- 0.5) * 2
        numy=(np.random.random() - 0.5) * 2
        numz=(np.random.random() - 0.5) * 2
        deltax= numx/np.sqrt(numx ** 2 + numy **2 + numz ** 2)
        deltay= numy/np.sqrt(numx ** 2 + numy **2 + numz ** 2)
        deltaz= numz/np.sqrt(numx ** 2 + numy **2 + numz ** 2)
        dx.append(deltax)
        dy.append(deltay)
        dz.append(deltaz)
        x.append(x[i -1] + deltax)
        y.append(y[i -1] + deltay)
        z.append(z[i -1] + deltaz)
    return np.array(x),np.array(y),np.array(z), np.array(dx), np.array(dy), np.array(dz)

from mpl_toolkits.mplot3d import Axes3D

x,y,z,dx,dy,dz = funcion3D(100)
x2,y2,z2,dx2,dy2,dz2 = funcion3D(100)
x3,y3,z3,dx3,dy3,dz3 = funcion3D(100)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z)
ax.plot(x2,y2,z2)
ax.plot(x3,y3,z3)
plt.show()
#%%

def r_cuadrado_3d (n):
    list=[]
    k = int(np.sqrt(n))
    for i in range (k):
        x,y,z, dx, dy, dz= funcion3D(n)
        r2 = np.sum(dx)**2 + np.sum(dy)**2 + np.sum(dz)**2
        # print(r2)
        list.append(r2)
    return np.mean(np.array(list))

mean_R2 = r_cuadrado_3d(1000)
print(mean_R2)

#%%

x,y, dx, dy = funcion(1000)

r2 = np.sum(dx)**2 + np.sum(dy)**2

suma=0

for valor in dx:
    suma += np.sum(valor*dy)
mean_dxdy = suma/1000**2

mean_dxdy/r2

#%%
def punto6(n):
    k = int(np.sqrt(n))
    result = []
    for i in range(k):
        x,y, dx, dy = funcion(n)
        r2 = np.sum(dx)**2 + np.sum(dy)**2
        suma = 0
        for valor in dx:
            suma += np.sum(valor*dy)
        mean_dxdy = suma/n**2
        result.append(mean_dxdy/r2)
    return np.mean(np.array(result))

punto6(100)

#%%
# Punto 7
enes = np.array([10,100,1000,10000])

l_rms = []

for n in enes:
    l_rms.append(r_cuadrado(n))

rms = np.array(l_rms)

plt.loglog(enes, rms)
plt.loglog(enes, np.sqrt(enes))
plt.show()
#%%
# Punto 2

def decay(N_0, lamb):
    N = N_0
    t = 0
    Ns = []
    tiempos = []
    Ns.append(N_0)
    tiempos.append(t)
    deltas = []
    deltas.append(0)
    while N > 0:
        delta_N = 0
        for i in range(N):
            np.random.seed(None)
            r_i = np.random.random()
            if (r_i < lamb):
                delta_N += 1
        deltas.append(delta_N)
        t += 1
        tiempos.append(t)
        N -= delta_N
        Ns.append(N)
    return np.array(tiempos), np.array(Ns), np.array(deltas)

eNes = [10,100,1000,10000]
lambdas = [0.1, 0.2, 0.3, 0.5, 0.8]

for cosa in eNes:
    t, N, delta = decay(cosa, 0.3)
    plt.semilogy(t, N)
plt.show()

for cosa in lambdas:
    t, N, delta = decay(1000, cosa)
    plt.semilogy(t, N)
plt.show()

t, N, delta = decay(1000,0.3)
plt.loglog(N,delta)
plt.show()
print("Punto 5")
print ("La probabilidad que el proceso ocurra, depende de la cantidad de particulas en cada instante de tiempo. Existe una ecuacion diferencial cuya solucion es una funcion exponencial, por tanto tiene todo el sentido.")
print("Punto 6")
print("Si la funcion fuese potencial, deberia verse una linea recta en una grafica log vs log; en este caso se puede ver que la recta se ve solo en funcion del semilog por la ecuacion.")
