import cv2 

class MouseEvents:
    def __init__(self) -> None:
        self.points = []

    def left_button_down(self, x, y, frame):
        self.points.append([x,y])  
        cv2.circle(frame, (x,y),5,(0,0,255),-1)
        cv2.imshow('origin',frame)
        print(x,y)      


    def right_button_down(self,x,y, frame):
        self.points.pop()
        print(x,y)      

    def onMouse(self, event, x, y, flags, img):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.left_button_down(x,y, img)
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.right_button_down(x,y,img)