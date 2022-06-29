from random import choices
alp = "abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ23456789"


def generate_password(m):
    while True:
        pas = "".join(choices(alp, k=m))
        if pas.isalnum() and pas.lower() != pas and pas.upper() != pas:
            return pas


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
