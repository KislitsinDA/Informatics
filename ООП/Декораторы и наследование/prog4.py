def cached(func):
    memory = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]
    return wrapper


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(7))
