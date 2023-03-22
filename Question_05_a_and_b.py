import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

#define your variable
x = sym.symbols('x')
#Define equation
eq = 1/(sym.exp(x*(-1)))
#define the derivative of the equation
eq1 = sym.diff(eq)
#convert both to numpy functions. note the syntax.
f = sym.lambdify(x, eq, 'numpy')
f1 = sym.lambdify(x, eq1,'numpy')
#create an array
x1 = np.arange(0,10,0.01)
#Apply the function to both arrays
y1 = f(x1)
y2 = f1(x1)
#plot your results
plt.plot(x1,y1)
plt.legend(["eq"]) #it is to combine 2 graphs
plt.show()
plt.plot(x1,y2)
plt.legend(["derivative"])
plt.show()

