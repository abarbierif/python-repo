class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount=0):
        self.salary += amount

    def anual_salary(self):
        return round(12*self.salary,4)

if __name__ == '__main__':
    emp = Employee(input('Employee name: '), input('Employee position: '), float(input('Employee salary = ')))
    emp.give_raise(float(input('rise = ')))
    print('new salary:', emp.salary)
    print(f"anual salary = {emp.anual_salary()}")
