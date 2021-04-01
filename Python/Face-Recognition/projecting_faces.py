import sys
import dlib
import cv2
import openface

predictor_model = "../models/shape_predictor_68_face_landmarks.dat"

file_name = sys.argv[1]

face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

file_name = sys.argv[1]

image = cv2.imread(file_name)
detected_faces = face_detector(image, 1)

print("Found {} faces in the image file {}".format(len(detected_faces), file_name))

for i, face_rect in enumerate(detected_faces):
    print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
    pose_landmarks = face_pose_predictor(image, face_rect)
    alignedFace = face_aligner.align(534, image, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    cv2.imwrite("aligned_face_{}.jpg".format(i), alignedFace)