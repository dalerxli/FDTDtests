import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fin = pd.read_csv('molcompar.out', sep=' ', header=None)
fin = np.array(fin)
plt.loglog(fin[0], fin[1], '.-', label='H error')
plt.loglog(fin[0], fin[2], '.-', label='E error')
plt.loglog(fin[0], fin[-1], '--')
plt.xlabel('h')
plt.ylabel('error')
plt.title('MOL2 results')
plt.legend()
plt.savefig('plots/mol2resultsfixed.pdf')


