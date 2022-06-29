import sys
unique_money = []
amount = 0
for line in sys.stdin:
    if line[:-1] not in unique_money:
        unique_money.append(line[:-1])
    else:
        amount += int(line[:line.find(" ")])
print(amount)
