name = input("Как вас зовут?: ")


def polite_input(question):
    return input(f"{name}, {question}")


age = polite_input('укажите возраст: ')
school_number = polite_input('укажите номер школы: ')
class_num = polite_input('укажите полный номер класса: ')