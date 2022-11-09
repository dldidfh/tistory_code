import time 
import os 
from glob import glob 
import numpy as np 
import cv2 
from multiprocessing import shared_memory 


data_size = np.zeros((400,400,3), dtype=np.uint8) # 데이터 사이즈를 미리 정하기 위해 변수 설정

shm = shared_memory.SharedMemory(create=True, size=data_size.nbytes, name="shm00001") # 데이터 사이즈만큼 공유메모리 할당

data = np.ndarray(data_size.shape, dtype=np.uint8, buffer=shm.buf) # 공유메모리에 넣을 데이터 설정 

print(shm.name)

imgs = glob(os.path.join('img/', "*.jpg"))
for img in  imgs :
    img = cv2.imread(img)
    img = cv2.resize(img, (400,400))
    data[:] = img[:] # 공유메모리의 데이터를 계속 변경함 
    time.sleep(2) # 2초마다 이미지 변경 
