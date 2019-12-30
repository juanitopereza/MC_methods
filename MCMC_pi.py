import numpy as np
import matplotlib.pyplot as plt

#%%
#1.1

def direct_pi(N):
    hits = 0
    for i in range(N):
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        if(x**2 + y**2 < 1.0):
            hits +=1
    return hits

#%%
pi_child = direct_pi(10000)*4/10000
pi_child

#1.2
#%%

def markov_pi(N, delta):
    hits = 0
    x = 1.0
    y = 1.0
    for i in range(N):
        dx = np.random.uniform(-delta, delta)
        dy = np.random.uniform(-delta, delta)
        if (abs(x + dx) < 1.0 and abs(y + dy) < 1.0):
            x += dx
            y += dy
        if (x**2 + y**2) < 1.0:
            hits +=1
    return hits
#%%

pi_markov = markov_pi(4000, 0.3)*4/4000
pi_markov

#%%

#1.8

def markov_two_site(k, p0, p1):
    if(k == 0):
        l = 1
        gamma = min(1,p1/p0)
    elif(k == 1):
        l = 0
        gamma = min(1,p0/p1)
    rand = np.random.random()
    if(rand < gamma): k = l
    return k
#%%
esta = 0
cuenta = 0
for i in range(1000):
    esta = markov_two_site(esta, 0.8, 0.2)
    if esta:
        cuenta += 1

cuenta

#%%
#1.16

def reject_continuous(pf, xmin, xmax):
    acepta = True
    while acepta:
        x = np.random.uniform(xmin, xmax)
        gamma = np.random.uniform(0, 0.95)
        if (gamma > pf(x)):
            acepta = True
        else:
            acepta = False
    return x
#%%

def my_fun(x, mu=0.7, sigma=0.05):
     return 1.0/np.sqrt(2*np.pi*sigma**2) * np.exp(-(x-mu)**2/(2*sigma**2))

equiseses = []
for i in range(1000):
    equiseses.append(reject_continuous(my_fun, 0, 1))

#%%
_ = plt.hist(equiseses, density=True, bins=50)
plt.xlim(0,1)

#%%

#1.18

def gauss(sigma):
    phi = np.random.uniform(0,2*np.pi)
    gamma = -np.log(np.random.random())
    r = sigma * np.sqrt(2*gamma)
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    return x, y

#%%
X = []
Y = []
for i in range(1000):
        x, y = gauss(0.01)
        X.append(x)
        Y.append(y)

#%%
_= plt.hist(X,density=True, bins = 50)    

_= plt.hist(Y,density=True, bins = 50)
