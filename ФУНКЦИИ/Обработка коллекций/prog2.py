n = int(input("Колличество классов: "))
info = []
for i in range(n):
    info.append([input()[-1] for _ in range(int(input("Сколько человек в классе: ")))])
for classroom in info:
    for i in range(len(classroom)):
        if classroom[i] != "5":
            classroom[i] = False
        else:
            classroom[i] = True
if all([any(classroom) for classroom in info]):
    print("YES")
else:
    print("NO")
