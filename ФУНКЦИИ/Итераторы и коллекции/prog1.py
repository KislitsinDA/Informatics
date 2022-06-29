import sys

text = [word.strip("' ../::!?") for line in sys.stdin for word in line.split()]
words = []
answer = []
for pair in enumerate(text):
    if pair[1].istitle() and pair[1] not in words:
        words.append(pair[1])
        answer.append(pair)
for pair in sorted(answer, key=lambda word: word[1]):
    print(f"{pair[0]}, {pair[1]}")
