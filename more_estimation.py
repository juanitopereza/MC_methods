import numpy as np
import matplotlib.pyplot as plt

#%%

def prob_density(x_k, sigma):
    return 1/(sigma * np.sqrt(2.0 * np.pi)) *np.exp(-1/2*(x_k**2/sigma**2))

def likelihood(x, sigmas, A):
    if(isinstance(sigmas,float)):
        likes = 1.0
        if (sigmas <=1) or (sigmas >=10):
            likes = 0
        else:
            for cosa in x:
                likes *= A * prob_density(cosa,sigmas)
    else:
        likes = np.ones(len(sigmas))
        for i in range(len(sigmas)):
            if (sigmas[i] <=1) or (sigmas[i] >=10):
                likes[i] = 0
            else:
                for cosa in x:
                    likes[i] *= A * prob_density(cosa,sigmas[i])
    return likes

def dl_ds(x, sigma, A):
    h = 0.1
    derivada = (likelihood(x, sigma+h, A) - likelihood(x, sigma-h, A))/(2.0*h)
    return derivada
def d2l_ds2(x, sigma, A):
    h = 0.1
    derivada = (dl_ds(x, sigma+h, A) - dl_ds(x, sigma-h, A))/(2.0*h)
    return derivada
def NR(x, guess, A):
    cero = guess
    while np.abs(dl_ds(x, cero, A)) > 1E-20:
        cero -= dl_ds(x, cero, A)/d2l_ds2(x, cero, A)
    return cero



data = np.loadtxt('valores.txt')

sigmas = np.linspace(1,10,1000)
likeli = likelihood(data, sigmas, 1.0)
#%%
plt.plot(sigmas,likeli)
plt.xlabel(r"$\sigma$")
plt.ylabel(r"$L\ * {\rm{prob} (\sigma)}$")
plt.savefig("like.png")
plt.close()
#%%

dLds = dl_ds(data, sigmas, 1.0)

#%%
plt.plot(sigmas, dLds)
plt.xlabel(r"$\sigma$")
plt.ylabel(r"$dL/d\sigma$")
plt.savefig("like_prime.png")
plt.close()

#%%


sigma_cero = NR(data, 4.0, 1.0)
print('sigma_cero : {}'.format(sigma_cero))

#%%

d2L = d2l_ds2(data,sigmas,1.0)

#%%

plt.plot(sigmas, d2L)
plt.xlabel(r"$\sigma$")
plt.ylabel(r"$d^2L/d\sigma^2$")
plt.savefig("like_prime_prime.png")
plt.close()

print("delta_sigma_cero= {}".format(-d2l_ds2(data,sigma_cero,1.0)))
