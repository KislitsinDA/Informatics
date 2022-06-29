def transpose(matrix):
    mat = []
    for i in range(len(matrix[0])):
        mat2 = []
        for j in matrix:
            mat2.append(j[i])
        mat.append(mat2)
    global matrix1
    matrix1 = mat


matrix1 = [[1]]
transpose(matrix1)
for line in matrix1:
    print(*line)
print("-----")
matrix1 = [[1, 2], [3, 4]]
transpose(matrix1)
for line in matrix1:
    print(*line)