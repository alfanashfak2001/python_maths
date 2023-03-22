import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.fftpack as sfft
import scipy.signal as signal


img = mpimg.imread("Fruit.jpg")

#Gaussian filter
kernel = np.outer(signal.gaussian(360, 5), signal.gaussian(360, 5))
kf = sfft.fft2(sfft.ifftshift(kernel))  #freq domain kernel
plt.imshow(np.abs(kf))
plt.show()
imgf = sfft.fft2(img)
plt.imshow(np.abs(kf))
plt.show()
img_b = imgf*kf
plt.imshow(np.abs(img_b))
plt.show()
img1 = sfft.ifft2(img_b)
plt.imshow(np.abs(img1))
plt.show()