from utils import *
import cv2

myDrone = initializeTello()

w,h = 360,240

while True:
    img = telloGetFrame(myDrone,w,h)
    cv2.imshow("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break