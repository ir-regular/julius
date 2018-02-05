import os.path
import argparse
import distutils.util
from julius.source.phrasefile import read_phrases
from julius.voice.say import insert_pauses, dictate
from julius.source.srs import Srs


def adhoc_handler(location, pause):
    if os.path.isfile(location):
        phrases = read_phrases(location)
        phrases = insert_pauses(phrases, pause)
    else:
        raise ValueError('Location must be a valid file')

    try:
        dictate(phrases)
    except KeyboardInterrupt:
        exit(0)


def srs_handler(location, pause):
    srs = Srs(location)
    files_due = srs.get_files_due()

    while files_due:
        file = files_due.pop(0)

        phrases = read_phrases(os.path.join(location, file))
        phrases = insert_pauses(phrases, pause)

        try:
            dictate(phrases)
        except KeyboardInterrupt:
            exit(0)

        if confirm('Are your results for file {0} correct?'.format(file)):
            srs.file_processed(file)
        else:
            srs.file_failed(file)

        if files_due:
            if not confirm('Dictate the next file?'):
                break


def confirm(prompt):
    prompt = prompt + ' [y/n]'
    while True:
        try:
            return distutils.util.strtobool(input(prompt))
        except ValueError:
            print('Please answer one of: yes, y, no, n.')
        except EOFError:
            print("I'll take it as a no, then.")
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['adhoc', 'srs'],
                        help='adhoc practice or spaced repetition system')
    # todo: could use type argument to automatically read in phrases?
    parser.add_argument('location',
                        help='file or directory of files to use for dictation')
    # todo: validate that pause length, if provided, is > 0
    parser.add_argument('-p', '--pause', type=int, default=1000,
                        help='pause between phrases, in milliseconds')
    args = parser.parse_args()

    if args.mode == 'adhoc':
        adhoc_handler(args.location, args.pause)
    else:
        srs_handler(args.location, args.pause)


if __name__ == "__main__":
    main()
