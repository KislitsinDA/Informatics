n = int(input("Количество слов: "))
words = [input().lower() for _ in range(n)]
answer = []
for check_word in words:
    current_answer = [check_word]
    for word in words:
        if check_word== word:
            continue
        if len(check_word) == len(word) and set(check_word) == set(word):
            current_answer.append(word)
    answer.append(sorted(current_answer))
for pairs in sorted(answer):
    if answer.count(pairs) > 1:
        answer.remove(pairs)
for pairs in sorted(answer):
    print(" ".join(pairs))
