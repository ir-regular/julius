# Julius: a dictation tool for shorthand practice

## What it does

Given a list of words, it shuffles them and reads them back to
you at a specified rate.

## Usage

**Julius is currently a Mac-only utility.**

`python julius.py adhoc sample/1.csv -p 1000`

Dictates the specified file, pausing for 1 second between each phrase.

`python julius.py srs sample`

Dictates all files from the specified directory that are
due for practice today.

### Command syntax

`python julius.py <mode> <path> [-p <value>]`

- `mode`: `adhoc` (single file) or `srs` (multiple files, uses a spaced
    repetition system to aid memorisation)
- `path`: a filepath (to the file or directory to dictate)
- `-p <value>`: optional, the length of pauses between phrases
    (in milliseconds) - defaults to 1000, or 1 second.

## SRS mode

### How it works

After taking down each phrase file scheduled for learning today,
Julius will pause and ask if you managed to write all the phrases
correctly.

If you didn't, the file will get scheduled for practice on the next day.

If you did, the file will get scheduled for practice some time in
the future. How far in the future exactly depends on how many times
you've practiced writing down phrases from the same file successfully:
you will see the same content again in 1, 2, 4, 7, 11, 14, 21, 35, 70,
or 105 days.

### Why it works

How easy it is for us to recall something depends on how long ago we
memorised it. When studying according to an SRS (spaced repetition
system) schedule, you refresh your memory in increasingly larger
intervals, until the information becomes fully integrated. It is vital
to check the system every day, so that your backlog doesn't grow too
large.

## Rationale

If you have a Mac, you could type `say "Hello world" -r 30 -v Alex`.
If you don't, there are tools online with similar functionality.
Unfortunately the effect is usually horribly creepy, as the tools
reeeeeaaaad theeeee woooords sloooowly with an electronic buzz.

So in order to un-creep myself I wrote Julius. It reads phrases
at a normal speed, inserting pauses between them.
