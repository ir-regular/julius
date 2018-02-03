# Julius: a dictation tool for shorthand practice

## What it does

Given a list of words, it shuffles them and reads them back to
you at a specified rate.

## Usage

**Julius is currently a Mac-only utility.**

`julius.py -w wordlist.csv -p 500`

### Flags

`-w` the location of a wordlist file, with a phrase per line

`-p` the length of pauses between phrases, in milliseconds

## Rationale

If you have a Mac, you could type `say "Hello world" -r 30 -v Alex`.
If you don't, there are tools online with similar functionality.
Unfortunately the effect is usually horribly creepy, as the tools
reeeeeaaaad theeeee woooords sloooowly with an electronic buzz.

So in order to un-creep myself I wrote Julius. It reads phrases
at a normal speed, inserting pauses between them.
