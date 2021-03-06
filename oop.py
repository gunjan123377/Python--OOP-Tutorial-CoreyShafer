# Python Pbject-Oriented Programming
#Git demo is happening.
#I am learning branching.

class Employee(object):

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


# emp_1 = Employee('Corey', 'Shafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# emp_1.first = 'Sue'
# # because of the @property, the email method don't need pharentesis
# print(emp_1.email)
# print(emp_1.fullname)

# emp_1.fullname = 'Jim Parson'
# print(emp_1.email)
# print(emp_1.fullname)

# del emp_1.fullname
# print(emp_1.fullname)


# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# # __add__ magc method
# print(emp_1 + emp_2)

# print(len(emp_1))


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# dev_1 = Developer('Corey', 'Shafer', 50000, 'Python')
# dev_2 = Developer('Test', 'User', 60000, 'Java')
#
# mgr_1 = Manager('Sue', 'Smith', 98000, [dev_1])


# CHECK BUILT-IN FUNCTIONS
# print(isinstance(mgr_1, Employee))
# # --> True
# print(isinstance(mgr_1, Manager))
# # --> True
# print(isinstance(mgr_1, Developer))
# # --> False
#
# print(issubclass(Developer, Employee))
# # --> True
# print(issubclass(Manager, Employee))
# # --> True
# print(issubclass(Manager, Developer))
# # --> False


# IHERITANCE

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()


# print(dev_1.email)
# print(dev_1.prog_lang)


# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(help(Developer))




# import datetime
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))


# emp_str_1 = 'John-Doe-70000'
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)


# Employee.set_raise_amt(1.05)
# emp_1.set_raise_amt(1.05)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)


# print(emp_1.__dict__)
# print(Employee.__dict__)


# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Employee.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# print(Employee.num_of_emps)
