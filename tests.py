import unittest
from FaceRecognition import FaceRecognition


class FaceRecognitionTests(unittest.TestCase):
    def test_object_creation(self):
        self.assertIsNotNone(FaceRecognition())

    def test_image_location(self):
        image_location = 'tom.png'
        face_recognition_instance = FaceRecognition()
        face_recognition_instance.set_image_location(image_location)
        self.assertEqual(image_location, face_recognition_instance.get_image_location())

    def test_exception_raise(self):
        face_recognition_instance = FaceRecognition()
        with self.assertRaises(Exception) as assertRaises:
            face_recognition_instance.show_faces_in_image()
        self.assertEqual(str(assertRaises.exception), 'The current object does not contain an image location.')


if __name__ == '__main__':
    unittest.main()
