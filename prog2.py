step = int(input())
start = int(input())
finish = int(input())
additional = int(input())
if start < finish:
    for i in range(start, finish+1, step):
        print(i, end="\t")
elif start > finish:
    for i in range(start, finish-1, -step):
        print(i, end="\t")
