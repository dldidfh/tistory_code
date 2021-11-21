import cv2 
import numpy as np 

class MouseGesture():
    def __init__(self) -> None:
        self.is_dragging = False 
        # 마우스 위치 값 임시 저장을 위한 변수 
        self.x0, self.y0, self.w0, self.h0 = -1,-1,-1,-1

    def on_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("왼쪽 버튼 눌림 \t좌표 : x : {} y : {}".format(x,y) )
        elif event == cv2.EVENT_LBUTTONUP:
            print("왼쪽 버튼 올림\t좌표 : x : {} y : {}".format(x,y) )
        elif event == cv2.EVENT_RBUTTONDOWN:
            print("오른쪽 버튼 눌림\t좌표 : x : {} y : {}".format(x,y) )
        elif event == cv2.EVENT_RBUTTONUP:
            print("오른쪽 버튼 올림\t좌표 : x : {} y : {}".format(x,y) )    
        elif event == cv2.EVENT_MBUTTONDOWN:
            print("가운데 버튼 내림\t좌표 : x : {} y : {}".format(x,y) )
        elif event == cv2.EVENT_MBUTTONUP:
            print("가운데 버튼 올림\t좌표 : x : {} y : {}".format(x,y) )
        # elif event == cv2.EVENT_MOUSEMOVE:
        #     # 마우스 움직임은 너무 많이 나와서 생략    
        #     print("마우스 움직임\t좌표 : x : {} y : {}".format(x,y) )
        elif event == cv2.EVENT_MOUSEHWHEEL:
            # 가로휠이 없는 마우스라 .... 
            print("마우스 가로 휠 \t좌표 : x : {} y : {}".format(x,y) )
        elif event == cv2.EVENT_MOUSEWHEEL:
            print("마우스 그냥 휠 \t좌표 : x : {} y : {}".format(x,y) )
            
        return 

image = cv2.imread('test.JPG')
window_name = 'mouse_callback'
mouse_class = MouseGesture()

cv2.imshow(window_name, image)
cv2.setMouseCallback(window_name, mouse_class.on_mouse, param=image)
cv2.waitKey(0)

