class Summator:
    def transform(self, n):
        return n

    def sum(self, m):
        return sum([self.transform(i) for i in range(m + 1)])


class SqareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


a = SqareSummator()
print(a.sum(3))
