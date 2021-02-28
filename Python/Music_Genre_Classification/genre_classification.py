#!/usr/bin/env python3

# Imports

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

import keras

from keras import models
from keras import layers

# Path to the CSV containing the Features
path = input("Enter the Full Path of the CSV file.")

# Reading the CSV files
data = pd.read_csv(path)
data.head()

data = data.drop(['filename'], axis=1)
data.head()

# Extracting the Label
genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)
print(y)

# Model Preprocessing
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Loading a Sequential Model using Keras
model = models.Sequential()
model.add(layers.Dense(256, activation='relu',
                       input_shape=(X_train.shape[1],)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Using Adam Optimization for smoothing
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Determining the number of Epoch, and Batch Sizes
history = model.fit(X_train,
                    y_train,
                    epochs=20,
                    batch_size=128)

# Deliverables
test_loss, test_acc = model.evaluate(X_test, y_test)
print('test_acc: ', test_acc)
predictions = model.predict(X_test)

# Saving the Model
model.save('name.h5')
