# Model

Inception and Xception model, imported using Keras, after the preprocessing of images
have been trained on the dataset.

The details about the Model can be found in the [Jupyter Notebooks](../Notebook).

Design of both the Model is similar:

![Design of Xception Model](https://i.postimg.cc/PrrD2sSy/model.png)

A link to the Models can be found
[here](https://drive.google.com/drive/folders/15p-DIFNw5N71gxmGNz84JuXuKpKZ4pN7?usp=sharing)

We have also used `GLoVe.6b` word representation model for determining word to word resemblance in captions.
Training is performed on aggregated global word-word co-occurrence statistics from the Dataset.

Here is a Direct [Link](https://github.com/stanfordnlp/GloVe) for the model.
