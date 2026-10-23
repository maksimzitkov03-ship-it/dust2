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
