def choose_coffee(*preferences):
    inf = {"Эспрессо": [1, 0, 0], "Капучино": [1, 3, 0], "Маккиато": [2, 1, 0], "Кофе по-венски": [1, 0, 2],
           "Латте Маккиато": [1, 2, 1], "Кон Панна": [1, 0, 1]}
    for i in preferences:
        print(i)
        got = True
        for j in range(3):
            if ingredients[j] < inf.get(i)[j]:
                got = False
        if got:
            for g in range(3):
                ingredients[g] = inf.get(i)[g]
            return i
    return "К сожалению, мы не можем предложить вам напиток"


ingredients = [1, 2, 3]
print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна"))
print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна"))
print("-----")
ingredients.clear()
ingredients = [4, 4, 0]
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))