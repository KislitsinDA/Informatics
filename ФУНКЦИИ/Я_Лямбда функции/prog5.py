def ask_password(login, password, success=True, failure=False):
    vowels = "aeiouy"
    amount_vowels = sum([1 for letter in password.lower() if letter in vowels])
    login_consonants = list(filter(lambda letter: letter not in vowels, login.lower()))
    password_consonants = list(filter(lambda letter: letter not in vowels, password.lower()))
    if amount_vowels == 3:
        if login_consonants == password_consonants:
            return success
        return failure, "Wrong consonants"
    if login_consonants == password_consonants:
        return failure, "Wrong number of vowels"
    return failure, "Everything is wrong"


def main(login, password):
    if type(ask_password(login, password)) == bool:
        print(f"Привет, {login}")
    else:
        print(f"Кто-то пытался притворится пользователем {login}, но в пароле допустил ошибку: "
              f"{ask_password(login, password)[1].upper()}")


main("anastasia", "nsyatos")
main("eugene", "aanig")