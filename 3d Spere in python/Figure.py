import numpy as np
import matplotlib.pyplot as plt

phi, thetha= np.mgrid[0:np.pi:30j,0:2*np.pi:30j]
x = np.sin(phi) * np.cos(thetha)
y = np.sin(phi) * np.sin(thetha)
z = np.cos(phi)

fig=plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_wireframe(x,y,z,color="cyan")
plt.show()