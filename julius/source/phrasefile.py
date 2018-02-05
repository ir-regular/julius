import csv
import random


def read_phrases(filename):
    """
    Read and shuffle phrases from a specified file

    >>> p = read_phrases('sample/1.csv')
    >>> len(p) == 37
    True
    >>> ('able' in p)
    True
    """
    phrases = []

    # todo: allow a second column with an indication of phrase frequency
    # (in order allow phrases to appear multiple times per read)

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            phrases.append(row[0])

    random.shuffle(phrases)

    return phrases
