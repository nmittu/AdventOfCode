import sys

with open(sys.argv[1]) as f:
    print sum([int(i) for i in f.readlines()])
