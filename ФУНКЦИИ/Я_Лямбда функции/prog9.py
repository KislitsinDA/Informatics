def same_by(characteristic, objects):
    qualified_list = list(filter(characteristic, objects))
    if objects == qualified_list:
        return True
    return False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")
