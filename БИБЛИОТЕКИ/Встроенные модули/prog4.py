import datetime

current_data = datetime.datetime.now()
current_data = current_data.date()
n = int(input("Введите кол-во дней: "))
data_dr = current_data + datetime.timedelta(days=n)
print(data_dr.day, data_dr.month)
