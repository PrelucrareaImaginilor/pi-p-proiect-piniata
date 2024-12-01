import numpy as np
import matplotlib.pyplot as plt
import PIL as pil

img = np.asarray(pil.Image.open("./test/football_64x64_grayscale.jpg"))

ft = np.log(1+abs(np.fft.fftshift( np.fft.fft2(img))))
plt.imshow(ft, cmap="gray")
plt.show()