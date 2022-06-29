import sys

gematries = {}
for line in sys.stdin:
    if line == "\n":
        break
    else:
        gematries[line] = sum([ord(letter) - ord("A") + 1 for letter in line.upper()])

values = sorted(gematries.items(), key=lambda value: (value[-1], value[0]))
for word in values:
    print(word[0], end="")
