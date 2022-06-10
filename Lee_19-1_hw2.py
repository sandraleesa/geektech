class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):
    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.salary < self.company_bank:
            print("У компании не достаточно средств!")
        else:
            print("Вот Ваша зарплата.")

    def person_info(self):
        print(f"""Имя: {self.first_name}
                  Фамилия: {self.last_name}
                  Зарплата: {self.salary}  """)
