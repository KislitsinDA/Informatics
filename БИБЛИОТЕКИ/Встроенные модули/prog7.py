import datetime
import math

birth = input().split(".")
birth1 = int(birth[2]), int(birth[1]), int(birth[0])
bio = input().split(".")
bio1 = int(bio[2]), int(bio[1]), int(bio[0])
bio11 = 23
bio22 = 28
bio33 = 33
raz = datetime.date(*bio1) - datetime.date(*birth1)
print(round(math.sin(2 * math.pi * raz.days / bio11) * 100, 2))
print(round(math.sin(2 * math.pi * raz.days / bio22) * 100, 2))
print(round(math.sin(2 * math.pi * raz.days / bio33) * 100, 2))
