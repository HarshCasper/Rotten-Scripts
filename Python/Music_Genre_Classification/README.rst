Music_Genre_Classification
==========================

|checkout|

Music genre classification is one of the most basic yet fascinating
DL/ML project. People use different approaches ranging from basi
classification techniques like Survey and questionnaire to highly
advanced combinations of Machine Learning Classifiers. The script that
follows is a very basic implementation of one such model, revolving
around Deep Learning, **Sequential Model**.

This script will not only enable you to setup a basic classification
system, but will also help in feature extraction, dataset division,
training and testing. Please be advised, that the aim is not to setup a
really advanced classification system, but rather a simple setup, using
a renowned dataset, to predict the genre of a musical piece using
minimal features.

Dependency
----------

The dependencies are summed uup in
`requirements.txt <requirements.txt>`__.

A separate list is also available below:

-  librosa
-  csv
-  Keras
-  TensorFlow
-  numba
-  numpy
-  pandas
-  scikit-learn
-  scipy

Considering there are some big libraries here, it is recommended to
setup a virtual environment first. This `link <https://realpython.com/lessons/creating-virtual-environment/>`__
might help.

Dataset
-------

We have used GTZAN dataset for our task. It is publicly available, here
is the `link <http://marsyas.info/downloads/datasets.html>`__. For more
information about the Dataset, click `here <https://www.kaggle.com/carlthome/gtzan-genre-collection>`__.

Feature Extraction
------------------

`LibRosa <https://librosa.org/>`__ along with SciPy has been used for
Feature Extraction.

As this is a much simpler approach, only *6 Features* have been used
along with their deltas, taking the total number of useful features to
26.

Here is a list of the Features.

-  chroma stft
-  rmse
-  spectral centroid
-  spectral bandwidth
-  rolloff
-  zero crossing rate

For those interested,
`this <https://librosa.org/doc/latest/index.html>`__ and
`this <https://github.com/vybhav72954/Audio_Features>`__ link will
provide explanations about these and many more useful Audio Features.
The features extracted are contained in a `CSV <Features/GTZAN.csv>`__,
which can be used by anyone if the user wants to test accuracy of
another classifier using the same features extracted.

Setup
-----

1. A virtual environment (recommended)
2. ``pip install -r requirements.txt``
3. Extract Features using
   `feature_extraction.py <feature_extraction.py>`__, it is
   recommended to use the CSV file, rather than downloading the whole
   Dataset if same features re being extracted.

   -  If different features are to be extracted, or the user wants to
      extract features himself only, download the dataset (use links
      provided above). Feed the path, proper headers and extract
      features.

4. The features extracted are saved in a ``csv`` file, the same file is
   used for training, the
   `genre_classification.py <genre_classification.py>`__ script
   contains proper comments to help the user.

Sample Output
-------------

.. code:: py

   7/7 [==============================] - 2s 5ms/step - loss: 2.2042 - accuracy: 0.1935
   Epoch 2/20
   7/7 [==============================] - 0s 5ms/step - loss: 1.8557 - accuracy: 0.3668
   Epoch 3/20
   7/7 [==============================] - 0s 5ms/step - loss: 1.6626 - accuracy: 0.3710
   Epoch 4/20
   7/7 [==============================] - 0s 5ms/step - loss: 1.4863 - accuracy: 0.4496
   Epoch 5/20
   7/7 [==============================] - 0s 5ms/step - loss: 1.3252 - accuracy: 0.5336
   Epoch 6/20
   7/7 [==============================] - 0s 5ms/step - loss: 1.2093 - accuracy: 0.5683
   Epoch 7/20
   '
   '
   '
   '
   '
   Epoch 18/20
   7/7 [==============================] - 0s 5ms/step - loss: 0.5832 - accuracy: 0.8097
   Epoch 19/20
   7/7 [==============================] - 0s 6ms/step - loss: 0.5832 - accuracy: 0.8078
   Epoch 20/20
   7/7 [==============================] - 0s 6ms/step - loss: 0.5296 - accuracy: 0.8529
   7/7 [==============================] - 0s 3ms/step - loss: 1.0282 - accuracy: 0.6750

Here is a brief summary of the model:

::

   Model: "sequential"
   _________________________________________________________________
   Layer (type)                 Output Shape              Param #   
   =================================================================
   dense (Dense)                (None, 256)               6912      
   _________________________________________________________________
   dense_1 (Dense)              (None, 128)               32896     
   _________________________________________________________________
   dense_2 (Dense)              (None, 64)                8256      
   _________________________________________________________________
   dense_3 (Dense)              (None, 10)                650       
   =================================================================
   Total params: 48,714
   Trainable params: 48,714
   Non-trainable params: 0
   _________________________________________________________________

In order to access the pre-trained model, click
`here <https://drive.google.com/drive/folders/1H5Sj-5eZ_ABCb0AF1wAqq5Waowk2__Pi?usp=sharing>`__

Note
----

The **average accuracy obtained is 67.50%**, which is obviously not a
really good number, but one needs to understand that with only 6 Major
features and a simple implementation of Sequential Model, without any
feature selection or rejection, one can’t hope for a better accuracy.
One must understand that GTZAN is a really old dataset and after going
through multiple research papers, the best number I was able to find was
*~85%*.

This code provides a really basic implementation of Deep Learning and
Music Genre classification, users are free to manipulate the code and
find better combination themselves.

P.S. - Even this implementation can attain higher accuracies with minor
tweaks.

.. code:: py

   275/275 [==============================] - 5s 20ms/step - loss: 0.7065 - acc: 0.7793 - val_loss: 0.9531 - val_acc: 0.7172
   Epoch 499/500
   274/275 [============================>.] - ETA: 0s - loss: 0.7031 - acc: 0.7777Epoch 1/500
   275/275 [==============================] - 5s 19ms/step - loss: 0.7019 - acc: 0.7780 - val_loss: 0.9383 - val_acc: 0.7258
   Epoch 500/500
   274/275 [============================>.] - ETA: 0s - loss: 0.6644 - acc: 0.7929Epoch 1/500
   275/275 [==============================] - 5s 20ms/step - loss: 0.6635 - acc: 0.7932 - val_loss: 0.9442 - val_acc: 0.7273

Here the attained accuracy is closer to 80%.

Author(s)
---------

Made by `Vybhav Chaturvedi <https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/>`__

If you like this script, I have made Repos related to `Music Classification and Music Human Emotion mapping <https://github.com/vybhav72954/Music-Mood-Analysis>`__ , `Music Feature Classification <https://github.com/vybhav72954/Audio_Features>`__.

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Music_Genre_Classification/

