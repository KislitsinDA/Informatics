def continue_fibonacci_sequence(sequence1, n):
    for i in range(n):
        next_element = sequence1[-1] + sequence1[-2]
        sequence1.append(next_element)


sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)

sequence = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence, 0)
print(*sequence)