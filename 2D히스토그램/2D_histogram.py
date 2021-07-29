from typing import no_type_check
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('test.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hist = cv2.calcHist(hsv_image,[0,1], None, [360,256], [0,360,0,256])
stack_hist = np.stack((hist,)*3,axis=-1)
print('image의 shape \t\t: ',image.shape)
print('hist의 shape \t\t: ',hist.shape)
print('stack hist의 shape \t: ',stack_hist.shape)

fig = plt.figure(figsize=(8,3))
plt.tight_layout()
plt.subplot((131)),plt.imshow(image)
plt.subplot((132)),plt.imshow(hist)
plt.subplot((133)),plt.imshow(stack_hist)


plt.show()