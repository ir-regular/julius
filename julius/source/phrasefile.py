import csv
import random

def read_phrases(filename):
    phrases = []

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # todo: allow an indication of phrase frequency - allow phrases to appear multiple times per read
            phrases.append(row[0])

    random.shuffle(phrases)

    return phrases