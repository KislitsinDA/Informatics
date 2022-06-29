class ReversedList:
    def __init__(self, lst):
        self.ls = lst[::-1]

    def __str__(self):
        return str(self.ls)

    def __len__(self):
        return len(self.ls)

    def __getitem__(self, index):
        return self.ls[index]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])
