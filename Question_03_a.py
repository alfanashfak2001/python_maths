import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
#plot x*cos(x/2) in (-5pi to 7pi)
x = np.arange(-5*pi,7*pi,0.001) #from,to,particles defining x
y = x*np.cos(x/2)  #defining y
plt.plot(x,y)	#combining and plotting
plt.legend(["x*cos(x/2)"])
plt.show()		#for show the graph
