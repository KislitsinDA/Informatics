import itertools
dictionary = input().lower().split()
letter = input().lower().split()
answer = []
for word in letter:
    is_readable = True
    for new_word in itertools.permutations(word, len(word)):
        new_word = "".join([*new_word])
        if new_word in dictionary and new_word != word:
            answer.append("#" * len(word))
            is_readable = False
    if is_readable:
        answer.append(word)
print(" ".join(answer))
