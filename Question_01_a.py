import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
import math
def plotperiodic():
    #define the variable variable
    x = sym.symbols('x')
    # equation
    eq0 = (x**2)+1
    eq1 = x*sym.exp(-x)
    eq2 = (x-2*np.pi)**2+1
    eq3 = (x-2*np.pi)*sym.exp(-x+2*np.pi)
    eq4 = (x-4*np.pi)**2+1
    eq01 = (x+2*np.pi)*sym.exp(-x-2*np.pi)
    eq02 = (x+2*np.pi)**2+1
    eq03 = (x+4*np.pi)*sym.exp(-x-4*np.pi)


    #convert both to numpy functions.
    f0 = sym.lambdify(x, eq0, 'numpy')
    f1 = sym.lambdify(x, eq1,'numpy')
    f2 = sym.lambdify(x, eq2, 'numpy')
    f3 = sym.lambdify(x, eq3,'numpy')
    f03 = sym.lambdify(x, eq03,'numpy')
    f4 = sym.lambdify(x, eq4,'numpy')
    f01 = sym.lambdify(x, eq01, 'numpy')
    f02 = sym.lambdify(x, eq02,'numpy')

    #create an array for x values
    x03 = np.arange(np.pi*-4,np.pi*-3,0.1) #-4pi to -3pi
    x02 = np.arange(np.pi*-3,np.pi*-2,0.1)#-3pi to -2pi
    x01 = np.arange(np.pi*-2,np.pi*-1,0.1)#-2 pi to -pi
    x0 = np.arange(np.pi*-1,0,0.1)#-pi to 0
    x1 = np.arange(0,np.pi*1,0.1)#0 to pi

    x2 = np.arange(np.pi,np.pi*2,0.1)#pi to 2pi
    x3 = np.arange(np.pi*2,np.pi*3,0.1)#2pi to 3pi
    x4 = np.arange(np.pi*3,np.pi*4,0.1)#3pi to 4 pi

    #Apply the function to both arrays
    y0 = f0(x0)
    y1 = f1(x1)
    y2 = f2(x2)
    y3 = f3(x3)
    y4 = f4(x4)
    y01 = f01(x01)
    y02 = f02(x02)
    y03 = f03(x03)
    arrofactualvalues = np.concatenate((y03,y02,y01,y0,y1,y2,y3,y4))
    # convert array to list
    listofactualvalues=list(arrofactualvalues)


    #plot results results

    plt.plot(x03,y03)#(x+4*np.pi)*sym.exp(-x-4*np.pi)
    plt.plot(x02,y02)#(x+2*np.pi)**2+1
    plt.plot(x01,y01)#(x+2*np.pi)*sym.exp(-x-2*np.pi)
    plt.plot(x0,y0)#(x**2)+1
    plt.plot(x1,y1)#x*sym.exp(-x)
    plt.plot(x2,y2)#(x-2*np.pi)**2+1
    plt.plot(x3,y3)#(x-2*np.pi)*sym.exp(-x+2*np.pi)
    plt.plot(x4,y4)#(x-4*np.pi)**2+1

    plt.legend(["[-4π,-3π]", "[-3π,-2π]","[-2π,-π]", "[-π,0]","[0,π]", "[0,2π]","[2π,3π]", "[3π,4π]"])
    plt.show()
    # return listofactualvalues
plotperiodic()