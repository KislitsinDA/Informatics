import itertools
cards = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "валет", "дама", "король", "туз"]
suits = ["бубен", "пик", "треф", "червей"]
all_combinations = list(itertools.combinations(list(itertools.product(cards, suits)), 3))
for combinations in all_combinations:
    is_greater_9 = False
    is_hearts = False
    for pair in combinations:
        if pair[0] in cards[9:] or int(pair[0]) == 10:
            is_greater_9 = True
        if pair[1] == "червей":
            is_hearts = True
    if is_greater_9 and is_hearts:
        list_combinations = []
        for pair in combinations:
            list_combinations.append(" ".join([*pair]))
        print(", ".join(list_combinations))
