# Face-Recognition
***

Face-Recognition is a technology which detects the face of a person and predicts the name of the person from the database. It uses Python.

## Dependencies

- Python 
- Numpy
- OpenCV
- Scipy
- Scikit-learn
- dlib


## Implementation

- Create a folder "training-images".
- Add images of each person you want to recognise to a folder by their name in "training-images".
  Then copy all the images of that person in "./training-images/Name_Of_Person" folder.


<code>
    python create_encodings.py
</code>


- This will create "encoded-images-data.csv" and "labels.pkl" files.


<code>
    python train.py
</code>


- This will create "classifier.pkl" file. It will also create "classifier.pkl.bak" backup file if the classifier with that name already exists.

- Make folder "test-images" which contains all the images you want to find people in.



<code>
    python predict.py
</code>



Now you can see the faces with name on the screen.

![Face-Recognition](https://github.com/Debashish-hub/Rotten-Scripts/blob/master/Python/Face-Recognition/ezgif.com-gif-maker.gif)

## Author

[Debashish kumar sahoo](https://github.com/Debashish-hub)
