import cv2
import numpy as np
from matplotlib import pyplot as plt

origin_image = cv2.imread('puppy.jpg')
hsv_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)

val = 100
array = np.full(hsv_image.shape, (0,0,val), dtype=np.uint8)

val_add_image = cv2.add(hsv_image, array)

print('BGR : \t',origin_image[55,116,:])
print('hsv : \t',hsv_image[55,116,:])
print('hsv 밝기(v) 증가 : \t',val_add_image[55,116,:])

val_add_image = cv2.cvtColor(val_add_image, cv2.COLOR_HSV2BGR)
image = np.concatenate((origin_image,val_add_image), axis=1)

cv2.imshow('add, subtract', image)
cv2.waitKey(0)