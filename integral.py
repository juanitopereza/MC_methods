
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

#Define la función a integrar en 10 dimesiones
def funcion(a,b,c,d,e,f,g,h,i,j):
    return (a+b+c+d+e+f+g+h+i+j)**3

#Método que integra usando Monte Carlo. Tiene como entrada: función a integra, limítes inerior y superior, número de puntos para el cálcuo y número de veces que se integra. Devuelve el promedio de los valores obtenidos. 
def Integra_10D(fun, lim1, lim2, NPoints, intentos):
    resultados = []
    for i in xrange(intentos):
        a = np.random.uniform(lim1,lim2,NPoints)
        b = np.random.uniform(lim1,lim2,NPoints)
        c = np.random.uniform(lim1,lim2,NPoints)
        d = np.random.uniform(lim1,lim2,NPoints)
        e = np.random.uniform(lim1,lim2,NPoints)
        f = np.random.uniform(lim1,lim2,NPoints)
        g = np.random.uniform(lim1,lim2,NPoints)
        h = np.random.uniform(lim1,lim2,NPoints)
        i = np.random.uniform(lim1,lim2,NPoints)
        j = np.random.uniform(lim1,lim2,NPoints)
        resultados.append((lim2-lim1)**10/NPoints*sum(fun(a,b,c,d,e,f,g,h,i,j)))
    return np.mean(resultados)

N = 10000
intentos = 20
res = Integra_10D(funcion,0.0,2.0,N,intentos) #Integra la función objetivo 20 veces con 1000 puntos.
print ('Valor de la integral con {} puntos y {} intentos = {}'.format(N,intentos,res))

eNes= []
valores = []
#Calcula la integral 20 veces para N = (2,4,8,...,8192)
for i in xrange(1,14):
    n = 2**i
    valores.append(Integra_10D(funcion, 0.0, 2.0, n, intentos))
    eNes.append(n)

#Grafica el valor de la integral vs. Número de puntos
plt.plot(eNes, valores)
plt.title(u'Valor integral vs. Número de puntos')
plt.xlabel('N')
plt.ylabel('Valor I')
plt.savefig('num_integral.pdf')
plt.close()


ValorAnalitico = 1126400.0 #Valor calculado en Wolfram Mathematica.
errores = 100*abs(ValorAnalitico - np.array(valores))/ValorAnalitico #Errores porcentuales de la integral númerica
x = 1/np.sqrt(np.array(eNes))

#Grafica errores porcentuales vs. 1/sqrt(N)
plt.plot(x, errores)
plt.title('Errores porcentuales vs. $1/\sqrt{N}$')
plt.xlabel('$1/\sqrt{N}$')
plt.ylabel('Error %')
plt.savefig('err_integral.pdf')
plt.close()

