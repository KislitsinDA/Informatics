def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return "Составное"
    return "Простое"


print(prime(1))
