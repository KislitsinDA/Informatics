phr = []


def parrot(phrase):
    phr.append(phrase)
    if phr.count(phrase) > 1:
        print(phrase)


parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")

parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")