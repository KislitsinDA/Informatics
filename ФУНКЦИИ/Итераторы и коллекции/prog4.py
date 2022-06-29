import itertools
suits = ["бубен", "пик", "треф", "червей"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
extra_suit = input("Какую часть не выводить: ")
for card in itertools.product(cards, suits):
    print(*card)
