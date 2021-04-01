import scipy.misc
import dlib
import numpy as np

face_detector = dlib.get_frontal_face_detector()

predictor_model = './models/shape_predictor_68_face_landmarks.dat'
pose_predictor = dlib.shape_predictor(predictor_model)

face_recognition_model = './models/dlib_face_recognition_resnet_model_v1.dat'
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)


def _rect_to_tuple(rect):
    return rect.top(), rect.right(), rect.bottom(), rect.left()


def _tuple_to_rect(rect):
    return dlib.rectangle(rect[3], rect[0], rect[1], rect[2])


def _trim_rect_tuple_to_bounds(rect, image_shape):
    return max(rect[0], 0), min(rect[1], image_shape[1]), min(rect[2], image_shape[0]), max(rect[3], 0)


def face_distance(face_encodings, face_to_compare):
    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)


def load_image_file(filename, mode='RGB'):
    img = scipy.misc.imread(filename)

    # If very large size image, Resize the image
    if img.shape[0] > 800:
        baseheight = 500
        w = (baseheight / img.shape[0])
        p = int(img.shape[1] * w)
        img = scipy.misc.imresize(img, (baseheight, p))
    elif img.shape[1] > 800:
        baseheight = 500
        w = (baseheight / img.shape[1])
        p = int(img.shape[0] * w)
        img = scipy.misc.imresize(img, (p, baseheight))

    return img


def _raw_face_locations(img, number_of_times_to_upsample=1):
    return face_detector(img, number_of_times_to_upsample)


def face_locations(img, number_of_times_to_upsample=1):
    return [_trim_rect_tuple_to_bounds(_rect_to_tuple(face), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample)]


def _raw_face_landmarks(face_image, face_locations=None):
    if face_locations is None:
        face_locations = _raw_face_locations(face_image)
    else:
        face_locations = [_tuple_to_rect(face_location) for face_location in face_locations]

    return [pose_predictor(face_image, face_location) for face_location in face_locations]


def face_landmarks(face_image, face_locations=None):n: A list of dicts of face feature locations (eyes, nose, etc)

    Given an image, return the 128-dimension face encoding for each face in the image.

    :param face_image: The image that contains one or more faces
    :param known_face_locations: Optional - the bounding boxes of each face if you already know them.
    :param num_jitters: How many times to re-sample the face when calculating encoding. Higher is more accurate, but slower (i.e. 100 is 100x slower)
    :return: A list of 128-dimentional face encodings (one for each face in the image)
are_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
 
    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)
