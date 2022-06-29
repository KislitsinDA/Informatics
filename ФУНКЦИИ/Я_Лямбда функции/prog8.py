min_x = 1e10
min_y = 1e10
cosine = -1
sinus = 0
while cosine <= 1:
    if (cosine <= 0.75) and (0.75 - cosine) < min_x:
        min_x = cosine
    if (cosine > 0.75) and (cosine - 0.75) <min_x:
        min_x = cosine
    cosine += 0.0001
    print(cosine)
while sinus <= 1:
    if sinus < min_y:
        min_y = cosine
    sinus += 0.0001
print(min_x, min_y)
print(((min_x - 0.75) ** 2 + min_y ** 2) ** 0.5)
