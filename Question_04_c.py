import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.fftpack as sfft

img = mpimg.imread("Fruit.jpg")

#DCT
imgc = sfft.dct((sfft.dct(img,norm='ortho')).T,norm='ortho')
plt.imshow(imgc)
plt.show()

#IDCT
img1 = sfft.idct((sfft.idct(imgc,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()

#Removing high frequency components
imgc1 = np.zeros((360,360))
imgc1[:120,:120] = imgc[:120,:120]
img1 = sfft.idct((sfft.idct(imgc1,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()

#Scaling to 240px x 240px compressing
imgc2 = imgc[0:240,0:240]
img1 = sfft.idct((sfft.idct(imgc2,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()


