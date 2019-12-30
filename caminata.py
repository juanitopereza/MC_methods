import numpy as np
import matplotlib.pyplot as plt

#%%

datos = np.loadtxt('datos_CAMINATA.txt')
np.shape(datos)

DatosPlot1 = datos[0,:]

plt.hist(DatosPlot1)
plt.show()
plt.savefig('binomial')
plt.close()

#%%

datos.shape[0]

sumas = []
for i in range(datos.shape[0]):
    sumas.append(np.sum(datos[i,:]))
sumas

plt.hist(sumas)
plt.show()

#%%
