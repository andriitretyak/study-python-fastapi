import os
os.system('cls' if os.name == 'nt' else 'clear')

### Умовні конструкції:
#1.Перевірка паролю
# Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає з ним. 
# Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".
print('Завдання_1')
password = 'password123'
user_entry1 = input('Введіть пароль: ')

if user_entry1 == password:
    print('Ви успішно увійшли в систему')
else:
    print('Невірний пароль')

#2. Визначення днів тижня
# Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. 
# Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.
print()
print('Завдання_2')

day_number = int(input('Введіть номер дня тижня (1-7): '))

if day_number == 1:
    print('Понеділок')
elif day_number == 2:
    print('Вівторок')
elif day_number == 3:
    print('Середа')
elif day_number == 4:
    print('Четвер')
elif day_number == 5:
    print("П'ятниця")
elif day_number == 6:
    print('Субота')
elif day_number == 7:
    print('Неділя')
else:
    print('Помилка: Невірний номер дня. Введіть число від 1 до 7.')

### Цикли:
# 1.Таблиця множення:
# Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
print()
print('Завдання_3')

number = 7

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

#2. Сума чисел:
# Завдання: Визначте список чисел і обчисліть їх суму.
print()
print('Завдання_4')

numbers = [35, 45, 534, 346, 64, 6]
sum_of_numbers = 0

for num in numbers:
    sum_of_numbers += num
print('Сума чисел:' , sum_of_numbers)

# 3.Факторіал числа:
# Завдання: Обчисліть факторіал заданого числа.
print()
print('Завдання_5')

factorial_number = 7
factorial = 1
for i in range(1, factorial_number + 1):
    factorial *= i
print(f"Факторіал числа {factorial_number}:", factorial)


# 4. Парні числа:
# Завдання: Виведіть всі парні числа від 1 до 50.
print()
print('Завдання_6')

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()
# 5.Пошук простих чисел:
# Завдання: Знайдіть всі прості числа в заданому діапазоні.
# Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання без використання `input`. 
print()
print('Завдання_7')

start = 10
end = 50

for num in range(start, end + 1):
    is_prime = True
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
