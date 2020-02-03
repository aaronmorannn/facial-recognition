# Reference https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html

import numpy as numpy
import cv2 as cv

capture = cv.VideoCapture(0)



# Access camera and refresh
if not capture.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame by frame
    ret, frame = capture.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    # Code that deals with the frames goes here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Display resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv.destroyAllWindows()