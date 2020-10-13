from PIL import Image
import face_recognition


class FaceRecognition:
    __image_location = ''

    def set_image_location(self, image_location: str) -> None:
        self.__image_location = image_location

    def get_image_location(self):
        return self.__image_location

    def show_faces_in_image(self) -> None:
        if not self.__image_location:
            raise Exception('The current object does not contain an image location.')
        else:
            image = face_recognition.load_image_file(self.__image_location)
            face_locations = face_recognition.face_locations(image)
            if len(face_locations) == 0:
                print('No faces were found in the provided image.')
            else:
                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    face_image = image[top:bottom, left:right]
                    pil_image = Image.fromarray(face_image)
                    pil_image.show()
