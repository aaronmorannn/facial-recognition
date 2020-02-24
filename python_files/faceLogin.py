import face_recognition
from PIL import Image as img , ImageDraw 

Reg_Photo = face_recognition.load_image_file('python_files\images\RegisterPhoto.png')
Reg_Photo_encoding = face_recognition.face_encodings(Reg_Photo)[0]

Known_face_encoding = [
    Reg_Photo_encoding

]

known_face_names = [
"Name of user"
]

Login_Photo = face_recognition.load_image_file('python_files\images\LoginPhoto.png')

face_locations = face_recognition.face_locations(Login_Photo)
face_encoding = face_recognition.face_encodings(Login_Photo,face_locations)

pil_image = img.fromarray(Login_Photo)

draw = ImageDraw.Draw(pil_image)


for(top,right,bottom , left) , face_encoding in zip(face_locations,face_encoding):
    matches = face_recognition.compare_faces(Known_face_encoding,face_encoding)

name = "Unknown Person"

if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]


    draw.rectangle(((left,top), (right, bottom)) , outline=(0,0,0))
    text_width , text_height = draw.textsize(name)
    draw.rectangle(((left,bottom - text_height) , (right , bottom+5)),fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6 , bottom - text_height), name, fill = (255,255,255,255))
    del draw

    print("Thank you for logging in " + name)

    pil_image.show()

    pil_image.save('python_files\images\identify.jpg')