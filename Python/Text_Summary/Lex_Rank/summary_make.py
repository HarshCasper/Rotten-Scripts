from preprocessing import EnglishCorpus

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer


def summarize_sentences(sentences: str, language="english") -> list:
    """
    Prepares the summary of sentences.
    Calls preprocessing for generating a list of processed sentences.
    Uses LexRank Summarization for preparing summary.
    :param sentences: Sentences form the text file
    :param language: Language used, default=English
    :return: Summary of the source file
    """
    # Preparation sentences
    corpus_maker = EnglishCorpus()
    preprocessed_sentences = corpus_maker.preprocessing(sentences)
    preprocessed_sentence_list = corpus_maker.make_sentence_list(
        preprocessed_sentences)
    corpus = corpus_maker.make_corpus()
    parser = PlaintextParser.from_string(" ".join(corpus), Tokenizer(language))

    # Using Rank system for tokenizing the Headwords
    summarizer = LexRankSummarizer()

    # Generating stopwords, i.e. words which are not affecting the context of the text.
    summarizer.stop_words = get_stop_words(language)

    # Limiting the summary to one-fifth of the article (See README)
    summary = summarizer(document=parser.document,
                         sentences_count=len(corpus) * 2 // 10)

    return summary
