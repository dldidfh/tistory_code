import cv2
import numpy as np
import os

image = cv2.imread('milk.jpg', cv2.IMREAD_COLOR)
image2 = image.copy()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

return_value, threshold_image = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
method_list = [cv2.CHAIN_APPROX_NONE,cv2.CHAIN_APPROX_SIMPLE,cv2.CHAIN_APPROX_TC89_L1, cv2.CHAIN_APPROX_TC89_KCOS]
method_list_str = ['cv2.CHAIN_APPROX_NONE','cv2.CHAIN_APPROX_SIMPLE','cv2.CHAIN_APPROX_TC89_L1', 'cv2.CHAIN_APPROX_TC89_KCOS']

temp_image = []
for i in range(len(method_list)):
    contours, hierarchy = cv2.findContours(threshold_image, 
                            cv2.RETR_LIST, 
                            method_list[i])   
    if i <2:    
        print(method_list_str[i] + '\t\t',contours[-1].shape)
    else:
        print(method_list_str[i] + '\t',contours[-1].shape)

    # for contour in contours:
    contour_image = cv2.drawContours(image.copy(),contours[-1],-1,(0,0,255),2)
    if i ==0:
        temp_image = contour_image
    else :
        temp_image = np.concatenate((temp_image,contour_image), axis=1)
cv2.imshow('constour_method', temp_image)

# threshold_image = np.stack((threshold_image,)*3, axis=-1)
# image = np.concatenate((threshold_image, image), axis=1)
# image = np.concatenate((image2, image), axis=1)



cv2.imshow('contours', image)

cv2.waitKey(0)