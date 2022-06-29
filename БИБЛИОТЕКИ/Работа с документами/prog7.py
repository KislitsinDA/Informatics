from sys import stdin
from xlsxwriter import Workbook

info = [{"name": line[:-1].split()[0], "prise": float(line[:-1].split()[1], "amount": int(line[:-1].split()[2])}
        for line in stdin]
workbook = Workbook("receipt.xlsx")
worksheet = workbook.add_worksheet()
for i in range(len(info)):
    worksheet.write(i, 0, info[i].get("name"))
    worksheet.write(i, 1, info[i].get("price"))
    worksheet.write(i, 2, info[i].get("amount"))
    worksheet.write_formula(i, 3, f'=B{i + 1} * C{i + 1}')
worksheet.write_formula(len(info), 3, f'SUM(D1:D{len(info)})')
workbook.close()


'''
молоко 49.99 2
колбаса 546.50 1
сыр 154 3
яйцо 12.02 10
мука 119.99 6
'''