import numpy as np
import cv2

image_path = './test.JPG'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(300,300))
return_value, image = cv2.threshold(image, 127,255,cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

erosion = cv2.erode(image,kernel,iterations=1)
dilate = cv2.dilate(image,kernel,iterations=1)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
blackhat = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT, kernel)
tophat = cv2.morphologyEx(image,cv2.MORPH_TOPHAT, kernel)
gradient = cv2.morphologyEx(image,cv2.MORPH_GRADIENT, kernel)


image = cv2.putText(image,'origin',(30,30),1,2,255,2)
erosion = cv2.putText(erosion,'Erosion',(30,30),1,2,255,2)
dilate = cv2.putText(dilate,'dilate',(30,30),1,2,255,2)
opening = cv2.putText(opening,'opening',(30,30),1,2,255,2)
closing = cv2.putText(closing,'closing',(30,30),1,2,255,2)
blackhat = cv2.putText(blackhat,'blackhat',(30,30),1,2,255,2)
tophat = cv2.putText(tophat,'tophat',(30,30),1,2,255,2)
gradient = cv2.putText(gradient,'gradient',(30,30),1,2,255,2)


concat_image1 = np.concatenate((erosion,dilate,blackhat,image),axis=1)
concat_image2 = np.concatenate((opening,closing,tophat,gradient),axis=1)
concat_image = np.concatenate((concat_image1,concat_image2),axis=0)

cv2.imshow('concat_image',concat_image)
cv2.moveWindow('concat_image',10,10)
cv2.waitKey(0)





