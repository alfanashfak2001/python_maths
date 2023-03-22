import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
import math

def f_Trans(n):
    #define symbol
    x = sym.Symbol("x")
    #define equation
    eq1 = 1 + x ** 2  # -pi to 0
    eq2 = x * sym.exp(-x)  # o to pi
    # find a0
    a0 = (1 / pi) * ((sym.integrate(eq1, (x, -pi, 0))) + (sym.integrate(eq2, (x, 0, pi))))
    print("a0 is",a0)
    #initialize fourier series to be plotted
    F_Series=a0/2

    for i in range(1,n+2): #(1,6) means 1 to 5

        #find an
        #multiplicate cos(nx) with eq1 and eq2 for find an
        eq1=(1+x**2)*(sym.cos(i*x))
        eq2=(x*sym.exp(-x))*(sym.cos(i*x))
        #integrate both eq1 and eq2
        an=(1/pi)*((sym.integrate(eq1, (x,-pi,0)))+(sym.integrate(eq2, (x,0,pi))))
        anintocos=an*sym.cos(i*x)
        #print(anintocos)
        #find bn
        eq1=(1+x**2)*(sym.sin(i*x))
        eq2=(x*sym.exp(-x))*(sym.sin(i*x))
        bn=(1/pi)*((sym.integrate(eq1, (x,-pi,0)))+(sym.integrate(eq2, (x,0,pi))))
        bnintosin=bn*sym.sin(i*x)
        #print(bnintosin)

        F_Series+=anintocos+bnintosin

    print("fourier series: ",F_Series)
    f = sym.lambdify(x, F_Series, 'numpy')
    # xfourier = np.arange(-4*pi, 4*pi, 0.1)
    xfourier = np.linspace(-4*pi, 4*pi,256)
    yfourier = f(xfourier)
    # print(yfourier)

    # plot your results
    plt.plot(xfourier, yfourier)
    yfourier=list(yfourier)

    # return yfourier

#o th harmonic it always a0/2
#graph is y=a0/2 it is a straight line
#plot the 1 st harmonic
f_Trans(0)
plt.legend(["1 st harmonic"])
plt.show()
#plot the fifth harmonic
f_Trans(4)
plt.legend(["5 th harmonic"])
plt.show()
#plot the a50 th harmonic
f_Trans(149)
plt.legend(["150 th harmonic"])
plt.show()

