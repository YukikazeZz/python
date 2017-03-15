#!/usr/bin/python
from __future__ import print_function
import os
import sys


def count_words(filename):
    d={}
    with open(filename) as f:
        for line in f:
            for fword in [word for word in line.strip().split(':') if not word.isdigit() and word]:
                d.setdefault(fword,0)
                d[fword] += 1

    for key,val in d.iteritems():
        print(key,':',val)

def main():
    sys.argv.append("")
    filename=sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit('{0} not found'.format(filename))
    else:
        count_words(filename)


if __name__=="__main__":
    main()
