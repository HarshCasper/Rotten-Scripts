import face_recognition_api
import cv2
import os
import pickle
import numpy as np
import warnings

# Basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load Face Recogniser classifier
fname = 'classifier.pkl'
if os.path.isfile(fname):
    with open(fname, 'rb') as f:
        (le, clf) = pickle.load(f)
else:
    print('\x1b[0;37;43m' + "Classifier '{}' does not exist".format(fname) + '\x1b[0m')
    quit()

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition_api.face_locations(small_frame)
            face_encodings = face_recognition_api.face_encodings(small_frame, face_locations)

            face_names = []
            predictions = []
            if len(face_encodings) > 0:
                closest_distances = clf.kneighbors(face_encodings, n_neighbors=1)

                is_recognized = [closest_distances[0][i][0] <= 0.5 for i in range(len(face_locations))]

                # predict classes and cull classifications that are not with high confidence
                predictions = [(le.inverse_transform(int(pred)).title(), loc) if rec else ("Unknown", loc) for pred, loc, rec in
                               zip(clf.predict(face_encodings), face_locations, is_recognized)]

            # # Predict the unknown faces in the video frame
            # for face_encoding in face_encodings:
            #     face_encoding = face_encoding.reshape(1, -1)
            #
            #     # predictions = clf.predict(face_encoding).ravel()
            #     # person = le.inverse_transform(int(predictions[0]))
            #
            #     predictions = clf.predict_proba(face_encoding).ravel()
            #     maxI = np.argmax(predictions)
            #     person = le.inverse_transform(maxI)
            #     confidence = predictions[maxI]
            #     print(person, confidence)
            #     if confidence < 0.7:
            #         person = 'Unknown'
            #
            #     face_names.append(person.title())

        process_this_frame = not process_this_frame


        # Display the results
        for name, (top, right, bottom, left) in predictions:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
