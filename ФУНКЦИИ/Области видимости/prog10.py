inf = []


def do_bet(num, bet):
    if bet == 0 or num < 1 or num > 10:
        return "Что-то пошло не так, попробуйте еще раз"
    if num not in inf:
        inf.append(num)
        return f"Ваша ставка в размере {bet} на лошадь номер {num} принята. Попрощайтесь со своими деньгами =)"
    return "Что-то пошло не такб попробуйте еще раз"


print(do_bet(1, 10))
print(do_bet(1, 100))
print(do_bet(2, 0))
print(do_bet(2, 200))