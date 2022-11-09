import numpy as np 
import cv2 
from multiprocessing import shared_memory 

existing_shm = shared_memory.SharedMemory(name="shm00001") # writer에서 설정한 name 을 기준으로 공유메모리 접근

img = np.ndarray((400,400,3), dtype=np.uint8, buffer=existing_shm.buf) # 공유메모리에서 가져온 값을 저장할 변수 설정 - 사이즈 같아야함 

while True :
    cv2.imshow("shared memory image",img) # 이미지 시각화
    key = cv2.waitKey(33)
    if key == ord('q'):break