# Homework

#> **Задача 1. Середнє трьох чисел**  
# Користувач вводить три числа. Обчисли середнє арифметичне.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
print(f"Arithmetic mean - {(num1 + num2 + num3) / 3}")
# > **Задача 2. Остача від ділення**  
# Користувач вводить два числа. Знайди остачу від ділення першого на друге.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Remainder from division - {num1 % num2}")

# > **Задача 3. Подвоєне число**  
# Користувач вводить число. Виведи подвоєне значення цього числа.

num = float(input("Enter a number: "))
print(f"Double meaning - {2 * num}")

# > **Задача 4. Конвертація хвилин у секунди**  
# Користувач вводить кількість хвилин. Обчисли, скільки це буде секунд.

num = int(input("Enter a number of minutes: "))
print(f"In seconds - {num * 60}")

# > **Задача 5. Кількість яблук на кожного**  
# Є n яблук і k учнів. Скільки яблук отримає кожен учень, якщо ділити порівну, і скільки залишиться?

n = 15
k = 4
print(f"Every gets {n // k} apples, remainder is {n % k}")

# > **Задача 6. Остання цифра числа**  

# Користувач вводить число. Виведи його останню цифру.

input_of_number = (input("Enter a number of minutes: "))
print(input_of_number[-1])

# > **Задача 7`*`. Обмін змінних**  
# Користувач вводить два числа. Після цього потрібно “поміняти” їх місцями і вивести результат.> 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1, num2 = num2, num1
print(f"The first number:{num1}.The second number:{num2}.")