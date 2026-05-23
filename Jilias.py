import numpy as np
import matplotlib.pyplot as plt

x_min = -1.55
x_max = 1.55
y_min = -1.2
y_max = 1.2

x = np.linspace(x_min, x_max, 1000)
y = np.linspace(y_min, y_max, 1000)
X, Y = np.meshgrid(x, y)

Z = X + 1j * Y
g_r = (1+np.sqrt(5))/2
c = complex(g_r - 2, g_r - 1)
max_iter = 175


julia = np.zeros(Z.shape, dtype = int)

for i in range(max_iter):
    mask = np.abs(Z) < 2
    Z[mask] = Z[mask]**2 + c
    julia[mask] = i

plt.figure(figsize=(8, 4))
plt.imshow(julia, 
           extent = (x_min, x_max, y_min, y_max),
           cmap = 'plasma',
           origin = 'lower')

plt.show()



