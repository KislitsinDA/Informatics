example = [4, 1, 5, 2, 3, 10]
print(example, id(example))


def variable_and_plus(value, addition):
    value = value + addition
    print(value, id(value))


variable_and_plus(example, [0])
print(example, id(example))