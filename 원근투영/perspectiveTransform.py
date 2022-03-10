import cv2 
import numpy as np 

from mouse_events import MouseEvents

POINTS_CHECK = False
# 좌표점은 좌상->좌하-> 우상 -> 우하 
# 변경할 좌표를 4x2 행렬로 전환 
# 이동할 좌표를 설정
mouse_events = MouseEvents()
mouse_events2 = MouseEvents()

path = 'images.jpg'
frame = cv2.imread(path)
height, width  = frame.shape[:2]
cv2.imshow('origin', frame)
if POINTS_CHECK != True:
    cv2.setMouseCallback('origin',mouse_events.onMouse, frame)
    cv2.waitKey(0)
    source_coord = np.float32( mouse_events.points )
    H = max(mouse_events.points[2][0],mouse_events.points[3][0]) - min(mouse_events.points[0][0],mouse_events.points[1][0])
    W = max(mouse_events.points[0][1], mouse_events.points[1][1], mouse_events.points[2][1], mouse_events.points[3][1] ) - min(mouse_events.points[0][1], mouse_events.points[1][1], mouse_events.points[2][1], mouse_events.points[3][1] )
    destination_coord = np.float32( [ [0,0], [0,H], [W,0], [W,H] ] )
    M = cv2.getPerspectiveTransform(source_coord, destination_coord)
    M2 = cv2.getPerspectiveTransform(destination_coord, source_coord)

    INV_M = np.linalg.pinv(M)
    
    
transformed = cv2.warpPerspective(frame, M, (W,H))
cv2.imshow('transformed', transformed)


if POINTS_CHECK != True:
    cv2.setMouseCallback('transformed',mouse_events2.onMouse, transformed)
    cv2.waitKey(0)
    line_coord = np.float32(mouse_events2.points)
    One = np.squeeze(INV_M @ np.expand_dims(np.append(line_coord[0], 1), axis=1))
    Two = np.squeeze(INV_M @ np.expand_dims(np.append(line_coord[1], 1), axis=1))
    One = One[:2] / One[2]
    Two = Two[:2] / Two[2]

    POINTS_CHECK = True

cv2.line(transformed, line_coord[0].astype(int), line_coord[1].astype(int), (255,0,0),2,1)
cv2.line(frame, One.astype(int), Two.astype(int), (255,0,0),2,1)

dst2 = cv2.warpPerspective(transformed, M2, (height, width))
cv2.imshow('transform2', dst2)

cv2.imshow('origin', frame)
cv2.imshow('transformed', transformed)
cv2.waitKey(0)