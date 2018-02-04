import subprocess

def dictate(parts):
    subprocess.run(['say', '-v', 'Daniel'], stdout=subprocess.PIPE, input=parts, encoding='utf-8')

def join_with_pauses(parts, pauseLength):
    return pause(pauseLength).join(parts)

def pause(pauseLength):
    return " [[slnc {0}]] ".format(pauseLength) if (pauseLength > 0) else " "