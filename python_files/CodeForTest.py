import face_recognition
from PIL import Image as img, ImageDraw
import numpy as numpy
import cv2

capture = cv2.VideoCapture(0)

while True:
    # Show camera window
    ret, frame = capture.read()
    cv2.imshow("Take profile picture", frame)

    # Save on pressing "Spacebar" then exit
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        cv2.imwrite("./images/RegisterPhoto.png", frame)
        cv2.destroyAllWindows()
        break

# When everything done, release the capture
capture.release()

Reg_Photo = face_recognition.load_image_file('./images/RegisterPhoto.png')
Reg_Photo_encoding = face_recognition.face_encodings(Reg_Photo)[0]

Known_face_encoding = [
    Reg_Photo_encoding

]

known_face_names = [
  
]

capture = cv2.VideoCapture(0)

while True:
    # Show camera window
    ret, frame = capture.read()
    cv2.imshow("Take profile picture", frame)

    # Save on pressing "Spacebar" then exit
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        cv2.imwrite("./images/LoginPhoto.png", frame)
        cv2.destroyAllWindows()
        break

Login_Photo = face_recognition.load_image_file('./images/LoginPhoto.png')

face_locations = face_recognition.face_locations(Login_Photo)
face_encoding = face_recognition.face_encodings(Login_Photo, face_locations)

pil_image = img.fromarray(Login_Photo)

draw = ImageDraw.Draw(pil_image)


for(top, right, bottom, left), face_encoding in zip(face_locations, face_encoding):
    matches = face_recognition.compare_faces(
        Known_face_encoding, face_encoding)

name = "Unknown Person"

if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height), (right, bottom+5)),
                   fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((left + 6, bottom - text_height),
              name, fill=(255, 255, 255, 255))
    del draw

    print("Thank you for registering" + name)

    pil_image.show()

    pil_image.save('identify.jpg')
   
