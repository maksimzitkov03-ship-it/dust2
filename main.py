import random


name = input("Введіть ваше ім'я: ")
age_1 = input("Введіть ваш вік: ")
print(f"Привіт {name}, тобі {age_1}!")


age_2 = int(input("\n[Вхід] Введіть ваш вік: "))
if age_2 > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")
