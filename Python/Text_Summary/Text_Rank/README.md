# Text_Rank
Text Rank approach for text summarization.

## Dependencies

- nltk
- numpy
- networkx

## NLTK models

- `stopwords`: Stopwords are the English words which does not add much meaning to a sentence.

## Setup

- Setup a `python 3.x` virtual environment.
- `Activate` the environment
- Install the dependencies using ```pip3 install -r requiremnts.txt```
- Setup the models by running the following commands,

```bash
$ python -m nltk.downloader stopwords
```
- Run the `text_summary.py` file
- Enter the source path.

## Results

The code generates the tokens (same as weights) of set of words, it shows the relative importance of words according to 
the summarizer, just uncomment the _l112_

Results can be found [here](../assets).
