import random
import string

alp = list(string.ascii_letters + string.digits)


def generate_password(m):
    global alp
    return "".join(random.sample(alp, m))


def main(n, m):
    par = []
    for i in range(n):
        par.append(generate_password(m))
    return par


print("Случайный пароль из 7 символов: ", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
