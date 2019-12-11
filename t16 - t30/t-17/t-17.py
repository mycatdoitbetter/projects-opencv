import cv2
import numpy as np
import matplotlib.pyplot as plt

# Abrir a imagem
img = cv2.imread('img.png', 0)






histograma_original = np.zeros([256], np.uint8)
histograma_equalizada = np.zeros([256], np.uint8)



img_flat = img.flatten()

for pixel in img_flat:
    histograma_original[pixel] += 1

# Calcula a função de distribuição cumulativa do histograma
cdf = [sum(histograma_original[:i + 1]) for i in range(len(histograma_original))]
cdf = np.array(cdf)


normal_cdf = ((cdf - cdf.min()) * 255) / (cdf.max() - cdf.min())
normal_cdf = normal_cdf.astype('uint8')


img_equalizada = normal_cdf[img_flat]
img_equalizada = np.reshape(img_equalizada, img.shape)


plt.plot(1)
plt.subplot(221)


plt.imshow(img, cmap='gray')
plt.subplot(222)

# Subplot do histograma da imagem em escala de cinza
plt.hist(img.ravel(), 256, [0, 256])
plt.subplot(223)

# Subplot da imagem equalizada
plt.imshow(img_equalizada, cmap='gray')
plt.subplot(224)

# Subplot do histograma da imagem equalizada
plt.hist(img_equalizada.ravel(), 256, [0, 256])
plt.show()