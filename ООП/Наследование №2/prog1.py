class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


incorrect_triangle = Triangle(4, 3, 6)
print(incorrect_triangle.perimeter())
correct_triangle = EquilateralTriangle(5)
print(correct_triangle.perimeter())
