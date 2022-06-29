import sys
amount = 0
for item in map(lambda line: line.lstrip(), sys.stdin):
    if item == "":
        break
    else:
        if item[0] == "#":
            amount += 1
print(amount)
