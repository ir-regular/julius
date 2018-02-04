import os.path
import argparse
from julius.source.phrasefile import read_phrases
from julius.voice.say import insert_pauses, dictate

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['adhoc', 'srs'], help='adhoc practice or spaced repetition system')
    # todo: could use type argument to automatically read in phrases?
    parser.add_argument('location', help='file or directory of files to use for dictation')
    # todo: validate that pause length, if provided, is > 0
    parser.add_argument('-p', '--pause', help='pause between phrases, in milliseconds', type=int, default=1000)
    args = parser.parse_args()

    if args.mode == 'adhoc':
        if os.path.isfile(args.location):
            phrases = read_phrases(args.location)
            phrases = insert_pauses(phrases, args.pause)
        elif os.path.isdir(args.location):
            raise NotImplementedError('adhoc mode for directories not yet implemented')
        else:
            raise ValueError('Location must be a valid file or directory')
    else:
        # args.mode == 'srs' because otherwise argparse would have errored out
        raise NotImplementedError('srs not yet implemented')

    try:
        dictate(phrases)
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
