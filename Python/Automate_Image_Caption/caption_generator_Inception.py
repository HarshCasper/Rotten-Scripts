#!/usr/bin/env python
# coding: utf-8

# IMPORTS

import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import string
import os
from PIL import Image
import glob
from pickle import dump, load
from time import time
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import (
    LSTM,
    Embedding,
    TimeDistributed,
    Dense,
    RepeatVector,
    Activation,
    Flatten,
    Reshape,
    concatenate,
    Dropout,
    BatchNormalization,
)
from keras.optimizers import Adam, RMSprop
from keras.layers.wrappers import Bidirectional
from keras.layers.merge import add
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.models import Model
from keras import Input, layers
from keras import optimizers
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

# GPU Physical Growth
import tensorflow as tf
from tqdm.notebook import tqdm

physical_devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], True)


# load doc into memory
def load_doc(filename):
    """
    Function for loading various files
    :param filename: Source Path
    :return: Caption Text
    """
    # open the file as read only
    with open(filename) as file:
        # read all text
        text = file.read()
    return text


# Load Caption Dataset
filename = "Flickr8k_text/Flickr8k.token.txt"
doc = load_doc(filename)


def load_descriptions(doc):
    """
    Loads description (Captions)
    :param doc: Caption text files
    :return: Captions mapped to images
    """
    mapping = {}
    # process lines
    for line in doc.split("\n"):

        # split line by white space
        tokens = line.split()
        if len(line) < 2:
            continue

        # take the first token as the image id, the rest as the description
        image_id, image_desc = tokens[0], tokens[1:]

        # extract filename from image id
        image_id = image_id.split(".")[0]

        # convert description tokens back to string
        image_desc = " ".join(image_desc)

        # create the list if needed
        if image_id not in mapping:
            mapping[image_id] = []

        # store description
        mapping[image_id].append(image_desc)
    return mapping


# parse descriptions
descriptions = load_descriptions(doc)
print("Loaded: %d " % len(descriptions))


def clean_descriptions(descriptions):
    """
    Function to Remove Extra  whitespaces, punctuation marks etc
    :param descriptions: Text File containing the description of images
    """

    # prepare translation table for removing punctuation
    table = str.maketrans("", "", string.punctuation)
    for key, desc_list in descriptions.items():
        for i in range(len(desc_list)):
            desc = desc_list[i]

            # tokenize
            desc = desc.split()

            # convert to lower case
            desc = [word.lower() for word in desc]

            # remove punctuation from each token
            desc = [w.translate(table) for w in desc]

            # remove hanging 's' and 'a'
            desc = [word for word in desc if len(word) > 1]

            # remove tokens with numbers in them
            desc = [word for word in desc if word.isalpha()]

            # store as string
            desc_list[i] = " ".join(desc)


# Call clean Description
clean_descriptions(descriptions)


# convert the loaded descriptions into a vocabulary of words
def to_vocabulary(descriptions):
    """
    Convert Captions into meaningful words
    :param descriptions: Clean Description files
    :return: Set of words corresponding to caption
    """
    # build a list of all description strings
    all_desc = set()
    for key, value in descriptions.keys():
        [all_desc.update(d.split()) for d in descriptions[key]]
    return all_desc


vocabulary = to_vocabulary(descriptions)
print("Original Vocabulary Size: %d" % len(vocabulary))


def save_descriptions(descriptions, filename):
    """
    Save descriptions in a file
    :param descriptions: Clean descriptions
    :param filename: Path of File
    """
    lines = []
    for key, desc_list in descriptions.items():
        for desc in desc_list:
            lines.append(key + " " + desc)
    data = "\n".join(lines)
    with open(filename) as file:
        file.write(data)


save_descriptions(descriptions, "Model/Inception/descriptions.txt")


def load_set(filename):
    """
    Loading Dataset files
    :param filename: path to file to be loaded
    """
    doc = load_doc(filename)
    dataset = []
    # process line by line
    for line in doc.split("\n"):
        # skip empty lines
        if len(line) < 1:
            continue
        # get the image identifier
        identifier = line.split(".")[0]
        dataset.append(identifier)
    return set(dataset)


# Load text file containing the list of images in training dataset
# We would be loading 6k files here
filename = "Flickr8k_text/Flickr_8k.trainImages.txt"
train = load_set(filename)

# NUmber of files
print("Dataset: %d" % len(train))

# Load images
images = "Flickr8k_Dataset/img/"
img = glob.glob(images + "*.jpg")

# Load the names of images to be used in train data
train_images_file = "Flickr8k_text/Flickr_8k.trainImages.txt"
# Read the train image names in a set
train_images = set(open(train_images_file, "r").read().strip().split("\n"))

# Create a list of all the training images with their full path names
train_img = []

# Appending the names of images in the file to be trained
for i in img:
    if i[len(images) :] in train_images:
        train_img.append(i)

