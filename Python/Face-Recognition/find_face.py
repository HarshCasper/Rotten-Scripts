import sys
import dlib
from skimage import io

file_name = sys.argv[1]

face_detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

image = io.imread(file_name)

detected_faces = face_detector(image, 1)

print("I found {} faces in the file {}".format(len(detected_faces), file_name))

win.set_image(image)

for i, face_rect in enumerate(detected_faces):
    print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))

    win.add_overlay(face_rect)

dlib.hit_enter_to_continue()