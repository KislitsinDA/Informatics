num = input().split()
last_num = num[-1]
last_last = num[:-1]
need_num = []
for num in set(last_last):
    if len(num) == 3:
        if int(num) > int(last_num):
            need_num.append(num)
print(" ".join(need_num))
