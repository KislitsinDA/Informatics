from sys import stdin
from xlsxwriter import Workbook

workbook = Workbook("receipt.xlsx")


def make_receipt(goods):
    worksheet = workbook.add_worksheet()
    repeat_goods = []
    for i in range(len(goods)):
        name = goods[i].get("name")
        price = goods[i].get("price")
        amount = goods[i].get("amount")
        is_repeated = False

        for repeat_good in repeat_goods:
            if [name, price] == repeat_good[:-2]:
                worksheet.write(repeat_good[-1], 2, amount + repeat_good[2])
                is_repeated = True
        if not is_repeated:
            worksheet.write(i, 0, name)
            worksheet.write(i, 1, price)
            worksheet.write(i, 2, amount)
            worksheet.write_formula(i, 3, f'=B{i + 1} * C{i + 1}')
            repeat_goods.append([name, price, amount, i])
    worksheet.write_formula(len(repeat_goods), 3, f"=SUM(D1:D{len(repeat_goods)}")


def create_repipt():
    info = []
    for line in stdin:
        if line[:1] != "...":
            info.append({"name": line[:-1].split()[0], "price": float(line[:-1].split()[1]),
                        "amount": (line[:-1].split()[2])})
        else:
            make_receipt(info)
            info = []
    workbook.close()

'''
молоко 49.99 2
колбаса 546.50 1
сыр 154 3
яйцо 12.02 10
мука 119.99 6
колбаса 536.50 2
---
тетрадь 29.50 2
антистресс 75.6 1
сметана 71 1
лампочка 157.99 1
тетрадь 29.50 2
'''
