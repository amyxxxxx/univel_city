# class DjangoStudent():
#     def __init__(self, name, laptop):
#         self.name = name
#         self.computer = laptop

# mystudent = DjangoStudent("Ejiro", "Macbook")
# print(mystudent.name)
# print(mystudent.computer)

# class  car():        
#     def __init__(self, brand,  price):                 
#         self.brand = brand                 
#         self.price = price

# mystudent = car("Lexus", "$100000")
# print(mystudent.brand)
# print(mystudent.price)

# class BankApp():
#     def __init__(self, name, balance):
#         if not isinstance(balance, (int, float)):
#             raise TypeError(f'Expected int or float but got {type(balance)}')
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#         return self.balance

#     def name_tolower(self):
#         self.name = self.name.lower()
#         return self.name

# customer1 = BankApp('Tunde', 105.44)
# print(customer1.name_tolower())
# print(customer1.deposit(1000))

# class vehicle():
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage    

#     def acceleration(self, time):
#         a = self.mileage*2/time**2
#         return a


# car1 = vehicle(15, 250)
# a = car1.acceleration(10)
# print(a)
# print(car1.max_speed)
# print(car1.mileage)


class Employee():
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    @property
    def bonus(self):
        return (self.salary * 0.1) + self.salary

    def report(self):
        return f"Hi {self.name}. Your take home salary is {self.bonus}"

a = Employee('Tosin', 10, 'Q/A')
print(a.report())

    
class Supervisors(Employee):
    def __init__(self, name, salary, designation, branch):
        self.branch = branch
        super().__init__(name, salary, designation)

    # def bonus(self):
    #     return self.salary + (self.salary * 0.17)

b = Supervisors('Tunde', 10000, 'Accountant', 'Sabo')
print(b.bonus)