# Load the names of images to be used in test data
test_images_file = "Flickr8k_text/Flickr_8k.testImages.txt"
# Read the test image names in a set
test_images = set(open(test_images_file, "r").read().strip().split("\n"))

# Create a list of all the test images with their full path names
test_img = []

# Appending the names of images in the file to be trained
for i in img:
    if i[len(images) :] in test_images:
        test_img.append(i)


def load_clean_descriptions(filename, dataset):
    """
    Loading clean descriptions
    :param filename: The path to description file
    :param dataset: Train or Test?
    :return: Loads description in the memory
    """
    # load document
    doc = load_doc(filename)
    descriptions = {}
    for line in doc.split("\n"):
        # split line by white space
        tokens = line.split()
        # split id from description
        image_id, image_desc = tokens[0], tokens[1:]
        # skip images not in the set
        if image_id in dataset:
            # create list
            if image_id not in descriptions:
                descriptions[image_id] = []
            # wrap description in tokens
            desc = "startseq " + " ".join(image_desc) + " endseq"
            # store
            descriptions[image_id].append(desc)
    return descriptions


train_descriptions = load_clean_descriptions("Model/Inception/descriptions.txt", train)


def preprocess(image_path):
    """
    Preprocessing of the images.
    :param image_path: Image Path
    :return: preprocessed output
    """

    # Convert all the images to size 299x299 as expected by the inception v3 model
    img = image.load_img(image_path, target_size=(299, 299))

    # Convert PIL image to numpy array of 3-dimensions
    x = image.img_to_array(img)

    # Add one more dimension
    x = np.expand_dims(x, axis=0)

    # preprocess the images using preprocess_input() from inception module
    x = preprocess_input(x)

    return x


# Load the inception v3 model
model = InceptionV3(weights="imagenet")

# Configure GPU
with tf.device("/gpu:0"):
    config = tf.compat.v1.ConfigProto(
        gpu_options=tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=1)
        # device_count = {'GPU': 1}
    )
    config.gpu_options.allow_growth = True
    session = tf.compat.v1.Session(config=config)
    tf.compat.v1.keras.backend.set_session(session)
    tqdm().pandas()

# Create a new model, by removing the last layer (output layer) from the inception v3
model_new = Model(model.input, model.layers[-2].output)


# Function to encode a given image into a vector of size (2048, )
def encode(image):
    """
    Feature Extraction
    :param image: Path to test/train images
    :return: Encoding vector
    """
    image = preprocess(image)  # preprocess the image
    fea_vec = model_new.predict(image)  # Get the encoding vector for the image
    # reshape from (1, 2048) to (2048, )
    fea_vec = np.reshape(fea_vec, fea_vec.shape[1])
    return fea_vec


# Below are the Feature Extraction functions, it is recommended to use the Features already extracted
# and provided to you, SEE README
"""
# Training Features
start = time()
encoding_train = {}
for img in tqdm(train_img):
    encoding_train[img[len(images):]] = encode(img)
print("Time taken in seconds =", time()-start)


# Training Features in a File
import pickle
with open("featuresTrain_Inception.p", "wb") as encoded_pickle:
    pickle.dump(encoding_train, encoded_pickle)


# Testing Features
start = time()
encoding_test = {}
for img in tqdm(test_img):
    encoding_test[img[len(images):]] = encode(img)
print("Time taken in seconds =", time()-start)


# Testing Features in a File
with open("featuresTest_Inception.p", "wb") as encoded_pickle:
    pickle.dump(encoding_test, encoded_pickle)
"""

# Load the Training Features
train_features = load(open("featuresTrain_Inception.p", "rb"))
print("Photos: train=%d" % len(train_features))

# Create a list of all the training captions
all_train_captions = []
for key, val in train_descriptions.items():
    for cap in val:
        all_train_captions.append(cap)
len(all_train_captions)

# Consider only words which occur at least 10 times in the corpus
word_count_threshold = 10
word_counts = {}
nsents = 0
for sent in all_train_captions:
    nsents += 1
    for w in sent.split(" "):
        word_counts[w] = word_counts.get(w, 0) + 1

vocab = [w for w in word_counts if word_counts[w] >= word_count_threshold]
print("preprocessed words %d -> %d" % (len(word_counts), len(vocab)))

ixtoword = {}
wordtoix = {}

ix = 1
for w in vocab:
    wordtoix[w] = ix
    ixtoword[ix] = w
    ix += 1

vocab_size = len(ixtoword) + 1


def to_lines(descriptions):
    """
    Convert Dictionary to List
    :param descriptions: Clean Description
    :return: List of all descriptions
    """
    all_desc = []
    for key, value in descriptions.keys():
        [all_desc.append(d) for d in descriptions[key]]
    return all_desc


