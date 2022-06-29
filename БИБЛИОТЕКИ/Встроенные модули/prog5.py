from random import sample
import string

alp = list(string.ascii_letters)


def generate_password(m):
    return "".join(sample(alp, k=m))


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
