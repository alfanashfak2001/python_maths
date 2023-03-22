import numpy as np
import scipy.fftpack as sfft
import matplotlib.pyplot as plt
from numpy import pi
x = np.arange(-np.pi,np.pi, 0.01)
x1 = np.arange(-np.pi,np.pi, 0.1)


y= np.sin(2*pi*x)+ 0.25*np.sin(50*x)
y1=np.sin(2*pi*x1)+ 0.25*np.sin(50*x1)

#dft
yf = sfft.fft(y)
yf1 = sfft.fft(y1)

#idft
yf_ = sfft.ifft(yf)
yf1_ = sfft.ifft(yf1)

plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x,np.real(yf_))
plt.plot(x1,np.real(yf1_))
plt.legend(["100Hz","10Hz","ifft 100Hz","ifft 10Hz"])

plt.show()