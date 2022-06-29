def find_mountain(heightsMap):
    maxim = 0
    row, pillar = 0, 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] > maxim:
                maxim = heightsMap[i][j]
                row, pillar = i, j
    return row, pillar


print(find_mountain([[1, 3, 1], [3, 2, 5], [2, 2, 2]]))
