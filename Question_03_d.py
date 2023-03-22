import math

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
import array as array
def taylor(n):

    taylorexp=0
    listOftaylorexp = array.array('d', [])

    for i in range(0,n):
        eq1 = ((-1) ** (i + 1))
        eq2 = math.factorial((2 * i) + 1)
        eq3 = ((pi/6) - (pi / 2)) ** (1 + 2 * i)
        eq4 = eq1 * eq3 / eq2
        taylorexp+=eq4
        value=(pi/3)*taylorexp
    print(value)
    return value


listOftaylorexp = array.array('d', [])
for j in range(1,61):
    print("for ",j-1,"th taylor expansion")

    listOftaylorexp.append(taylor(j))


xvalues = np.linspace(0,60,60)

plt.plot(xvalues,listOftaylorexp)

#real value of the function
realvalue=(pi/3)*sym.cos(pi/6)
xpoints = np.array([0, 60])
ypoints = np.array([realvalue,realvalue])
plt.plot(xpoints,ypoints)
plt.legend(["approximation","realvalue"])
plt.show()