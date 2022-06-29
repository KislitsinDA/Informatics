def simple_map(transformation, values):
    return list(map(transformation, values))


numbers = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, numbers))
