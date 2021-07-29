import cv2
import os 
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
print(image.dtype)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w = image.shape[:2]
image = cv2.resize(image, (512,512))
resize_w_rate = w/512
resize_h_rate = h/512
box_xmin = 0
box_ymin = 0
box_xmax = 0
box_ymax = 0
with open('./test.txt','r') as rd:
    boxes = rd.readlines()
    for box in boxes:
        box = box.split()
    
        box_xmin = int((float(box[1]) - float(box[3])/2) * w / resize_w_rate)
        box_ymin = int((float(box[2]) - float(box[4])/2) * h / resize_h_rate)
        box_xmax = int((float(box[1]) + float(box[3])/2) * w / resize_w_rate)
        box_ymax = int((float(box[2]) + float(box[4])/2) * h / resize_h_rate)
print(box_xmin,box_xmax,box_ymin,box_ymax)

testtestest = cv2.rectangle(image.copy(),(box_xmin,box_ymin),(box_xmax,box_ymax),(255,0,0),2)

mask = np.zeros(image.shape[:2], np.uint8)
mask[box_ymin:box_ymax, box_xmin:box_xmax ] = 255.0

mask_image = image[box_ymin:box_ymax, box_xmin:box_xmax]

blue_hist = cv2.calcHist([image],[0],mask,[256],[0,256])
green_hist = cv2.calcHist([image],[1],mask,[256],[0,256])
red_hist = cv2.calcHist([image],[2],mask,[256],[0,256])

plt.subplot(221),plt.imshow(image)
plt.subplot(222),plt.imshow(testtestest)
plt.subplot(223),plt.imshow(mask_image)
plt.subplot(224), plt.plot(blue_hist, color='b'),plt.plot(green_hist, color='g'),plt.plot(red_hist, color='r')
plt.xlim([-10,266])

plt.show()
