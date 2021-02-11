#!/usr/bin/env python
# coding: utf-8

# Import from summary_make.py
from summary_make import summarize_sentences


def main():
    """
    Main function, wrapper around summary_make
    """
    filepath = input("Enter the Source File: ")
    with open(filepath, encoding='utf-8') as f:
        sentences = f.readlines()
    sentences = ' '.join(sentences)

    summary = summarize_sentences(sentences)

    filepath_index = filepath.find('.txt')
    outputpath = filepath[:filepath_index] + '_lexRank.txt'

    with open(outputpath, 'w') as w:
        for sentence in summary:
            w.write(str(sentence) + '\n')


if __name__ == "__main__":
    main()
