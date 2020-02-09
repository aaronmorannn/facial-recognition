# Reference https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
import numpy as numpy
import cv2

capture = cv2.VideoCapture(0)

while True:
    #Show camera window
    ret, frame = capture.read()
    cv2.imshow("Take profile picture", frame) 
    
    #Save on pressing "Spacebar" then exit
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        cv2.imwrite("./TestImages/usr1.png", frame)
        cv2.destroyAllWindows()
        break

# When everything done, release the capture
capture.release()
