import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

n = 201
zlim = 20
#xx, yy, zz = np.linspace(-1, 1, n), np.linspace(-1, 1, n), np.linspace(0, 15, n)
#print(xx, yy, zz)
x, y, z = np.meshgrid(np.linspace(-1, 1, n), np.linspace(-1, 1, n), np.linspace(0, zlim, n))

def E(z,t,w,e,phi):
    k = w*np.sqrt(e)
    return np.exp(1j*(k*z-(w*t)+phi))/np.sqrt(2)

#mask for z-axis
mx = x==0
my = y==0
mask = mx & my

epsend = 15/2

zmask = z >= epsend
#eps = np.array([4 for i in range(len(z[mask][:np.where(z[mask] == 5)[0][0]]))])
#eps = np.concatenate((eps, np.array([1 for i in range(len(z[mask][:np.where(z[mask] == 5)[0][0]]))])))

eps = 1/4*~zmask
eps += zmask
phaseshift = np.pi*(0.5-1)*zmask

u = np.real(E(z, 0, np.pi/epsend, 1, 0))*mask
v = np.real(E(z, 0, np.pi/epsend, eps, phaseshift))*mask
w = y * 0

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.quiver(x,y,z,u,v,w)#, length=0.1, normalize=True)
#ax.plot(u, v, zz)
ax.set_ylim(-1, 1)
ax.set_xlim(-1, 1)
ax.set_zlim(0, zlim)
#ax.axis('equal')
plt.show()
