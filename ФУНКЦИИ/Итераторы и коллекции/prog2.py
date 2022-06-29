import sys

books = [book for book in input().split("\t")]
shops = []
prices = []
for line in sys.stdin:
    shops.append(line.split("\t")[0])
    prices.append([int(amount) for amount in line.split("\t")[1:]])
answered_shop = min(list(zip(shops, [sum(amount) for amount in prices])), key=lambda x: x[1])[0]
print(answered_shop)
for pair in list(zip(books, [current_amounts for current_amounts in prices[shops.index(answered_shop)]])):
    print(*pair)

'''
Арифметика для старших Геометрия в четырехмерье Эсперанто для начинающих
Пятёрка 205 300 420
Академкнига 500 200 250
Всё для школы 350 350 350
'''