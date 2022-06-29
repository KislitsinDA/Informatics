def defractalize(fractal1):
    for i in fractal1:
        if i == fractal1:
            fractal1.remove(i)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)

fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)