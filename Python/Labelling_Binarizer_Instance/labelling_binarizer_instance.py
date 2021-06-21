from sklearn.preprocessing import Imputer, LabelBinarizer, LabelEncoder, OneHotEncoder
import numpy as np
import pickle


def null_values(data):
    data = data.isna().sum()
    return data[list(map(lambda x: x[1] != 0, data.iteritems()))]


class SingletonLabelBinarizer:
    def __init__(self, *args, **kwargs):
        self.label_binarizer = LabelBinarizer()

    def fit(self, x):
        self.label_binarizer.fit(x)

    def transform(self, x):
        return self.label_binarizer.transform(x)

    def fit_transform(self, x):
        return self.label_binarizer.fit_transform(x)

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SingletonLabelBinarizer, cls).__new__(cls)
        return cls.instance

    @property
    def encoder(self):
        return self.label_binarizer

    @encoder.setter
    def encoder(self, x):
        self.label_binarizer = LabelBinarizer()

    def inverse_transform(self, y):
        return self.label_binarizer.inverse_transform(y)
