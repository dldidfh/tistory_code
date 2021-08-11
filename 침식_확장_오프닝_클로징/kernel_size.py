import numpy as np
import cv2

image_path = './test.JPG'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(300,300))
return_value, image = cv2.threshold(image, 127,255,cv2.THRESH_BINARY)

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))
kernel3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
kernel4 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

kernel_list = [kernel1,kernel2,kernel3,kernel4]

kernel1 = cv2.dilate(image,kernel1,iterations=1)
kernel2 = cv2.dilate(image,kernel2,iterations=1)
kernel3 = cv2.dilate(image,kernel3,iterations=1)
kernel4 = cv2.dilate(image,kernel4,iterations=1)

image = cv2.putText(image,'origin',(30,30),1,2,255,2)
kernel1 = cv2.putText(kernel1,'RECT 5x5',(30,30),1,2,255,2)
kernel2 = cv2.putText(kernel2,'RECT 11x11',(30,30),1,2,255,2)
kernel3 = cv2.putText(kernel3,'CROSS 5x5',(30,30),1,2,255,2)
kernel4 = cv2.putText(kernel4,'ELLIPSE 5x5',(30,30),1,2,255,2)

concat_image = np.concatenate((image,kernel1,kernel2,kernel3,kernel4),axis=1)

cv2.imshow('concat_image',concat_image)
cv2.moveWindow('concat_image',10,10)
cv2.waitKey(0)





