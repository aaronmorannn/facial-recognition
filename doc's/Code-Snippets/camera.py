# Reference https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
import numpy as numpy
import cv2

capture = cv2.VideoCapture(0)

cv2.namedWindow("Test")

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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Display resulting frame
    cv2.imshow('Camera', gray)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()
