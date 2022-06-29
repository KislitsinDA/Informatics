import sys
import functools

print(functools.reduce(lambda x, y: x if x < y else y, sys.stdin))
