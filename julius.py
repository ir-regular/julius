import argparse
from julius.source.phrasefile import read_phrases
from julius.voice.say import join_with_pauses, dictate

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--phrases", help="phrase list file location", required=True)
    # todo: validate that pause length, if provided, is > 0
    parser.add_argument("-p", "--pause", help="pause between phrases, in milliseconds", type=int, default=1000)
    args = parser.parse_args()

    phrases = read_phrases(args.phrases)
    output = join_with_pauses(phrases, args.pause)

    try:
        # todo: could feed it phrases one by one, to allow the user to pause
        dictate(output)
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
