def golden_ratio(i):
    fibonacci = [1, 1]
    for j in range(i):
        num_1 = fibonacci[j] + fibonacci[j + 1]
        fibonacci.append(num_1)
    print(fibonacci[i] / fibonacci[i - 1])


golden_ratio(4)
