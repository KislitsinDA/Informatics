import datetime as dt


class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        date_1 = dt.date(2019, self.month, self.day)
        date_2 = dt.date(2019, other.month, other.day)
        total_date = str(date_1 - date_2).split()
        if len(total_date) != 1:
            return total_date[0]
        else:
            return 0

jan5 = Date(1, 5)
jan1 = Date(1, 1)
print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)
