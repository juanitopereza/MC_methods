import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('parametros.dat')

#make a simple figure
fig1 = plt.figure()
ax1 = plt.axes()

ax1.set_xlabel("a")
ax1.set_ylabel("f(a)")
ax1.set_title("parametro a")

count, bins, ignored =plt.hist(data[:,0], 100, normed=True)

filename = 'grafica_a' 
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()

fig2 = plt.figure()
ax2 = plt.axes()

ax2.set_xlabel("b")
ax2.set_ylabel("f(b)")
ax2.set_title("parametro b")

count, bins, ignored =plt.hist(data[:,1], 20, normed=True)

filename = 'grafica_b' 
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()

fig3 = plt.figure()
ax3 = plt.axes()

ax3.set_xlabel("c")
ax3.set_ylabel("f(c)")
ax3.set_title("parametro c")

count, bins, ignored =plt.hist(data[:,2], 20, normed=True)

filename = 'grafica_c' 
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()

fig4 = plt.figure()
ax4 = plt.axes()

ax4.set_xlabel("d")
ax4.set_ylabel("f(d)")
ax4.set_title("parametro d")

count, bins, ignored =plt.hist(data[:,3], 20, normed=True)

filename = 'grafica_d' 
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()
