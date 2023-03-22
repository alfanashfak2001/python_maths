import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

#define your variable
x = sym.symbols('x')
#Define equation
eq1 = sym.sin(sym.sin(2*x)) #sin sin 2x
eq2=-1*(x**3)-2*(x**2)+(3*x)+10 #-x^3-2x^2+3x+10
eq3=sym.exp(-0.8*x)
eq4=(x**2)*(sym.cos(sym.cos(2*x)))-2*(sym.sin(sym.sin(x-(sym.pi)/3)))
eq5=2*sym.cos(x+pi/6)
eq6=x*sym.exp(-0.4*(x**2))
#convert to numpy functions. note the syntax.
f1 = sym.lambdify(x, eq1, 'numpy')
f2 = sym.lambdify(x, eq2, 'numpy')
f3 = sym.lambdify(x, eq3, 'numpy')
f4 = sym.lambdify(x, eq4, 'numpy')
f5 = sym.lambdify(x, eq5, 'numpy')
f6 = sym.lambdify(x, eq6, 'numpy')
#create an array
x1 = np.arange(-10,10,0.01)
x2 = np.arange(-pi,0,0.01)
x3 = np.arange(0,pi,0.01)
#Apply the function to array
y1 = f1(x1)
y2 = f2(x1)
y3 = f3(x1)
y4 = f4(x1)
#for periodic function
y5 = f5(x2)
y6 = f6(x3)


#plot your results
plt.plot(x1,y1)
plt.legend(["sin(sin(2x))"])
plt.show()
plt.plot(x1,y2)
plt.legend(["-x^3-2x^2+3x+10"])
plt.show()
plt.plot(x1,y3)
plt.legend(["e^-0.8x"])
plt.show()
plt.plot(x1,y4)
plt.legend(["x^2*cos(cos(2x))-2sin(sin(x-pi/3))"])
plt.show()
#periodic function
plt.plot(x2,y5)
plt.plot(x3,y6)
plt.legend(["2cos(x+pi/6)","x e^-0.4x^2"])
plt.show()
