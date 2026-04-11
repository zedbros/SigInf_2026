import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

source_image = Image.open('mnist.png')
image = np.array(source_image)
print(image.shape)
plt.imshow(image)
plt.show()

new_image = image
np.reshape(new_image, (len(image)*2, len(image)*2, 4))
print(new_image.shape)
plt.imshow(new_image)
plt.show()
