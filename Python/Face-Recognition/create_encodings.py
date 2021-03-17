import os
import face_recognition_api
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np
import pandas as pd


def _get_training_dirs(training_dir_path):
    return [x[0] for x in os.walk(training_dir_path)][1:]


def _get_training_labels(training_dir_path):
    return [x[1] for x in os.walk(training_dir_path)][0]


def _get_each_labels_files(training_dir_path):
    return [x[2] for x in os.walk(training_dir_path)][1:]


def _filter_image_files(training_dir_path):
    exts = [".jpg", ".jpeg", ".png"]

    training_folder_files_list = []
    for list_files in _get_each_labels_files(training_dir_path):
        l = []
        for file in list_files:
            imageName, ext = os.path.splitext(file)
            if ext.lower() in exts:
                l.append(file)
        training_folder_files_list.append(l)

    return training_folder_files_list


def _zipped_folders_labels_images(training_dir_path, labels):
    return list(zip(_get_training_dirs(training_dir_path),
                    labels,
                    _filter_image_files(training_dir_path)))


def create_dataset(training_dir_path, labels):
    X = []
    for i in _zipped_folders_labels_images(training_dir_path, labels):
        for fileName in i[2]:
            file_path = os.path.join(i[0], fileName)
            img = face_recognition_api.load_image_file(file_path)
            imgEncoding = face_recognition_api.face_encodings(img)

            if len(imgEncoding) > 1:
                print('\x1b[0;37;43m' + 'More than one face found in {}. Only considering the first face.'.format(file_path) + '\x1b[0m')
            if len(imgEncoding) == 0:
                print('\x1b[0;37;41m' + 'No face found in {}. Ignoring file.'.format(file_path) + '\x1b[0m')
            else:
                print('Encoded {} successfully.'.format(file_path))
                X.append(np.append(imgEncoding[0], i[1]))
    return X

encoding_file_path = './encoded-images-data.csv'
training_dir_path = './training-images'
labels_fName = "labels.pkl"

# Get the folder names in training-dir as labels
# Encode them in numerical form for machine learning
labels = _get_training_labels(training_dir_path)
le = LabelEncoder().fit(labels)
labelsNum = le.transform(labels)
nClasses = len(le.classes_)
dataset = create_dataset(training_dir_path, labelsNum)
df = pd.DataFrame(dataset)

# if file with same name already exists, backup the old file
if os.path.isfile(encoding_file_path):
    print("{} already exists. Backing up.".format(encoding_file_path))
    os.rename(encoding_file_path, "{}.bak".format(encoding_file_path))

df.to_csv(encoding_file_path)

print("{} classes created.".format(nClasses))
print('\x1b[6;30;42m' + "Saving labels pickle to'{}'".format(labels_fName) + '\x1b[0m')
with open(labels_fName, 'wb') as f:
    pickle.dump(le, f)
print('\x1b[6;30;42m' + "Training Image's encodings saved in {}".format(encoding_file_path) + '\x1b[0m')
