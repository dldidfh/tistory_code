import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test.JPG')
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,w,_ = image.shape
box_list = []
mask_image = []
temp_image = []
seed = 8
with open('test.txt','r') as rd:
    boxes = rd.readlines()
    for box in boxes:
        box = box.strip()
        box = box.split()
        box = list(map(float,box))
        box_width = box[3] * w
        box_height = box[4] * h
        box_center_x = box[1] * w 
        box_center_y = box[2] * h

        xmin = int(box_center_x - box_width/2)
        ymin = int(box_center_y - box_height/2)
        xmax = int(box_center_x + box_width/2)
        ymax = int(box_center_y + box_height/2)
        mask = np.zeros((h,w), np.uint8)
        mask[ymin:ymax, xmin:xmax] = 255 
        mask_image.append( cv2.resize(image[ymin:ymax,xmin:xmax],(300,300)))

for i in range(seed,len(mask_image)):
    if i == seed:
        temp_image = mask_image[i]
    else:
        temp_image = np.concatenate((temp_image,mask_image[i]), axis=1)
cv2.imshow('bounding boxes',temp_image)
cv2.waitKey(0)