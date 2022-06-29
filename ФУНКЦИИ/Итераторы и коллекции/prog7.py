import math
import functools
import sys

numbers = [int(number) for number in sys.stdin]
print(functools.reduce(lambda x, y: math.gcd(x, y), numbers))
