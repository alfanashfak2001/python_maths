import math

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
def taylor(n):
    x = sym.symbols('x')

    taylorexp=0

    for i in range(0,n):
        eq1 = ((-1) ** (i + 1))
        eq2 = math.factorial((2 * i) + 1)
        eq3 = (x - (pi / 2)) ** (1 + 2 * i)
        eq4 = eq1 * eq3 / eq2
        taylorexp+=eq4
    # print(taylorexp)
    f = sym.lambdify(x, taylorexp, 'numpy')
    x1 = np.arange(np.pi*-2,np.pi*2,0.01)
    y = f(x1)

    #plot your results
    plt.plot(x1,y)



for j in range(1,61):
    taylor(j)

plt.show()