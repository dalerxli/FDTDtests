from matplotlib import pyplot as plt
import numpy as np
#from scipy.integrate import solve_ivp

def gaussian(x):
    return np.exp(-(x - 5)**2 / 2)

dx = 0.05
L = 10
x = np.linspace(0, L, num = (L/dx) + 1)
N = len(x)

E = gaussian(x)
E[0] = 0
E[-1] = 0

B = gaussian(x)
B[0] = 0
B[-1] = 0

T = 21
dt = dx/2

s = dt/(2*dx)

m = int(round(T/dt))

for j in range(m):
    B[1:-1] = B[1:-1] + s*(E[2:] - E[:-2])
    B[0]=B[1]
    B[-1] = B[-2]
    
    E[1:-1] = E[1:-1] + s*(B[2:] - B[:-2])
    
    t = (j+1)*dt
    
    if(t==int(t)):
        plt.subplot(1,2,1)
        plt.plot(x, E)
        plt.ylabel('E')
                
        plt.subplot(1,2,2)
        plt.plot(x, B)
        plt.ylabel('B')
        
    plt.tight_layout()
    #plt.savefig('___t{0:03d}.png'.format(j))
    #plt.clf()

'''
import commands
print commands.getoutput('convert -quality 100 ___t*.png giftest/yeetest.gif')
print commands.getoutput('rm ___t*.png') #remove temp files        
'''
plt.tight_layout()
#plt.savefig('testplots/yeetest.pdf')
plt.show()
