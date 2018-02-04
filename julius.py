import argparse
from julius.source.phrasefile import read_phrases
from julius.voice.say import insert_pauses, dictate

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--phrases", help="phrase list file location", required=True)
    # todo: validate that pause length, if provided, is > 0
    parser.add_argument("-p", "--pause", help="pause between phrases, in milliseconds", type=int, default=1000)
    args = parser.parse_args()

    phrases = read_phrases(args.phrases)
    phrases = insert_pauses(phrases, args.pause)

    try:
        dictate(phrases)
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
