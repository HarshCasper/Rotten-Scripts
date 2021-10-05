"""

Copyright (C) 2019-2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

Modified from https://github.com/Visual-mov/Colorful-Julia (MIT License)

"""

from markovmeme.utils import list_corpus
import random
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))


# Generation Functions


def generate_text(corpus, use_model=True, size=10):
    """Based on a corpus file prefix in "corpus" generate either word-based
    ngram (wordgram) model, or just randomly select a sentence from
    the corpus.

    Parameters
    ==========
    corpus: the prefix of the corpus file, is checked to exist
    use_model: boolean. Choose an actual sentence or generate one.
    size: The number of words to generate (only for a model).
    """
    # Get the corpus file, if not provided a full path
    if not os.path.exists(corpus):
        corpus = get_corpus(corpus)

    if use_model:
        return generate_words_markov(corpus, size=size)
    return select_sentence(corpus)


# Word Gram Models


def generate_word_grams(text):
    """Generate a lookup of words mapped to the next occurring word, and
    we can use this to generate new text based on occurrence.
    """
    words = text.split()
    wordgrams = {}

    # Add each word to the lookup
    for i in range(len(words) - 1):

        # Have lookup be all lowercase version
        word = words[i].lower()

        if word not in wordgrams:
            wordgrams[word] = []

        # Each entry should have the next occurring word
        wordgrams[word].append(words[i + 1])

    # The last word potentially doesn't have any following
    word = words[len(words) - 1].lower()
    if word not in wordgrams:
        wordgrams[word] = []
    return wordgrams


def select_sentence(corpus):
    """Given a corpus file, split based on sentences and randomly select
    a sentence.
    """
    text = load_corpus(corpus)
    return "%s." % random.choice(text.split(".")).strip()


def generate_words_markov(corpus, size=10):
    """Generate a word lookup based on unique words, and for each
    have the values be the list of following words to choose from.
    Randomly select a next word in this fashion. We don't
    take punctuation into account, but we do capitalize the
    first letter and end the entire thing with a period.
    """
    # Load filename into list of words
    text = load_corpus(corpus)
    words = text.split()

    # Generate words lookup
    grams = generate_word_grams(text)

    # Now generate the sentence of a particular size
    current = random.choice(words)
    result = current.capitalize()
    for _ in range(size):

        # Always look up entirely lowercase
        possibilities = grams[current.lower()]
        if len(possibilities) == 0:
            break
        next_word = random.choice(possibilities)
        result = "%s %s" % (result, next_word)
        current = next_word

    # Ensure we end in a period.
    if result[-1] in [",", "", " ", "!"]:
        result = result[:-1]

    result = "%s." % result
    return result


# Corpus Functions


def get_corpus(prefix):
    """load a corpus file from "corpus" in the same directory as this script.
    we assume a .txt extension, and return the full path to the file.
    """
    selection = list_corpus(remove_ext=False)
    selected = "%s.txt" % (prefix)

    # Return filename if exists
    corpus_folder = os.path.join(here, "data", "corpus")
    filename = os.path.join(corpus_folder, selected)

    if not os.path.exists(filename):
        sys.exit("Missing corpus file %s" % filename)

    return filename


def load_corpus(filename):
    """Given a filename, load the corpus to build the model. This is called by
    both generation functions.
    """
    if not os.path.exists(filename):
        sys.exit("Cannot find %s" % filename)

    # Read and get rid of newlines
    with open(filename, "r") as filey:
        text = filey.read().replace("\n", " ")
    return text
