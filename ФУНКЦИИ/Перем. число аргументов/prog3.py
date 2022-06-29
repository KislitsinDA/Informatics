def send_mail(name, date, email, place="Пермь"):
    print(f"To: {email}")
    print(f"Здравствуйте, {name}")
    print(f"Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдет {date}.")


send_mail(email="danilka@mail.ru", name="Роман", place="третьем кабинете", date="23.03.22")