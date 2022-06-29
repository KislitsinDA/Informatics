def is_rhythm(phrases):
    vowels = "аяеёуоыиюэ"
    amounts = []
    for phrase in phrases.split():
        amounts.append(len(list(filter(lambda letter: letter in vowels, phrase))))
    if len(set(amounts)) == 1:
        return "Парам-пам-пам"
    return "Пам парам"


print(is_rhythm(input()))
