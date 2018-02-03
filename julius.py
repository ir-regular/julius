import argparse
import csv
import random
import subprocess

def read_phrases(filename):
    phrases = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # todo: allow an indication of phrase frequency - allow phrases to appear multiple times per read
            phrases.append(row[0])

    random.shuffle(phrases)

    return phrases

def join_phrases(phrases, pauseLength):
    return "[[slnc {0}]]".format(pauseLength).join(phrases)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--phrases", help="phrase list file location", required=True)
    # todo: validate that pause, if provided, is > 0
    parser.add_argument("-p", "--pause", help="pause between phrases, in milliseconds", type=int, default=1000)
    args = parser.parse_args()

    phrases = read_phrases(args.phrases)
    output = join_phrases(phrases, args.pause)

    try:
        # todo: could feed it phrases one by one, to allow the user to pause
        subprocess.run(['say', '-v', 'Daniel'], stdout=subprocess.PIPE, input=output, encoding='ascii')
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
