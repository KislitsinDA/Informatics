class Knight:
    def __init__(self, row, col, color):
        self.row, self.col = row, col
        self.color = color

    def can_move(self, row1, col1):
        if 0 > row1 or row1 > 7 or 0 > col1 or col1 > 7:
            return False
        for i in [-2, 2]:
            for j in range(-1, 2, 2):
                if (self.row + i == row1 and self.col + j == col1) or (self.row + j == row1 and self.col + i == col1):
                    return True

    def set_position(self, row1, col1):
        if self.can_move(row1, col1):
            print('yes')

    def get_color(self):
        return self.color

    def char(self):
        return 'N'


WHITE = 1
BLACK = 2
row0 = 2
col0 = 2
knight = Knight(row0, col0, WHITE)
print('white' if knight.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(knight.char(), end='')
        elif knight.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
print('===========')
WHITE = 1
BLACK = 2
row0 = 0
col0 = 1
knight = Knight(row0, col0, WHITE)
print('white' if knight.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(knight.char(), end='')
        elif knight.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
print('===========')
WHITE = 1
BLACK = 2
row0_W = 0
col0_W = 1
knight_W = Knight(row0_W, col0_W, WHITE)
row0_B = 7
col0_B = 6
knight_B = Knight(row0_B, col0_B, BLACK)
print('white' if knight_W.get_color() == WHITE else 'black')
print('white' if knight_B.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if (row0_W, col0_W) == (row, col):
            print(knight_W.char(), end='')
        elif (row0_B, col0_B) == (row, col):
            print(knight_B.char(), end='')
        elif knight_W.can_move(row, col) or knight_B.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
