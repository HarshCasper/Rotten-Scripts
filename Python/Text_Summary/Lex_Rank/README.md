# Lex_Rank
Lex Rank approach for text summarization.


## Dependencies

- sumy
- spacy
- neologdn
    * _This requires requires C++11 compiler_. CLick [here](https://pypi.org/project/neologdn/)
    for documentation and [here](https://nuwen.net/mingw.html#install) 
    for the C++11 compiler I use.

## NLTK models

- `en_core_web_sm`: A spaCy english multi-task CNN trained on OntoNotes.
- `punkt`: NLP sentence tokenizer

## Setup

- Setup a `python 3.x` virtual environment.
- `Activate` the environment
- Install the dependencies using ```pip3 install -r requiremnts.txt```
    * Install C++ compiler if `neologdn` is triggering `wheel` errors.
- Setup the models by running the following commands,

```bash
$ python -m spacy download en_core_web_sm
$ python -c "import nltk; nltk.download('punkt')"
```
- Run the `main.py` file
- Enter the source path.

## Results

Results can be found [here](../assets).
