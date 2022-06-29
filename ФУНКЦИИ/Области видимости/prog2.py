def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def smaller_root(p, q):
    return(-p - discriminant(1, p, q) ** 0.5) / 2


def larger_root(p, q):
    return (-p + discriminant(1, p, q) ** 0.5) / 2


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))


main()
