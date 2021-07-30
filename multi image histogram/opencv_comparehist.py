import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test.JPG')
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,w,_ = image.shape

mask_image = []
hist_list = []
with open('test.txt','r') as rd:
    boxes = rd.readlines()
    for i, box in enumerate(boxes[10:15]):
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
        add_image = cv2.resize(image[ymin:ymax,xmin:xmax], (200,200))
        cv2.imshow(str(i),add_image)
        add_image = cv2.cvtColor(add_image, cv2.COLOR_BGR2HSV)
        hsv_hist = cv2.calcHist([add_image],[0,1],None,[360,256],[0,360,0,256])
        cv2.normalize(hsv_hist,hsv_hist,0,1, cv2.NORM_MINMAX)
        hist_list.append(hsv_hist)
        

# cv2.compareHist
for i,hist1  in enumerate(hist_list):
    for j, hist2 in enumerate(hist_list):
        
        ret1 = cv2.compareHist(hist1,hist2, cv2.HISTCMP_CORREL)
        ret2 = cv2.compareHist(hist1,hist2, cv2.HISTCMP_CHISQR)
        ret3 = cv2.compareHist(hist1,hist2, cv2.HISTCMP_INTERSECT)
        ret4 = cv2.compareHist(hist1,hist2, cv2.HISTCMP_BHATTACHARYYA)
        ret5 = cv2.compareHist(hist1,hist2, cv2.HISTCMP_HELLINGER)
        ret6 = cv2.compareHist(hist1,hist2, cv2.HISTCMP_KL_DIV)
        print("\t\t\t\t\t\t\t{} 번과 {} 번의 비교".format(i,j))
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print(" 상관관계 : {:.4f} \t 카이제곱 : {:.4f} \t 인터섹션 : {:.4f} \t 바타챠랴 : {:.4f} \t 헬링거 : {:.4f} \t 콜백발산 : {:.4f} ".format(
            ret1,ret2,ret3,ret4,ret5,ret6
        ))
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
cv2.waitKey(0)