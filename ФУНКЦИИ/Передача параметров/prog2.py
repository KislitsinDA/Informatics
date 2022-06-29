daily_food = [0, 150, 150, 59, 450, 1400, 79, 560]


def count_food(days):
    chet = 0
    for i in days:
        chet += daily_food[i - 1]
    return chet


print(count_food([2, 3, 5, 7]))