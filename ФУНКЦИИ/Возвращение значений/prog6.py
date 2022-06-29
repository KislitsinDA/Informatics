def print_documents(pages):
    otv = ""
    for i in pages:
        if "Секретно" in i:
            return otv + "Дальнешие материалы засекречены"
        otv += i + " "
    return otv + "Напечатанно без купюр"


print(print_documents(["1", "2", "3 Секретно", "4", "5", " '6'"]))