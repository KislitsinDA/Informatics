def matrix(width=1, height=False, item=0):
    if not height:
        otv = [[item] * width] * width
    else:
        otv = [[item] * width] * height
    return otv


rows = matrix()
for row in rows:
    print(*row)
print("-------")
rows = matrix(2)
for row in rows:
    print(*row)