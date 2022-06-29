import sys

answer = {}
for line in sys.stdin:
    population_amount = int(line[line.rfind(" ") + 1:][:-1]) // 100000 * 100
    if(population_amount, population_amount + 100) not in answer.keys():
        answer[(population_amount, population_amount + 100)] = [line[:line.find(" ")]]
    else:
        previous_city = answer.get((population_amount, population_amount + 100))
        answer[(population_amount, population_amount + 100)] = [*previous_city, line[:line.find(" ")]]
for amount in sorted(answer, key=lambda x: x[0]):
    print(f"{amount[0]} , {amount[1]}: {', '.join(sorted(answer.get(amount)))}")
