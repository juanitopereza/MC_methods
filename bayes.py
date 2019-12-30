import numpy as np
import matplotlib.pyplot as plt

#%%
data = np.loadtxt("valores.txt")

def pdf(x,sigma):
    return (1.0/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*(x/sigma)**2)

def likelihood(valores, sigma):
    l = 1.0
    for x in valores:
        l *= pdf(x,sigma)
    return l
#%%

N= 10**5
list=[3.0]
for i in range(N):
    list_new = list[i] + np.random.normal()
    alpha = likelihood(data,list_new)/likelihood(data,list[i])
    if(alpha > 1):
        list.append(list_new)
    else:
        num = np.random.random()
        if(alpha > num):
            list.append(list_new)
        else:
            list.append(x[i])
x = np.array(list)
#%%


plt.hist(x, normed=True, bins=50)
plt.title("$\mu =\ {},\ \sigma =\ {}$".format(x.mean(), x.std()))
plt.savefig("grafica_sigma.png")
