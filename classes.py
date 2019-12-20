import datetime


class Employee:
    COMPANY_NAME = "organization"
    DOMAIN_NAME = "com"

    employee_count = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email_id = first_name + "." + last_name + \
                        "@" + self.COMPANY_NAME + "." + self.DOMAIN_NAME

        Employee.employee_count += 1

    def __repr__(self):
        return f"Employee(\"{self.first_name}\", \"{self.last_name}\", {self.salary})"

    def __str__(self):
        return f"{self.full_name}, {self.salary}, {self.email_id}"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.full_name)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, full_name):
        first, last = full_name.split(" ")
        self.first_name = first
        self.last_name = last

    def welcome(self):
        return f"{self.first_name}, Welcome to {self.COMPANY_NAME}.{self.DOMAIN_NAME}"

    @classmethod
    def set_company_name(cls, name):
        cls.COMPANY_NAME = name

    @classmethod
    def get_employee(cls, data):
        first, last, salary = data.split("-")
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        return not (day.weekday() == 5 or day.weekday == 6)


class Developer(Employee):
    DOMAIN_NAME = "dev"

    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        str = super().__str__()
        return str + f", {self.prog_lang}"

    @classmethod
    def get_employee(cls, data):
        first, last, salary, lang = data.split("-")
        return cls(first, last, salary, lang)


class Manager(Employee):
    DOMAIN_NAME = "man"


print(f"Welcome to {Employee.COMPANY_NAME}.{Employee.DOMAIN_NAME}")

emp1 = Employee("Pradip", "Gajjar", 500000)
emp2 = Employee("Rakesh", "Gajjar", 600000)

print(emp1)
print(emp2)

emp3 = Employee("Aarav", "Gajjar", 1000000)
print(Employee.__str__(emp3))

print(f"{emp1.welcome()}")
print(f"{emp2.welcome()}")
print(f"{emp3.welcome()}")
Employee.set_company_name("test")
print(f"Welcome to {Employee.COMPANY_NAME}.{Employee.DOMAIN_NAME}")
print(f"{emp1.welcome()}")
print(f"{emp2.welcome()}")
print(f"{emp3.welcome()}")

print(f"{emp1.welcome()}")
print(f"{emp2.welcome()}")
print(f"{emp3.welcome()}")
emp1.COMPANY_NAME = "startup"
print(f"Welcome to {Employee.COMPANY_NAME}.{Employee.DOMAIN_NAME}")
print(f"{emp1.welcome()}")
print(f"{emp2.welcome()}")
print(f"{emp3.welcome()}")

emp4 = Employee.get_employee("Swara-Gajjar-1000000")
print(emp4)

print(f"Total number of Employees {Employee.employee_count}")

date = datetime.date(2019, 12, 14)

print(Employee.is_workday(date))

emp5 = Developer.get_employee("Aaradhya-Gajjar-1000000-Python")
print(emp5)

emp6 = Manager.get_employee("Aarya-Gajjar-1000000")
print(emp6)

print(Manager.__repr__(emp6))

print(isinstance(emp6, Manager))
print(issubclass(Developer, Employee))

print(f"Sum: {emp1 + emp2}")

print(len(emp1))

print(emp1.full_name)

emp1.full_name = "Pradip Gajjar"