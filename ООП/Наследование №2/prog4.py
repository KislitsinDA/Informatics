class Summator:
    def transform(self, n):
        return n

    def sum(self, m):
        return sum([self.transform(i) for i in range(m + 1)])


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 3


a = PowerSummator(4)
print(a.sum(3))
