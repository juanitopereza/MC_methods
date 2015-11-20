import numpy as np

datos = np.loadtxt('monthrg.dat')

datos_2 = datos[np.where(datos[:,3] != -99)[0]]

dat_f = np.array([datos_2[:,0]+(datos_2[:,1]/12.0),datos_2[:,3]]).T 

np.savetxt('datos_t.dat',dat_f[:,0])
np.savetxt('datos_f.dat',dat_f[:,1])
