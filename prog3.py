string_1 = input().split()
string_2 = input().split("-L-")
string_3 = input().split(">W<")

for word1 in string_1:
    words_2 = []
    words_3 = []
    for word2 in string_2:
        if len(set(word2)) >= 3:
            for letter in set(word2):
                if letter.lower() in word1.lower():
                    words_2.append(word2.upper())
                    break
    for word3 in string_3:
        if len(word3) <= len(word1) and word3.islower():
            words_3.append(word3)

    print(f'{word1}:')
    print('; '.join(words_2))
    print(' * '.join(words_3))
