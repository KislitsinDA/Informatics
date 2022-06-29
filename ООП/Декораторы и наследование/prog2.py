def check_password(func):
    def wrapper():
        password = "Yandex"
        new_password = input()
        if new_password == password:
            func()
        else:
            print("В доступе отказано")
    return wrapper()


@check_password
def fib():
    fib1, fib2 = 1, 1
    n = int(input())
    print(fib1, fib2, end=" ")
    for i in range(n - 2):
        fib1, fib2 = fib2, fib1 * fib2
        print(fib2, end=" ")

