import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    return np.exp(-((x - mu)/sig)**2 /2)/(sig*np.sqrt(2*np.pi))

c = 1
dx = 0.01
L = 10
x = np.linspace(0, L, num = (L/dx) + 1)
N = len(x)

dt = dx/(2*c)
s = (c*dt/dx)**2

#u = gaussian(x, 5, 1)
#u=np.sin(5*np.pi*x/L)
u=np.zeros(len(x))
#u[0] = 0
#u[-1] = u[-2]
#u[-1] = 0

deriv = np.zeros(len(x))
deriv[len(x)/2 - 50 : len(x)/2 + 50] = 1
u1 = np.zeros(len(x))
u1[1:-1] = np.copy((s/2)*(u[2:]+u[:-2])+(1-s)*u[1:-1]+dt*deriv[1:-1])
#u1[1:-1] = u[1:-1] + dt*deriv[1:-1]
#u1[-1]=u1[-2]

T = 10
m = int(round(T/dt))

for j in range(m):
    tmp = np.copy(u1)
    u1[1:-1] = s*(u1[2:] + u1[:-2]) + 2*(1-s)*u1[1:-1] - u[1:-1]
    #u1[-1] = u1[-2]
    u = np.copy(tmp)

    t = j*dt

    if(t == int(t) or t==0.2):
        plt.plot(x, u1, label='t='+str(t))
plt.ylabel('u')
plt.xlabel('x')
plt.legend()
plt.tight_layout()
plt.show()
                       
