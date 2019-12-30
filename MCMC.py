import numpy as np
import matplotlib.pyplot as plt

# def verguero():
#     lista = list(range(10))*2
#     encontro = True
#     cuenta = 0
#     while encontro:
#         rand1 = int(np.random.uniform(0,20))
#         media1 = lista.pop(rand1)
#         rand2 = int(np.random.uniform(0,19))
#         media2 = lista.pop(rand2)
#         cuenta += 1
#         if media1 == media2:
#             encontro = False
#         else:
#             lista.append(media1)
#             lista.append(media2)
#     return cuenta
#
# cue = []
# for i in range(10000):
#     cue.append(verguero())
# cuentas = np.array(cue)
#
# promedio = np.mean(cuentas)
#
# promedio
# _ = plt.hist(cuentas, bins=50)
# #Ejercicio 7.1
# n_puntos=1000
# x = np.linspace(0, np.pi)
# def f(x):
#     y = 0.5 * np.sin(x)
#     if(np.isscalar(x)):# esto va a funcionar si entra un numero
#         if (x>np.pi) | (x<0):
#             y = 0
#     else: #esto va a funcionar si entra un array
#         ii = (x>np.pi) | (x<0)
#         y[ii] = 0.0
#     return y
#
# #%%
# N = 100000
# resultados = []
# sigma_delta = [1.0, 0.001, 1000.0]
#
# for delta in sigma_delta:
#     lista = [np.random.random()*np.pi]
#     for i in range(1,N):
#         propuesta  = lista[i-1] + np.random.normal(loc=0.0, scale=delta)
#         r = min(1,f(propuesta)/f(lista[i-1]))
#         alpha = np.random.random()
#         if(alpha<r):
#             lista.append(propuesta)
#         else:
#             lista.append(lista[i-1])
#     resultados.append(lista)
#
# len(resultados)
#
#
# #%%
# fig= plt.figure(figsize=(10,3))
# ax= fig.add_subplot(131)
# ax.hist(resultados[0], density=True, bins=x)
# ax.plot(x, f(x))
# ax2= fig.add_subplot(132)
# ax2.hist(resultados[1], density=True, bins=x)
# ax2.plot(x, f(x))
# ax3= fig.add_subplot(133)
# ax3.hist(resultados[2], density=True, bins=x)
# ax3.plot(x, f(x))
# plt.show()
#
# #%%
# #Ejercicio 7.2

N=100000
def dens(x, y):
    return np.exp(-0.5*(x**2/4 + y**2 +x*y/1.5))
x_lista = [np.random.random()]
y_lista = [np.random.random()]
sigma_delta = 1.0

for i in range (1,N):
    propuestax= x_lista[i-1] + sigma_delta*(np.random.random() - 0.5)
    propuestay= y_lista[i-1] + sigma_delta*(np.random.random() - 0.5)
    r= min (1.0, dens(propuestax, propuestay)/ dens(x_lista[i-1],y_lista[i-1]))
    alpha= np.random.random()
    if (alpha< r):
        x_lista.append(propuestax)
        y_lista.append(propuestay)
    else:
        x_lista.append(x_lista[i-1])
        y_lista.append(y_lista[i-1])

#%%
_ = plt.hist2d(x_lista, y_lista, bins=50)
# plt.xlim(-5,5)
# plt.ylim(-5,5)
plt.show()

#%%


x_line = np.linspace(-5,5,100)
y_line = np.linspace(-5,5,100)
x_grid, y_grid = np.meshgrid(x_line, y_line)
z_grid = dens(x_grid, y_grid)

fig, (ax0, ax1) = plt.subplots(1,2)

# grafica los puntos de la grid
im = ax0.pcolormesh(x_grid, y_grid, z_grid)
