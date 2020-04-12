import numpy as numpy
import cv2
import face_recognition
from PIL import Image as img , ImageDraw 


capture = cv2.VideoCapture(0)

while True:

    ret, frame = capture.read()
    cv2.imshow("Take profile picture", frame) 

    #Save on pressing "Spacebar" then exit
    if(cv2.waitKey(1) & 0xFF == ord('q')): #picture is taken by pressing q
        cv2.imwrite("images/photo.png", frame)
        cv2.destroyAllWindows()
        break

capture.release()
