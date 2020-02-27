import face_recognition
from PIL import Image as img , ImageDraw 

image_of_Obama = face_recognition.load_image_file('RegisterPhoto.jpg')
Obama_face_encoding = face_recognition.face_encodings(image_of_Obama)[0]

Known_face_encoding = [
    Obama_face_encoding

]

known_face_names = [
"Name of user"
]

Test_image = face_recognition.load_image_file('LoginPhoto.jpg')

face_locations = face_recognition.face_locations(Test_image)
face_encoding = face_recognition.face_encodings(Test_image,face_locations)

pil_image = img.fromarray(Test_image)

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

    pil_image.save('identify.jpg')