import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

fig=plt.figure() 
ax = fig.add_subplot(111,projection='3d') 

ax.scatter([1,2,3],[2,3,4],[4,5,6],color="red",s=100)

plt.show()