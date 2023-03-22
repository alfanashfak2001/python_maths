import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sfft
from matplotlib import image as mpimg


img = mpimg.imread("Fruit.jpg")
plt.imshow(img)
plt.show()

#fft
imgf = sfft.fft2(img)
plt.imshow(np.abs(imgf))
plt.show()
#image with fft shift
imgf = sfft.fftshift(imgf)
plt.imshow(np.abs(imgf))
plt.show()

#inverse fft
img1 = sfft.ifft2(imgf)
plt.imshow(np.abs(img1))
plt.show()

#remove high frequencies
imgf1 = np.zeros((360,360),dtype=complex)
c = 180
r = 50
for m in range(0,360):
    for n in range(0,360):
        if (np.sqrt(((m-c)**2 + (n-c)**2))<r):
            imgf1[m,n] = imgf[m,n]

plt.imshow(np.abs(imgf1))
plt.show()
img1 = sfft.ifft2(imgf1)
plt.imshow(np.abs(img1))
plt.show()

#remove low frequencies
imgf1 = np.zeros((360,360),dtype=complex)
c = 180
r = 90
for m in range(0,360):
    for n in range(0,360):
        if (np.sqrt(((m-c)**2 + (n-c)**2))>r):
            imgf1[m,n] = imgf[m,n]

plt.imshow(np.abs(imgf1))
plt.show()
img1 = sfft.ifft2(imgf1)
plt.imshow(np.abs(img1))
plt.show()

