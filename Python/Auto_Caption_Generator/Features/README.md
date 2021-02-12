# Features

For both Inception and Xception model, same technique has been used.

For Feature extraction, Transfer learning has been used, that is, using pretrained models already trained on large
datasets and extract the features from these models and use those features itself. Both Inception and Xception have
been trained on imagenet dataset that had 1000 different classes to classify.

Using Keras, both these Models can be imported, and their weights are automatically downloaded.

Since we have used a different Dataset, further preprocessing is required.

- Change the image size to `299*299*3` as input.
- Remove the Last classification layer (Used for imagenets)
- Generate Feature Vectors.

Here is a Google Drive [link](https://drive.google.com/drive/folders/1PUgH3f-dFYFPuSDeJVif-AmAtOsvSww_?usp=sharing)
where you can find extracted features.
