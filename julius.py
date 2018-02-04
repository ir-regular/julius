import os.path
import argparse
from julius.source.phrasefile import read_phrases
from julius.voice.say import insert_pauses, dictate
from julius.source.srs import Srs


def adhoc_handler(location, pause):
    if os.path.isfile(location):
        phrases = read_phrases(location)
        phrases = insert_pauses(phrases, pause)
    elif os.path.isdir(location):
        raise NotImplementedError('adhoc mode for directories not yet implemented')
    else:
        raise ValueError('Location must be a valid file or directory')

    try:
        dictate(phrases)
    except KeyboardInterrupt:
        exit(0)


def srs_handler(location, pause):
    srs = Srs(location)
    try:
        raise NotImplementedError('Srs not fully implemented - stats saved')
    except KeyboardInterrupt:
        exit(0)
    finally:
        srs.save_stats()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['adhoc', 'srs'], help='adhoc practice or spaced repetition system')
    # todo: could use type argument to automatically read in phrases?
    parser.add_argument('location', help='file or directory of files to use for dictation')
    # todo: validate that pause length, if provided, is > 0
    parser.add_argument('-p', '--pause', help='pause between phrases, in milliseconds', type=int, default=1000)
    args = parser.parse_args()

    if args.mode == 'adhoc':
        adhoc_handler(args.location, args.pause)
    else:
        srs_handler(args.location, args.pause)

if __name__ == "__main__":
    main()
