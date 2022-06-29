import sys
heights = []
for line in sys.stdin:
    if line != "\n":
        heights.append(int(line))
    else:
        break
if heights:
    print(sum(heights) / len(heights))
else:
    print(-1)
