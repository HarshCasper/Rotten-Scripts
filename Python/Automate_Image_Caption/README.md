# Automated Caption Generator

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oSUxHpz6UIEhtGjOw_SCAYWxYodwCYpf)

**Automatic Image Captioning**, using Deep Learning and Flickr-8k Dataset.
Also made a comparison between Xception Model and Inception Model.

This is the easiest way to generate captions and alt text for all kind of images using
Convolutional Neural Networks and a type of Recurrent Neural Network (LSTM).

## About

The image features will be extracted from CNN models trained on the imagenet dataset (see below)
and then the features are fed into the LSTM model which will be responsible for generating the image captions.

This Repo revolves around 2 Models provided by Keras.

- [Inception](https://keras.io/api/applications/inceptionv3/)
- [Xception](https://keras.io/api/applications/xception/)

1. Features Extracted can be found [here](Features)
1. Dataset used can be found [here](Dataset)
1. Jupyter Notebooks can be found [here](Notebook)
1. Models Trained can be found [here](Model)
1. Requirements and dependencies can be found [here](requirements.txt)

Want to contribute? Suggestions, Error reporting, Bug Solving are highly
appreciated, please open an Issue and/or PR
[here](https://github.com/vybhav72954/Automated_Image_Captioning)

## Setup 

- Setup a Virtual Environment (HIGHLY RECOMMENDED)
- Activate the Environment.
- Install Requirements, use `pip3 install -r requirements.txt`
  - NOTE: A GPU accelerated hardware is recommended, after `TF v2.1`,
    _there is no need to install GPU separately._ So no need to use `pip3 install tensorflow-gpu`
    For GPU, separate Guidelines are provided [here](#GPU).
- See the Google Drive links for features, dataset and models.
- Download the required files.

### GPU

It is recommended to train these Neural Networks using GPU accelerated hardware.
User first need to have a CUDA enabled Graphics Card, if this condition is met, Download CUDA toolkit and cuDNN library.

For installation and help, these links are helpful:

[Official CUDA Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)

[Official CUDNN Installation Guide](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)

[An easy walk-through](https://medium.com/swlh/cuda-installation-in-windows-2020-638b008b4639)

## Usage

1. Start with changing the hardcoded paths in the python scripts.
2. If yu want to train the Network yourself (GPU recommended), run the whole script.
3. You can skip, Feature Extraction and Selection and Model training by downloading the required files.
4. Comment out the code you wnt to skip.
5. Classification Task is separately marked.
6. For only classification, execute only those functions which are invoked during the task.
7. Check Notebooks for an interactive example.
8. Inception Model uses GloVe word vectors, see [this](Model/README.md), download  the file beforehand.

#### Author

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/).
I have plans to update this project even further but that is beyond he scopes of this Repo, **Rotten-Scripts** is not
meant for Deep Learning but is a accumulation of scripts in multiple languages.

Check this [Repo](https://github.com/vybhav72954/Automated_Image_Captioning), if you have further
interests in Preprocessing using word ranking, and BLEU.

## Disclaimer

Using GPU for training these networks can lead to Memory overflow errors,
long sessions can lead to overheating issues and can cause similar problems related to GPU computing.

Carefully read the CUDA guidelines to avoid any problems.
