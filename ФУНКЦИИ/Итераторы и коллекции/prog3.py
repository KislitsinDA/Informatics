answer = []
table = [input().split() for _ in range(3)]
a = [int(number) for number in table[0]]
b = [int(number) for number in table[1]]
c = [int(number) for number in table[3]]
for column in zip(a, b, c):
    if sum(column) != sum(a) or not(sum(a) == sum(b) == sum(c)):
        answer.append(0)
if all(answer):
    print("YES")
else:
    print("NO")
