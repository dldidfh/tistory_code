import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test.JPG')
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,w,_ = image.shape

mask_image = []
hist_add = np.array([0])
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
        add_image = cv2.cvtColor(cv2.resize(image[ymin:ymax,xmin:xmax], (100,100)), cv2.COLOR_BGR2HSV)
        hsv_hist = cv2.calcHist(add_image,[0,1],None,[360,256],[0,360,0,256])
        hist_add = hist_add + hsv_hist
        
    

x = np.arange(360)
y = np.arange(256)
xx, yy = np.meshgrid(x,y)
xxx, yyy = xx.ravel(), yy.ravel()
top = hist_add.flatten()
bottom = np.zeros_like(top)
width = depth = 1
z = np.zeros(360)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.bar3d(xxx,yyy,bottom,width,depth,top)
ax.set_xlabel('Hue')
ax.set_ylabel('saturation')
ax.set_zlabel('number')
plt.show()