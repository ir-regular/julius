import subprocess
import itertools


def dictate(parts):
    """Converts `parts` to valid input for mac os 'say' util."""
    # todo: could feed it phrases one by one, to allow the user to pause
    input_string = " ".join(parts)
    subprocess.run(['say', '-v', 'Daniel'], stdout=subprocess.PIPE, input=input_string, encoding='utf-8')


def insert_pauses(parts, pause_length):
    """
    Returns a list of phrases interleaved with pauses, encoded for mac os 'say' util.

    >>> insert_pauses(['a', 'b', 'c'], 100)
    ['a', '[[slnc 100]]', 'b', '[[slnc 100]]', 'c']

    Skips pauses of length 0 in order to enable smooth dictation at top speed.
    >>> insert_pauses(['a', 'b', 'c'], 0)
    ['a', 'b', 'c']

    Doesn't care about type of parts elements, so you can vary pause length using complex structures.
    >>> earworm = [['badger', 'badger'], ['mushroom', 'mushroom']]
    >>> earworm = [insert_pauses(l, 100) for l in earworm]
    >>> insert_pauses(earworm, 1000)
    [['badger', '[[slnc 100]]', 'badger'], '[[slnc 1000]]', ['mushroom', '[[slnc 100]]', 'mushroom']]
    """
    if pause_length == 0:
        return parts

    pause_part = pause(pause_length)
    parts = [(part, pause_part) for part in parts]
    return list(itertools.chain.from_iterable(parts))[:-1]


def pause(pause_length):
    """Return a pause, encoded for mac os 'say' util.

    >>> pause(500)
    '[[slnc 500]]'
    """
    return "[[slnc {0}]]".format(pause_length)
