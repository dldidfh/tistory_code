import cv2
import time
import numpy as np
from numpy.lib.function_base import diff

video_path = './cctv.mp4'
output_path = './background_extraction_output.mp4'
video = cv2.VideoCapture(video_path)

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 프레임 정보를 저장해놓을 변수를 선언한다
# first_frame = np.zeros((400,400,3))
# second_frame = np.zeros((400,400,3))
first_frame = np.zeros((400,400))
second_frame = np.zeros((400,400))
# 영상에서 첫 프레임과 두번째 프레임을 저장한다 
for i in range(2):
    return_value, frame = video.read()
    frame = cv2.resize(frame,(400,400))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i == 0 : first_frame = frame
    if i == 1 : second_frame = frame

diff_image = second_frame - first_frame
concat_image = np.concatenate((first_frame,second_frame,diff_image),axis=1)

cv2.imshow('images',concat_image)
cv2.waitKey(0)
    