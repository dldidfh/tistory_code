import cv2
import numpy as np
from matplotlib import pyplot as plt

origin_image = cv2.imread('puppy.jpg')
hsv_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)
image = np.concatenate((origin_image,hsv_image), axis=1)

print('원본 : \t',origin_image[0,0,:])
print('hsv : \t',hsv_image[0,0,:])

cv2.imshow('HSV', image)
cv2.waitKey(0)