import nltk.data
import re


def read_sentences(filename):
    # todo: need to find a way for people to download this easily
    pickle = 'downloads/nltk_data/tokenizers/punkt/english.pickle'
    tokenizer = nltk.data.load(pickle)
    with open(filename) as fp:
        contents = fp.read()
    sentences = [split_into_phrases(sentence)
                 for sentence in tokenizer.tokenize(contents)]
    return sentences


def split_into_phrases(sentence):
    return re.split(r'\s+', sentence)
