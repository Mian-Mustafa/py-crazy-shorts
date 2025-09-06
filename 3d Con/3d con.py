import numpy as np
import matplotlib.pyplot as plt

r = np.linspace (0,1,50)
theta = np.linspace(0,2*np.pi,50)
R ,T = np.meshgrid(r,theta)

X = R * np.cos(T)
Y = R * np.sin(T)
Z = R # Height incease with radius

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z, color="orange",edgecolor="black")

plt.show()