import numpy as np
import matplotlib.pyplot as plt

#%%

def function(x):
    return (x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9])**2

#%%
def Monte_Int(function, N):
    points_x = np.random.uniform(0,1,size=(10,N))
    points_y = np.random.uniform(0,100,size=N)

    N_adentro = 0
    N_box = 0
    for i in range(N):
        if(points_y[i] <= function(points_x[:,i])):
            N_adentro += 1
        else:
            N_box += 1

    return N_adentro*100/(N_adentro + N_box)

#%%

intentos = 1000
N = 1000
valores = np.zeros(intentos)
for i in range(intentos):
    valores[i] = Monte_Int(function,N)

integral = np.mean(valores)

print('El valor de la integral es: ', integral)

#%%

valorinshis = np.zeros(10000)
for i in range(10000):
    prueba_x = np.random.uniform(0,1,size=(10,N))
    valorinshis[i] = np.mean(function(prueba_x))
mi_val = np.mean(valorinshis)
mi_val

#%%
def f(x):
    return np.exp(-x*x-x)
def fun_vec(x):
    norm = np.sqrt(np.sum(x*x))
    return np.exp(-norm*norm)



def sampler(dist, N,dim, sigma_delta):

    lista = np.zeros((dim,N))
    propuesta = np.zeros(dim)
    for i in range(1,N):
        for j in range(dim):
            propuesta[j]  = lista[j,i-1] + sigma_delta * (np.random.random()-0.5)
        r = min(1,dist(propuesta)/dist(lista[:,i-1]))
        alpha = np.random.random()
        if(alpha<r):
            lista[:,i] = propuesta
        else:
            lista[:,i] = lista[:,i-1]
    return lista

#%%
x = np.linspace(-10,10)

numbers = sampler(f,10**5,1,1)

np.shape(numbers)

_ = plt.hist(Number_gen(f,10**5,1,1)[0], density='True', bins=x)
plt.plot(x,f(x))

#%%
x = np.linspace(-10,10,1000)
y = np.linspace(-10,10,1000)

xx, yy = np.meshgrid(x,y)

z = np.exp(-xx**2 - yy**2)
np.shape(z)

exp_2d_nums = Number_gen(fun_vec,10**5,2,1)

np.shape(exp_2d_nums)

_ = plt.hist2d(exp_2d_nums[0], exp_2d_nums[1], bins=100)

#%%
plt.pcolormesh(xx,yy,z)
plt.xlim(-3,3)
plt.ylim(-3,3)

#%%

I_MC = 2.27588*np.mean(np.cos(Number_gen(f,10**5,1,1)[0]))
I_MC
V_2 = np.mean(fun_vec(Number_gen(fun_vec,10**5,2,1)))



ver = fun_vec(Number_gen(fun_vec,10**5,2,1))
np.shape(ver)
