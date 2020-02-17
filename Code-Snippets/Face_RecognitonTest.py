import numpy as np
import cv2
import face_recognition

# Using facial recognition Library
image = face_recognition.load_image_file("./TestImages/Test.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)
print(f'There are {len(face_locations)} people in this image')
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()