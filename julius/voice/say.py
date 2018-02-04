import subprocess
import itertools

def dictate(parts):
    # todo: could feed it phrases one by one, to allow the user to pause
    input = " ".join(parts)
    subprocess.run(['say', '-v', 'Daniel'], stdout=subprocess.PIPE, input=input, encoding='utf-8')

def insert_pauses(parts, pauseLength):
    if pauseLength == 0:
        return parts

    pausePart = pause(pauseLength)
    parts = [(part, pausePart) for part in parts]
    return list(itertools.chain.from_iterable(parts))

def pause(pauseLength):
    return "[[slnc {0}]]".format(pauseLength)