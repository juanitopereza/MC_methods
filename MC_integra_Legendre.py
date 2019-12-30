import numpy as np

def fun(x):
    return (np.abs((5*x**3-3*x)/2))**2

def Integra(fun, a, b, NPoints, intentos):
    x = np.random.uniform(a,b,NPoints)
    res = []
    for i in xrange(intentos):
        res.append((b-a)/NPoints*sum(fun(x)))
    return np.mean(res)
def error(calculado,analitico):
    return (np.abs((calculado-analitico)/analitico))

#%%

print("El valor de la integral es: {}".format(Integra(fun,-1,1,10000,200)))
