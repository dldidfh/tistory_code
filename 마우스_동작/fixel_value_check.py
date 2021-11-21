import cv2 
import numpy as np 

class MouseGesture():
    def __init__(self) -> None:
        self.is_dragging = False 
        # 마우스 위치 값 임시 저장을 위한 변수 
        self.x0, self.y0, self.w0, self.h0 = -1,-1,-1,-1

    def on_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x0 = x
            self.y0 = y
            self.is_dragging = True
            print("사각형의 시작 좌표는 x : {} y : {}".format(x,y) )
        elif event == cv2.EVENT_LBUTTONUP:
            self.is_dragging = False
            cv2.rectangle(param['image'], (self.x0, self.y0), (x,y),(0,0,255),2)            
            cv2.imshow(param['window_name'], param['image'])
            print("사각형의 좌표는 ({}, {}), ({}, {})".format(self.x0,self.y0,x,y) )
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.is_dragging:
                temp_img = param['image'].copy()
                cv2.rectangle(temp_img, (self.x0, self.y0), (x,y),(0,0,255),2)            
                cv2.imshow(param['window_name'], temp_img)
        return 


image = cv2.imread('test.JPG')
window_name = 'mouse_callback'
mouse_class = MouseGesture()
param = {
    "image" : image,
    "window_name" : window_name
}
cv2.imshow(window_name, image)
cv2.setMouseCallback(window_name, mouse_class.on_mouse, param=param)
cv2.waitKey(0)

