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
    files_due = srs.get_files_due()

    while files_due:
        file = files_due.pop(0)

        phrases = read_phrases(os.path.join(location, file))
        phrases = insert_pauses(phrases, pause)

        try:
            dictate(phrases)
            print('Dictation paused.')
            if confirm('Please check your results for file {0}: are they correct?'.format(file)):
                srs.file_processed(file)
            else:
                srs.file_failed(file)
            if files_due and not confirm('Would you like to proceed to the next file?'):
                break

        except KeyboardInterrupt:
            exit(0)
        except EOFError:
            exit(0)

    if files_due:
        print('There remain {0} files to be reviewed today.'.format(len(files_due)))
    else:
        print('Nothing else to be reviewed today.')


def confirm(prompt):
    prompt = prompt + ' [y/n]'
    while True:
        try:
            return distutils.util.strtobool(input(prompt))
        except ValueError:
            print('Please answer one of: yes, y, no, n.')


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
