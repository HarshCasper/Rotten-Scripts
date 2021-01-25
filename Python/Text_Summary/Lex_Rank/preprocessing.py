#!/usr/bin/env python
# coding: utf-8


# Import
import spacy
import neologdn


class EnglishCorpus:
    """
    A Class for for retaining the structure of text file as a corpus.

    ...

    Methods:
        preprocessing(text:str)
            Remove Special Characters and whitespaces

        make_sentence_list(sentences:str)
            Break sentence into a list of sentence suing NLP

        make_corpus()
            Generates the corpus in Morphological order
    """

    # Preparation of morphological analyzer
    def __init__(self):
        """
        Constructor to initialize spaCy English model (See README)
        """
        self.nlp = spacy.load("en_core_web_sm")

    # Pre-processing of line breaks and special characters
    def preprocessing(self, text: str) -> str:
        """
        Removes white spaces and special characters.
        Generates a set of sentences.
        :param text: String of text to ge processed
        :return: Sentence without white space and special characters
        """
        text = text.replace("\n", "")
        text = neologdn.normalize(text)

        return text

    # Divide sentences into sentences while retaining the results of morphological analysis
    def make_sentence_list(self, sentences: str) -> list:
        """
        Retains Morphological analysis and divides sentences in list of sentences.
        Using Natural Language Processing
        :param sentences: Sentences with morphological meaning
        :return: List of sentence
        """
        doc = self.nlp(sentences)
        self.ginza_sents_object = doc.sents
        sentence_list = [s for s in doc.sents]

        return sentence_list

    # Put a space between words
    def make_corpus(self) -> list:
        """
        Puts the white spaces between words
        Generates Corpus
        :return: Corpus for Tokenizing
        """
        corpus = []
        for s in self.ginza_sents_object:
            tokens = [str(t) for t in s]
            corpus.append(" ".join(tokens))

        return corpus
