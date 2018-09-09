#!/usr/bin/env python3


import sys


current_word = None
current_label=None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word,label,count = line.split('\t')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word and current_label==label:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_word,current_label,current_count))
        current_count = count
        current_label=label
        current_word = word

# do not forget to output the last word if needed!
if current_word == word and current_label==label:
    print('%s\t%s\t%s' % (current_word,current_label,current_count))

