import subprocess
import itertools


def dictate(parts):
    # todo: could feed it phrases one by one, to allow the user to pause
    input_string = " ".join(parts)
    subprocess.run(['say', '-v', 'Daniel'], stdout=subprocess.PIPE, input=input_string, encoding='utf-8')


def insert_pauses(parts, pause_length):
    if pause_length == 0:
        return parts

    pause_part = pause(pause_length)
    parts = [(part, pause_part) for part in parts]
    return list(itertools.chain.from_iterable(parts))


def pause(pause_length):
    return "[[slnc {0}]]".format(pause_length)