def max_length(descriptions):
    """
    Determine the maximum length
    :param descriptions: Clean Descriptions
    :return: Maximum Length
    """
    lines = to_lines(descriptions)
    return max(len(d.split()) for d in lines)


# determine the maximum sequence length
max_length = max_length(train_descriptions)
print("Description Length: %d" % max_length)


def data_generator(descriptions, photos, wordtoix, max_length, num_photos_per_batch):
    """
    Generate Data for model fitting
    :param descriptions: Clean Descriptions
    :param photos: Source of Image files
    :param wordtoix: Preprocessed words
    :param max_length: Maximum length of a Caption
    :param num_photos_per_batch: Batch Size oof images
    :return:
    """
    X1, X2, y = [], [], []
    n = 0
    # loop for ever over images
    while 1:
        for key, desc_list in descriptions.items():
            # retrieve the photo feature
            try:
                photo = train_features[key + ".jpg"]
            except Exception as e:
                continue
            n += 1
            for desc in desc_list:
                # encode the sequence
                seq = [wordtoix[word] for word in desc.split(" ") if word in wordtoix]
                # split one sequence into multiple X, y pairs
                for i in range(1, len(seq)):
                    # split into input and output pair
                    in_seq, out_seq = seq[:i], seq[i]
                    # pad input sequence
                    in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
                    # encode output sequence
                    out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
                    # store
                    X1.append(photo)
                    X2.append(in_seq)
                    y.append(out_seq)
            # yield the batch data
            if n == num_photos_per_batch:
                yield [array(X1), array(X2)], array(y)
                X1, X2, y = [], [], []
                n = 0


# Glove Vectors for further preprocessing
# using word vectors
glove_dir = ""
# An empty dictionary
embeddings_index = {}
f = open(os.path.join(glove_dir, "glove.6B.200d.txt"), encoding="utf-8")

for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype="float32")
    embeddings_index[word] = coefs
f.close()
print("Found %s word vectors." % len(embeddings_index))

embedding_dim = 200

# 200 dimensional vectors for 10000 words in vocab
embedding_matrix = np.zeros((vocab_size, embedding_dim))

for word, i in wordtoix.items():
    # if i < max_words:
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # Words not found in the embedding index will be all zeros
        embedding_matrix[i] = embedding_vector

# Model Building
inputs1 = Input(shape=(2048,))
fe1 = Dropout(0.5)(inputs1)
fe2 = Dense(256, activation="relu")(fe1)
inputs2 = Input(shape=(max_length,))
se1 = Embedding(vocab_size, embedding_dim, mask_zero=True)(inputs2)
se2 = Dropout(0.5)(se1)
se3 = LSTM(256)(se2)
decoder1 = add([fe2, se3])
decoder2 = Dense(256, activation="relu")(decoder1)
outputs = Dense(vocab_size, activation="softmax")(decoder2)
model = Model(inputs=[inputs1, inputs2], outputs=outputs)

# Model Summary
print(model.summary())

model.layers[2].set_weights([embedding_matrix])
model.layers[2].trainable = False

# Setting up Model, epochs, batch size
model.compile(loss="categorical_cross-entropy", optimizer="adam")

epochs = 10
number_pics_per_bath = 3
steps = len(train_descriptions) // number_pics_per_bath

# Saving the models after every Epoch
for i in range(epochs):
    with tf.device("/gpu:0"):
        generator = data_generator(
            train_descriptions,
            train_features,
            wordtoix,
            max_length,
            number_pics_per_bath,
        )
        model.fit_generator(generator, epochs=1, steps_per_epoch=steps, verbose=1)
        model.save("model_" + str(i) + ".h5")

model.optimizer.lr = 0.0001
epochs = 10
number_pics_per_bath = 6
steps = len(train_descriptions) // number_pics_per_bath

# Final Weight of Model
model.save_weights("models_Inception/model_30.h5")

##################################################################
##################### CLASSIFICATION #############################
##################################################################

model.load_weights("models_Inception/model_30.h5")

images = ""

with open("encoded_test_images.pkl", "rb") as encoded_pickle:
    encoding_test = load(encoded_pickle)


def greedySearch(photo):
    in_text = "startseq"
    for i in range(max_length):
        sequence = [wordtoix[w] for w in in_text.split() if w in wordtoix]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = ixtoword[yhat]
        in_text += " " + word
        if word == "endseq":
            break
    final = in_text.split()
    final = final[1:-1]
    final = " ".join(final)
    return final


for i in os.listdir("Flickr8k_Dataset/img"):
    if i in encoding_test.keys():
        print(i)
        break

pic = "1523984678_edd68464da.jpg"
image = encoding_test[pic].reshape((1, 2048))
x = plt.imread("Flickr8k_Dataset/img" + pic)
plt.imshow(x)
plt.show()
print("Caption:", greedySearch(image))
