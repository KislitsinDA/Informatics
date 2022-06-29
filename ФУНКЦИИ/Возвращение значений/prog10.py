def roots_of_quadratic_equation(a, b, c):
    otv = [" "]
    if a == 0 and b == 0:
        if c != 0:
            otv[0] = "Корней нет"
    elif a == 0 and b != 0:
        otv[0] = -c / b
    else:
        disc = (b ** 2 - 4 * a * c) ** 0.5
        if disc > 0:
            otv[0] = (-b - disc) / (2 * a)
            otv.append((-b + disc) / (2 * a))
        elif disc == 0:
            otv[0] = (-b / (2 * a))
        else:
            otv[0] = "Корней нет"
    return otv


result = roots_of_quadratic_equation(1, 2, 1)
print(*sorted(result))
result = roots_of_quadratic_equation(1, -3, 2)
print(*sorted(result))