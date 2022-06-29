string = []
string.extend(input("Очень важная строка: "))
string2 = input("Грезы(записать через(--)): ").split(" -- ")
right_string = []
for word in string2:
    amount = 0
    letter_word = list(set(word))
    for letter in set(string):
        if letter in letter_word:
            amount += 1
    if amount >= 4:
        right_string.append(word)
print(" = ".join(right_string))

