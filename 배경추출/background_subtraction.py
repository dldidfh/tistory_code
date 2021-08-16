import cv2
import numpy as np
import time

video_path = './cctv.mp4'
output_path = './background_subtraction_output.mp4'

video = cv2.VideoCapture(video_path)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))
codec = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, codec, fps, (width, height)) 

fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=200,nmixtures=3,backgroundRatio=0.7, noiseSigma=0)
# fgbg = cv2.createBackgroundSubtractorMOG2(history=200,varThreshold=32,detectShadows=False)
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG(initializationFrames=20, decisionThreshold=0.5)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
while(1):
    start = time.time()
    
    return_value, frame = video.read()
    # 비디오 프레임 정보가 있으면 계속 진행 
    if return_value:
        pass
    else : 
        print('비디오가 끝났거나 오류가 있습니다')
        break

    background_extraction_mask = fgbg.apply(frame)
    # background_extraction_mask = cv2.morphologyEx(background_extraction_mask,
    #                                  cv2.MORPH_CLOSE, kernel)
    background_extraction_mask = cv2.dilate(background_extraction_mask,kernel,iterations=1)

    background_extraction_mask = np.stack((background_extraction_mask,)*3, axis=-1)

    concat_image = np.concatenate((frame,background_extraction_mask), axis=1)

    cv2.imshow('background extraction video', concat_image)
    cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()
    
