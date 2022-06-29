def mirror(arr2):
    arr2.extend(arr2[::-1])


arr = [1, 2]
mirror(arr)
print(*arr)

arr = [1]
mirror(arr)
print(*arr)