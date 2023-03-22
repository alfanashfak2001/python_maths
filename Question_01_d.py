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

    plt.legend(["eq03", "eq02","eq01", "eq0","eq1", "eq2","eq3", "eq4"])
    return listofactualvalues



#n here is the length of the series you want if you need for n=1 enter 1
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


    # plot your results
    plt.plot(xfourier, yfourier)
    yfourier=list(yfourier)
    return yfourier


def calculatermse():
    #input m means which harmonic you need
    #enter from 1
    m=int(input("enter needed rmse of harmonic"))
    if m>=1:
        list1=plotperiodic()
        list2=f_Trans(m-1)
        MSE = np.square(np.subtract(list1,list2)).mean()

        RootMeanSqureError = math.sqrt(MSE)
        print("Root Mean Square Error for",m," th harmonic")
        print(RootMeanSqureError)
    else:
        print("enter values from 1")

calculatermse()


