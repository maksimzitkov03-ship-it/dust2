import random


name = input("Введіть ваше ім'я: ")
age_1 = input("Введіть ваш вік: ")
print(f"Привіт {name}, тобі {age_1}!")



age_2 = int(input("\n[Вхід] Введіть ваш вік: "))
if age_2 > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")



target_number = random.randint(1, 10)
attempts = 3
print("\n[Гра] Комп'ютер загадав число від 1 до 10. У вас є 3 спроби!")

for attempt in range(1, attempts + 1):
    user_guess = int(input(f"Спроба {attempt}. Введіть число: "))
    if user_guess == target_number:
        print("Вітаємо! Ви вгадали число!")
        break
    elif user_guess > target_number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Спроби закінчилися. Було загадано {target_number}.")



print("\n[Діапазон]")
start = int(input("Введіть число З: "))
end = int(input("Введіть число ПО: "))
for i in range(start, end + 1):
    print(i, end=" ")
print()



print("\n[Парні числа навпаки]")
n_even = int(input("Введіть число n: "))
start_even = n_even if n_even % 2 == 0 else n_even - 1
for i in range(start_even, 0, -2):
    print(i, end=" ")
print()



print("\n[Факторіал]")
n_fact = int(input("Введіть число n для факторіалу: "))
factorial = 1
if n_fact < 0:
    print("Факторіал від'ємного числа не існує.")
else:
    for i in range(1, n_fact + 1):
        factorial *= i
    print(f"Факторіал числа {n_fact}! = {factorial}")



print("\n[Оцінка студента]")
score = int(input("Введіть кількість балів (0-100): "))
if 0 <= score <= 49:
    print("Незадовільно")
elif 50 <= score <= 69:
    print("Задовільно")
elif 70 <= score <= 89:
    print("Добре")
elif 90 <= score <= 100:
    print("Відмінно")
else:
    print("Некоректна кількість балів!")



print("\n[Калькулятор]")
a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
operation = input("Введіть математичну дію (+, -, *, /): ")

if operation == '+':
    print(f"Результат: {a + b}")
elif operation == '-':
    print(f"Результат: {a - b}")
elif operation == '*':
    print(f"Результат: {a * b}")
elif operation == '/':
    if b == 0:
        print("Ділення на нуль")
    else:
        print(f"Результат: {a / b}")
else:
    print("Невідома операція!")