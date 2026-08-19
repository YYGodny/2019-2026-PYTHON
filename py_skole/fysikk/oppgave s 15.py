import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"Global_temp_GISS.txt")

tid = data[:,0]
temperatur = data[:,1]

plt.figure(1)
plt.plot(tid, temperatur)
plt.title('endring i global temperatur')
plt.xlabel('tid i år')
plt.ylabel('temperaturendring i K')
plt.grid()
plt.show()
