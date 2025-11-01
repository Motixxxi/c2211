#3 РОБОТА З КІЛЬКОМА КЛАСАМИ.

#Зв'язок класів - це взаємодія декількох класів одночасно

# class Human:
#     def __init__(self, name="Human", age=10):
#         self.name=name
#         self.age=age
#
# class Avto:
#     def __init__(self,brand):
#         self.brand=brand
#         self.passengers = []
#     def AddPassengers(self,human):
#         self.passengers.append(human)
#     def NamePassengers(self):
#         if self.passengers!=[]:
#             print(f"Names of {self.brand} passengers: ")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
#
# nick=Human("Nick")
# kate=Human("Kate")
# car= Avto("Audi")
# car.AddPassengers(nick)
# car.AddPassengers(kate)
# car.NamePassengers()

# Створити клас студент з параметрами ім'я, вік.
# Створити клас ГрупаС2211 в якому буде метод який дозволить додати студента
# до групи і метод який дозволить вивести всіх студентів
# Зробити зв'язок між класами

# 4.  Успадкування класів. Метод super.

#Успадкування - передача властивостей з батьківського класу дочірнім класам
#  Human -> Student     Human->Worker
# class Human:
#     height=170
#     age = 10
# class Student(Human):
#     age=12
# class Worker(Human):
#     age=25
#
# student=Student()
# worker= Worker()
# print(student.height)
# print(worker.height)


class Grandparent:
    height = 170
    name = "Jack"
    age = 60

class Parent(Grandparent):
    age = 40

# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.name)
#         print(self.age)
#     def __str__(self):
#         return f"{self.height}{self.name}{self.age}"
#
# nick = Child()
# print(nick)


class Class1:
    var = 20
    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)



hello_world = Class2()