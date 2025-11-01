name = input("Введи своє ім'я: ")
age = input("Введи свій вік: ")
print(f"Привіт {name}, тобі {age}!")



age = int(input("Введи свій вік: "))

if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")



import random

number = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. Спробуй вгадати!")

for i in range(attempts):
    guess = int(input("Введи число: "))
    if guess == number:
        print("Вітаю! Ти вгадав!")
        break
    elif guess > number:
        print("Менше!")
    else:
        print("Більше!")
else:
    print(f"На жаль, ти не вгадав. Загадане число було {number}.")




start = int(input("Введи початкове число: "))
end = int(input("Введи кінцеве число: "))

for i in range(start, end + 1):
    print(i)




n = int(input("Введи число n: "))

for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")



n = int(input("Введи число n: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факторіал числа {n} = {factorial}")




score = int(input("Введи кількість балів: "))

if 0 <= score <= 49:
    print("Незадовільно")
elif 50 <= score <= 69:
    print("Задовільно")
elif 70 <= score <= 89:
    print("Добре")
elif 90 <= score <= 100:
    print("Відмінно")
else:
    print("Некоректне значення балів!")




a = float(input("Введи перше число: "))
b = float(input("Введи друге число: "))
operation = input("Введи дію (+, -, *, /): ")

if operation == "+":
    print("Результат:", a + b)
elif operation == "-":
    print("Результат:", a - b)
elif operation == "*":
    print("Результат:", a * b)
elif operation == "/":
    if b == 0:
        print("Ділення на нуль!")
    else:
        print("Результат:", a / b)
else:
    print("Невідома операція!")
