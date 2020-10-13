from PIL import Image
from FaceRecognition import FaceRecognition

face_recognition_object = FaceRecognition()

face_recognition_object.set_image_location('target_shoppers.png')
face_recognition_object.show_faces_in_image()
