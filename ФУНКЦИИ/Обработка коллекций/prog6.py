import sys
current_item_index = 1
answer = []
for item in map(lambda line: line.lstrip(), sys.stdin):
    if item == "":
        break
    else:
        if item[0] == "#":
            answer.append(f"Line {current_item_index}: {item.lstrip('# ').rstrip()}")
    current_item_index += 1

print("\n".join(answer))
