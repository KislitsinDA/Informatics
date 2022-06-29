class Profile:
    def __init__(self, job):
        self.job = job

    def info(self):
        return ""

    def describe(self):
        return f"Профессия: {self.job}, {self.info()}"


class Vacancy(Profile):
    def __init__(self, job, salary):
        super().__init__(job)
        self.salary = salary

    def info(self):
        return f"Предлагаемая зарплата: {self.salary}"


class Resume(Profile):
    def __init__(self, job, experiance):
        super().__init__(job)
        self.exp = experiance

    def info(self):
        return f"Стаж работы: {self.exp}"


doctor_vacancy = Vacancy("doctor", 25000)
doctor_resume = Resume("doctor", 3)
print(doctor_vacancy.describe())
print(doctor_resume.describe())
