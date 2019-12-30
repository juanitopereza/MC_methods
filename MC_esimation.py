import numpy as np
import matplotlib.pyplot as plt

#%%

pot = np.arange(13)

N = np.array([0])
N = np.append(N,2**pot)
N = np.append(N,3)
N.sort()
def prior(x):
    return 1.0

def likelihood(x, N, R):
    return 100 + np.log(x**R * (1.0 - x)**(N-R))
# norm_const: np.math.factorial(N)/(np.math.factorial(N-R)*np.math.factorial(R))


def flips(N):
    randomi = np.random.random(N)
    ii = randomi < 0.25
    flips = np.zeros(N)
    flips[ii] = 1.0
    return int(np.sum(flips))

#%%
fig = plt.figure(figsize=(25,15))

cont = 1
for ene in N:
    R = flips(ene)
    H = np.linspace(0,1,1000)
    #print("n= ", ene, "R = ", R)
    posterior = prior(H)*likelihood(H, ene, R)
    posterior = posterior - np.max(posterior)
    ax = fig.add_subplot(5,3,cont)
    ax.plot(H,np.exp(posterior))
    cont += 1
plt.show()

#%%

#Punto2

def poste(x, y):
    return 1.0 + (x-y)**2
#%%
Flashes = np.array([1, 2, 3,8,64,512])

fig2 = plt.figure(figsize=(10,10))

cont = 1
for flash in Flashes:
    x_k = np.random.uniform(-5, 5, flash)
    alpha = np.linspace(-6, 6, 1000)
    L = np.zeros(1000)
    for x in x_k:
            L += -np.log(poste(x,alpha))
    L = L - np.max(L)
    if (flash <= 8):
        ax = fig2.add_subplot(3,2,cont)
        ax.scatter(x_k, np.ones(flash))
        ax.plot(alpha,np.exp(L))
        ax.axvline(np.mean(x_k), ymin=0.1, ymax=0.9, c='r')
        ax.set_xlim(-5.1, 5.5)
        cont += 1
    else:
        ax = fig2.add_subplot(3,2,cont)
        ax.plot(alpha,np.exp(L))
        ax.axvline(np.mean(x_k), ymin=0.1, ymax=0.9, c='r')
        ax.set_xlim(-5.1, 5.5)
        cont += 1
plt.show()
