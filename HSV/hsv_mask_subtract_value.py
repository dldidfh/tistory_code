import cv2
import numpy as np
from matplotlib import pyplot as plt

origin_image = cv2.imread('puppy.jpg')
hsv_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)

val = 255

mask = hsv_image[:50,:100,:]

array = np.full(mask.shape, (0,0,val), dtype=np.uint8)

sub_mask_image = cv2.subtract(mask, array)

hsv_image[:50,:100,:] = sub_mask_image

val_sub_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

print("원본 bgr \t:",origin_image[0,0,:])
print("변환 bgr \t:",val_sub_image[0,0,:])

image = np.concatenate((origin_image,val_sub_image), axis=1)

cv2.imshow('add, subtract', image)
cv2.waitKey(0)


