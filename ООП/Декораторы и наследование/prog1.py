a = print()


def new_print(*args):
    for item in args:
        a(item.upper())


print = new_print
print("Нельзя ли потише?")
