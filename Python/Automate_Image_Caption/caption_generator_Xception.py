# -*- coding: utf-8 -*-

import string
from PIL import Image
import os
from pickle import dump, load
import numpy as np
from keras.applications.xception import Xception, preprocess_input
from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers.merge import add
from keras.models import Model, load_model
from keras.layers import Input, Dense, LSTM, Embedding, Dropout
import matplotlib as plt

# small library for seeing the progress of loops.
from tqdm.notebook import tqdm
import tensorflow as tf

with tf.device("/gpu:0"):
    config = tf.compat.v1.ConfigProto(
        gpu_options=tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=1)
        # device_count = {'GPU': 1}
    )
    config.gpu_options.allow_growth = True
    session = tf.compat.v1.Session(config=config)
    tf.compat.v1.keras.backend.set_session(session)
    tqdm().pandas()
    """
    import tensorflow as tf
    device_name = tf.test.gpu_device_name()
    if device_name != '/device:GPU:0':
      raise SystemError('GPU device not found')
    print('Found GPU at: {}'.format(device_name))
    """

    def load_doc(filename):
        """
        Function for loading various files
        :param filename: Source Path
        """
        # Opening the file as read only
        with open(filename) as file:
            text = file.read()
        return text

    def all_img_captions(filename):
        """
        Load the captions of images
        :param filename: Source path
        :return: Captions
        """
        file = load_doc(filename)
        captions = file.split("\n")
        descriptions = {}
        for caption in captions[:-1]:
            img, caption = caption.split("\t")
            if img[:-2] not in descriptions:
                descriptions[img[:-2]] = [caption]
            else:
                descriptions[img[:-2]].append(caption)
        return descriptions

    def cleaning_text(captions):
        """
        Cleaning Captions, lower casing, removing punctuations and words containing numbers
        :param captions:
        :return: clean captions
        """
        table = str.maketrans("", "", string.punctuation)
        for img, caps in captions.items():
            for i, img_caption in enumerate(caps):
                img_caption.replace("-", " ")
                desc = img_caption.split()

                # converts to lower case
                desc = [word.lower() for word in desc]
                # remove punctuation from each token
                desc = [word.translate(table) for word in desc]
                # remove hanging 's and a
                desc = [word for word in desc if (len(word) > 1)]
                # remove tokens with numbers in them
                desc = [word for word in desc if (word.isalpha())]
                # convert back to string

                img_caption = " ".join(desc)
                captions[img][i] = img_caption
        return captions

    def text_vocabulary(descriptions):
        """
        Generate all the unique words from captions
        :param descriptions: Captions
        :return: Set of unique words
        """
        # build vocabulary of all unique words
        vocab = set()
        for key, value in descriptions.keys():
            [vocab.update(d.split()) for d in descriptions[key]]
        return vocab

    def save_descriptions(descriptions, filename):
        """
        Save captions in one file
        :param descriptions: Captions
        :param filename: Destination file
        """
        lines = []
        for key, desc_list in descriptions.items():
            for desc in desc_list:
                lines.append(key + "\t" + desc)
        data = "\n".join(lines)
        with open(filename) as file:
            file.write(data)

    # Set these path according to project folder in you system
    dataset_text = "Flickr8k_text"
    dataset_images = "Flickr8k_Dataset/img"

    # we prepare our text data
    filename = dataset_text + "/" + "Flickr8k.token.txt"
    # loading the file that contains all data
    # mapping them into descriptions dictionary img to 5 captions
    descriptions = all_img_captions(filename)
    print("Length of descriptions =", len(descriptions))

    # cleaning the descriptions
    clean_descriptions = cleaning_text(descriptions)

    # building vocabulary
    vocabulary = text_vocabulary(clean_descriptions)
    print("Length of vocabulary = ", len(vocabulary))

    # saving each description to file
    save_descriptions(clean_descriptions, "Model/Xception/descriptions.txt")

    # Below are the Feature Extraction functions, it is recommended to use the Features already extracted
    # and provided to you, SEE README

    """
    def extract_features(directory):
        with tf.device('/device:GPU:0'):
            model = Xception(include_top=False, pooling='avg')
            features = {}
            for img in tqdm(os.listdir(directory)):
                filename = directory + "/" + img
                image = Image.open(filename)
                image = image.resize((299, 299))
                image = np.expand_dims(image, axis=0)
                # image = preprocess_input(image)
                image = image / 127.5
                image = image - 1.0
    
                feature = model.predict(image)
                features[img] = feature
            return features
    
    
    # 2048 feature vector
    features = extract_features(dataset_images)
    dump(features, open("features_GPU.p", "wb"))
    """

    # Load Already extracted features

    features = load(open("features_Xception.p", "rb"))

    def load_photos(filename):
        """
        Load Photos from directories
        :param filename: path to photos
        :return: photos
        """
        file = load_doc(filename)
        photos = file.split("\n")[:-1]
        return photos

    def load_clean_descriptions(filename, photos):
        """
        Load clean captions
        :param filename: path to captions
        :return: clean captions
        """
        file = load_doc(filename)
        descriptions = {}
        for line in file.split("\n"):

            words = line.split()
            if len(words) < 1:
                continue

            image, image_caption = words[0], words[1:]

            if image in photos:
                if image not in descriptions:
                    descriptions[image] = []
                desc = "<start> " + " ".join(image_caption) + " <end>"
                descriptions[image].append(desc)

        return descriptions

    def load_features(photos):
        """
        Load features for selected photos
        :param photos: Path to photos
        :return: features
        """
        all_features = load(open("features_Xception.p", "rb"))
        features = {k: all_features[k] for k in photos}
        return features

    filename = dataset_text + "/" + "Flickr_8k.trainImages.txt"

    # train = loading_data(filename)
    train_imgs = load_photos(filename)
    train_descriptions = load_clean_descriptions(
        "Model/Xception/descriptions.txt", train_imgs
    )
    train_features = load_features(train_imgs)

    def dict_to_list(descriptions):
        """
        Convert Dictionary of captions to list
        :param descriptions: Dict of captions
        :return: List of captions
        """
        all_desc = []
        for key, value in descriptions.keys():
            [all_desc.append(d) for d in descriptions[key]]
        return all_desc

    # creating tokenizer class
    # this will provide a vectorised text corpus
    # each integer will represent token in dictionary


    def create_tokenizer(descriptions):
        """
        Generate Tokens form list of captions
        :param descriptions: Dict of captions
        :return: Tokens
        """
        desc_list = dict_to_list(descriptions)
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(desc_list)
        return tokenizer

    # give each word an index, and store that into tokenizer.p pickle file
    tokenizer = create_tokenizer(train_descriptions)
    dump(tokenizer, open("Model/Xception/tokenizer.p", "wb"))
    vocab_size = len(tokenizer.word_index) + 1

    def max_length(descriptions):
        """
        Maximum Length of Caption
        :param descriptions: Dict of captions
        :return: Length of captions
        """
        desc_list = dict_to_list(descriptions)
        return max(len(d.split()) for d in desc_list)

    max_length = max_length(descriptions)

    def data_generator(descriptions, features, tokenizer, max_length):
        """
        Data Generator, for 6000 images, data cant be stored in any strycture
        Yield data in batches.
        :param descriptions: path to description.txt
        :param features: Loaded Features
        :param tokenizer: Index value or Token
        :param max_length: Maximum length o Captions
        :return: Yields of  data
        """
        while 1:
            for key, description_list in descriptions.items():
                # retrieve photo features
                feature = features[key][0]
                input_image, input_sequence, output_word = create_sequences(
                    tokenizer, max_length, description_list, feature
                )
                yield [input_image, input_sequence], output_word

    def create_sequences(tokenizer, max_length, desc_list, feature):
        """
        Creates sequence from batches.
        :param tokenizer: index
        :param max_length: max length of caption
        :param desc_list: List of description
        :param feature: Features of the images
        :return: Data generated in sequence of Arrays
        """
        X1, X2, y = [], [], []
        # walk through each description for the image
        for desc in desc_list:
            # encode the sequence
            seq = tokenizer.texts_to_sequences([desc])[0]
            # split one sequence into multiple X,y pairs
            for i in range(1, len(seq)):
                # split into input and output pair
                in_seq, out_seq = seq[:i], seq[i]
                # pad input sequence
                in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
                # encode output sequence
                out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
                # store
                X1.append(feature)
                X2.append(in_seq)
                y.append(out_seq)
        return np.array(X1), np.array(X2), np.array(y)

    # You can check the shape of the input and output for your model
    [a, b], c = next(
        data_generator(train_descriptions, features, tokenizer, max_length)
    )
    a.shape, b.shape, c.shape

    from keras.utils import plot_model

    with tf.device("/device:GPU:0"):
        # define the captioning model
        def define_model(vocab_size, max_length):
            """
            Model description
            :param vocab_size: Number of unique words ti be trained
            :param max_length: Maximum length
            :return: Merged CNN and LSTM model
            """
            # features from the CNN model squeezed from 2048 to 256 nodes
            inputs1 = Input(shape=(2048,))
            fe1 = Dropout(0.5)(inputs1)
            fe2 = Dense(256, activation="relu")(fe1)

            # LSTM sequence model
            inputs2 = Input(shape=(max_length,))
            se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
            se2 = Dropout(0.5)(se1)
            se3 = LSTM(256)(se2)

            # Merging both models
            decoder1 = add([fe2, se3])
            decoder2 = Dense(256, activation="relu")(decoder1)
            outputs = Dense(vocab_size, activation="softmax")(decoder2)

            # tie it together [image, seq] [word]
            model = Model(inputs=[inputs1, inputs2], outputs=outputs)
            model.compile(loss="categorical_cross-entropy", optimizer="adam")

            # summarize model
            print(model.summary())
            plot_model(model, to_file="Model/Xception/model.png", show_shapes=True)

            return model

    print("Dataset: ", len(train_imgs))
    print("Descriptions: train=", len(train_descriptions))
    print("Photos: train=", len(train_features))
    print("Vocabulary Size:", vocab_size)
    print("Description Length: ", max_length)

    model = define_model(vocab_size, max_length)
    epochs = 10
    steps = len(train_descriptions)
    os.mkdir("models_Xception")
    for i in range(epochs):
        generator = data_generator(
            train_descriptions, train_features, tokenizer, max_length
        )
        model.fit(generator, epochs=1, steps_per_epoch=steps, verbose=1)
        model.save("models6/model_" + str(i) + ".h5")

    ##################################################################
    ##################### CLASSIFICATION #############################
    ##################################################################
    img_path = "Flickr8k_Dataset/img/1523984678_edd68464da.jpg"

    max_length = 32
    tokenizer = load(open("Model/Xception/tokenizer.p", "rb"))
    model = load_model("models_Xception/model_9.h5")
    xception_model = Xception(include_top=False, pooling="avg")

    def extract_feature(filename, model):
        """
        Feature Extraction for the file to be classified
        :param filename: Path to file
        :param model: Model to be used
        :return: Features
        """
        try:
            image = Image.open(filename)

        except:
            print(
                "ERROR: Couldn't open image! Make sure the image path and extension is correct"
            )
        image = image.resize((299, 299))
        image = np.array(image)
        # for images that has 4 channels, we convert them into 3 channels
        if image.shape[2] == 4:
            image = image[..., :3]
        image = np.expand_dims(image, axis=0)
        image = image / 127.5
        image = image - 1.0
        feature = model.predict(image)
        return feature

    def word_for_id(integer, tokenizer):
        """
        Tokenizing words
        """
        for word, index in tokenizer.word_index.items():
            if index == integer:
                return word
        return None

    def generate_desc(model, tokenizer, photo, max_length):
        """
        Generates Description for Captions to map them with Images
        :param model: Path of Model
        :param tokenizer: Path of Tokenizer
        :param photo: Path o Image
        :param max_length:
        :return:
        """
        in_text = "start"
        for i in range(max_length):
            sequence = tokenizer.texts_to_sequences([in_text])[0]
            sequence = pad_sequences([sequence], maxlen=max_length)
            pred = model.predict([photo, sequence], verbose=0)
            pred = np.argmax(pred)
            word = word_for_id(pred, tokenizer)
            if word is None:
                break
            in_text += " " + word
            if word == "end":
                break
        return in_text

    # path = 'Flicker8k_Dataset/111537222_07e56d5a30.jpg'
    photo = extract_feature(img_path, xception_model)
    img = Image.open(img_path)

    description = generate_desc(model, tokenizer, photo, max_length)
    print("\n\n")
    print(description)
    plt.imshow(img)
    plt.show()
