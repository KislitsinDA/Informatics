def check_password(password):
    def real_decorator(func):
        if password == "ranger":
            func()
        else:
            print("В доступе отказано")
    return real_decorator()


@check_password("ranger")
def hello():
    print("Hello")
