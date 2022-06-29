def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    return tribonacci(n) + tribonacci(n - 1) + tribonacci(n - 2)


print(tribonacci(0))
