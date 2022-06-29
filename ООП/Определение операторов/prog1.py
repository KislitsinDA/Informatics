class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.p = proteins
        self.f = fats
        self.c = carbohydrates

    def get_proteins(self):
        return self.p

    def get_fats(self):
        return self.f

    def get_carbohydrates(self):
        return self.c

    def get_kcalories(self):
        kcalories = 4 * self.p + 9 * self.f + 4 * self.c
        return kcalories

    def __add__(self, other):
        return FoodInfo(self.p + other.p, self.f + other.f, self.c + other.c)


food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2
print(food1.get_proteins(), food1.get_fats(),
      food1.get_carbohydrates(), food1.get_kcalories())
print(food2.get_proteins(), food2.get_fats(),
      food2.get_carbohydrates(), food2.get_kcalories())
print(food3.get_proteins(), food3.get_fats(),
      food3.get_carbohydrates(), food3.get_kcalories())
