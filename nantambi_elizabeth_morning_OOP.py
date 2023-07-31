# class Car:
#     def __init__(self,name,mileage,model,year):
#         self.name = name
#         self.mileage = mileage
#         self.model = model
#         self.year = year

# my_cae= Car("corola",0,"Toyota",2023) 
# print(my_cae.name)
# print(my_cae.mileage)
    
# #example: student class

# class Student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.course)
        
# my_student = Student("Liz",20,"BSE")
# my_student.display() 

# # example: circle class
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius
#     def display(self):
#         print(self.radius)
#         print(self.area())
#         print(self.perimeter())
# circle_1= Circle(12)      
# circle_1.display()  

# # Exercise 
# # Rectangle class
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return 2*(self.length+self.width)


# # Employees' bonuses class
# class EmployeesBonuses:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
        
#     def display(self):
#         print("name"+" " + self.name)
#         print("salary"+" " + str(self.salary))
        
#     def bonus_calculation(self):
#         print ("bonus"+" " + str(self.salary*(15/100)))
      

# Employee1= EmployeesBonuses("Liz", 150000)
# Employee1.display()
# Employee1.bonus_calculation()

# # Encapsulation
# # Example with a bank account

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print(self.balance)

# Convert degrees celcius to farenheit


class Temp:
    def __init__(self,temp):
        self._temp = temp
    def convert(self):
        x= print((self._temp * 9/5) + 32)
        # return x
        # print(x)
Degrees= Temp(37)
Degrees.convert()



#assignment on encapsulation

class Employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary
    def increment_amount(self,amount):
         self._salary += amount
         print(self._salary)
    def display(self):
        print("Name"+" " + self._name)
        print("New salary"+" " + str(self._salary))
    
Employee1= Employee("Liz",500000)
Employee1.increment_amount(600000)
Employee1.display()
    