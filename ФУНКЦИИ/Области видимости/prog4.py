num1 = 1
item = []


def add_item(item_name, item_cost):
    item.append([item_name, str(item_cost)])


def print_receipt():
    global num1, item
    chet = 0
    if item:
        print(f"Чек {num1}. Всего продуктов: {len(item)}")
        for i in item:
            print(" - ".join(i))
            chet += int(i[1])
        print(f"Итого: {chet}")
        print("----------------")
        num1 += 1
        item.clear()


add_item('Блокнот', 100)
print_receipt()
add_item('Ручка', 70)
print_receipt()
print_receipt()
add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()
add_item('Булочка', 15)
add_item('Булочка', 15)