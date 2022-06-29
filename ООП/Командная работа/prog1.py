class Bishop:
    def __init__(self, row, col, color):
        self.row, self.col = row, col
        self.color = color

    def can_move(self, row1, col1):
        if 0 > row1 or row1 > 7 or 0 > col1 or col1 > 7:
            return False
        for i in range(-7, 8):
            j = abs(i)
            if (self.row + i == row1 and self.col + i == col1) or\
                    (self.row + j == row1 and self.col + j == col1) or\
                    (self.row + j == row1 and self.col + i == col1) or\
                    (self.row + i == row1 and self.col + j == col1):
                return True

    def set_position(self, row1, col1):
        if self.can_move(row1, col1):
            print('yes')

    def get_color(self):
        return self.color

    def char(self):
        return 'B'


WHITE = 1
BLACK = 2
row0 = 0
col0 = 2
bishop = Bishop(row0, col0, WHITE)
print('white' if bishop.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(bishop.char(), end='')
        elif bishop.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()


WHITE = 1
BLACK = 2
row0 = 4
col0 = 5
bishop = Bishop(row0, col0, BLACK)
print('white' if bishop.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(bishop.char(), end='')
        elif bishop.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
