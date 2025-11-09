#*Beginner level*

# 1. Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення `Password accepted.`. У іншому випадку повідомлення буде `Sorry, that is the wrong password.`.

input_password = int(input("Enter your password: "))
password = 1234
if input_password == password:
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password") 

# 2. Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.

name1 = input("Введіть перше ім'я: ")
name2 = input("Введіть друге ім'я: ")

if name1 > name2:
    print(name2, name1)
else:
    print(name1, name2)

# 3. Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або `1` або `2` або `3`, то виводиться повідомлення - назва числа, відповідно, `One`, `Two`, `Three`. В усіх інших випадках виводиться слово `Unknown`.

n = input("Enter a number: ")

if n == "1":
    print("One")
elif n == "2":
    print("Two")
elif n == "3":
    print("Three")
else:
    print("Unknown")
    
# 4. Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.

letter1 = input("Enter a first letter: ").lower()
letter2 = input("Enter a second letter: ").lower()

if ord(letter1) > ord(letter2):
    print(f"Letter {letter2} is before {letter1} ")
elif ord(letter1) < ord(letter2):
    print(f"Letter {letter1} is before {letter2} ")
elif ord(letter1) == ord(letter2):
    print(f"Letter {letter1} is on the same place as {letter2} ")

# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення `A cold, isn’t it?`. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде `Cool.`, у інших випадках `Nice weather we’re having.`.

t = int(input("Enter the value of temperature: "))

if t <= 0:
     print("A cold, isn’t it?")
elif t > 0 and t < 10:
     print("Cool.")
else:
     print("Nice weather we’re having.")

#*Middle level*

# 6. Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.

n = int(input("Enter the number of sides: "))

if n == 3:
     print("Triangle")
elif n == 4:
     print("Quadrangle")
elif n == 5:
     print("Pentagon")
elif n == 6:
     print("Hexagon")
else:
     print("Enter the number of sides between 3 and 6: ")

# 7. Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.

n = int(input("Enter a number: "))

if n == 0:
  print("The number is green")
elif n >= 0 and n <= 36:
    if (n % 2 == 0) and ((0 < n or n >= 10) or (19 < n or n >= 28)):
       print("The number is black")
    else:
          print("The number is red")
else:
  print("Please enter a number between 0 and 36")

# 8. Дано дві точки: `A(x1, y1)` і `B(x2, y2)`. Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.

x1 = 1
y1 = 2
x2 = 3
y2 = 2
dist1 = (x1 ** 2 + y1 ** 2) ** 0.5
dist2 = (x2 ** 2 + y2 ** 2) ** 0.5
if (dist1 > dist2):
  print("A")
elif (dist1 < dist2):
  print("B")
else:
  print("The distance is the same")
# 9. Вводяться координати `(x, y)` точки `A` і радіус кола (`r`). Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.
x = int(input("Enter coordinate x: "))
y = int(input("Enter coordinate y: "))
r = int(input("Enter radius: "))
dist = (x ** 2 + y ** 2) ** 0.5

if dist == r:
    print("The point belongs to the circle")
else:
    print("The point is outside the circle")

# 10. Дано натуральное число. Визначити, чи закінчується число парною цифрою. Якщо так, то виведе `True`, інакше `False`.

n = 23
print(int(str(n)[-1]) % 2 == 0)

# 11. Напишіть програму для знаходження коренів квадратного рівняння `a*x² + b*x + c = 0`. Користувач вводить значення коефіцієнтів `a`, `b`, `c`. У вхідних даних наведено три пари вхідних значень коефіцієнтів, а у вихідних даних - відповідні повідомлення про кількість коренів або їх відсутність.
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b ** 2 - 4 * a * c

if d > 0:
  x1 = (-b + d ** 0.5) / (2 * a)
  x2 = (-b - d ** 0.5) / (2 * a)
  print(f"{x1:.2f} and {x2:.2f}")
elif d == 0:
  x = -b / (2 * a)
  print(f"{x:.2f}")
else:
  print("No roots.")

# 12. Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем) парне або непарне. Якщо так, то виведе `True`, інакше `False`.

n = int(input("Please enter an integer: "))

print(n % 2 == 0)

# 13. Відомі рік і номер місяця народження людини, а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.

year_of_birth = 1987
month_of_birth = 2
current_year = 2026
current_month = 1

if current_month < month_of_birth:
    print(current_year - year_of_birth - 1)
else:
    print(current_year - year_of_birth)

# *Hard level*

# 14. Дано чотирицифрове число. Замінити усі парні цифри числа на символ `*` і вивести число.

n = 2227
result  = ""
for i in str(n):
    if (int(i)) % 2 == 0:
        result += "*"
    else:
        result += i
print(result)