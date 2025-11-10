# *Beginner level*
# 1. Напишіть функцію, яка отримує ім’я і друкує вітальне повідомлення `Hello, <name>`.

def say_hello(name):
    print(f"Hello, {name}")

# 2. Напишіть функцію, яка отримує рядок і ціле число `n` та повертає `n` копій заданого рядка.

def return_copies(s, num):
    return s * num

#3. Напишіть функцію для обчислення суми двох цілих чисел.

def countSum(num1, num2):
    return num1 + num2

# 4. Напишіть функцію для отримання рядка з перших `n` символів іншого рядка. Якщо довжина рядка менше `n`, поверніть початковий рядок.

def make_str(s, n):
    if len(s) <= n:
        return s
    else:
        return s[:n]
    
# 5. Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції `max()`.

def return_max(num1, num2, num3):
    return max(num1,num2,num3)
    
# 6. Напишіть функцію для створення позначок тегів `HTML` навколо введених рядків. Функція отримує назву тега `HTML` і рядок, який необхідно помістити у відповідні теги.

def makeTag(s, tag):
    return f"<{tag}>{s}</{tag}>"

# 7. Напишіть функцію, яка повертає назву пори року для введеного значення номера місяця.

def returnSeason(m):
    if m != 0:
      if m in [3,4,5]:
        print("Spring")
      elif m in [6,7,8]:
        print("Summer")
      elif m in [9,10,11]:
         print("Autumn")
      else:
         print("Winter")

# 8. Напишіть функцію для створення гістограми (наприклад, у вигляді *) із заданого списку цілих чисел як у вихідних даних. Формат введення списку чисел як у вхідних даних.

def make_gist():
    s = input("Enter a list of numbers: ")
    l = [i for i in s if i.isdigit()]
    for item in l:
        print(int(item) * "*", end="")
        print(end="\n")

#*Middle level*

# 9. Напишіть функцію для визначення, чи рік високосний чи ні.

def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
      print("The year is leap")
    else:
       print("The year isn't leap")

# 10. Напишіть функцію, яка отримує значення середньомісячної кількості опадів по місяцях (в мм) і повертає загальний обсяг опадів протягом року, середньорічну кількість опадів, назви місяців та значення з найвищим та найменшим числом опадів протягом року.

d = {"January": 15, "February": 22, "March": 134, "April": 125, "May":78, "June":56, "July":14, "August":12, "September":124, "October":45, "November":127, "December":56 }
def count_index(d):
    sum = 0
    for key in d:
        sum += d[key]
        if d[key] == max(d.values()):
            max_month = key
        elif d[key] == min(d.values()):
            min_month = key
    average = sum/12
    return sum, average, max_month, d[max_month], min_month, d[min_month]

# 11. На стадіоні є три категорії місць для сидіння: місця класу A коштують a грошових одиниць, місця класу B коштують b грошових одиниць, а місця класу C - c грошових одиниць. Напишіть першу функцію, яка запитує скільки продано квитків на кожний клас місць, і другу функцію, яка відображає суму отриманого доходу від продажу квитків на кожен клас окремо і загалом. Формати введення і виведення такі, як у вхідних і вихідних даних.

def how_many():
    places_a = int(input("How many first class tickets were sold?"))
    places_b = int(input("How many second class tickets were sold?"))
    places_c = int(input("How many third class tickets were sold?"))
    return places_a, places_b, places_c

def count_income(places_a, places_b, places_c):
    price_a = 20.5
    price_b = 15.75
    price_c = 10.55
    income = {"A" : price_a * places_a,
              "B" : price_b * places_b,
              "C" : price_c * places_c,}
    total_income = 0
    for key in income:
        total_income += income[key]
    return income, total_income
places_a, places_b, places_c = how_many()

# 12. Напишіть функцію, яка перевіряє, чи рядок є паліндром чи ні. Регістр літер, пропуски і знаки пунктуації не враховувати.  
# *Паліндром - це слово, фраза або послідовність, яка читається так само як зліва направо, так і справа наліво.

def is_palindrom(s):
  list_of_s1 = [i for i in s.lower() if i != " " and i.isalpha()]
  list_of_s2 = [i for i in s.lower() if i != " " and i.isalpha()]
  list_of_s1.reverse()
  return "".join(list_of_s2) == "".join(list_of_s1)

# *Hard level*
# 13. Напишіть рекурсивну функцію, яка обчислює суму цілих чисел `a` і `b`. З арифметичних операцій використовується тільки додавання одиниці і віднімання одиниці.

def make_sum(a, b):
    if b > 0:
       return make_sum(a + 1, b - 1)
    elif b < 0:
       return make_sum(a - 1, b + 1)
    else:
       return a

# 14. Дано послідовність цілих чисел, що закінчується числом 0. Напишіть рекурсивну функцію, яка друкує цю послідовність в зворотному порядку. При розв’язуванні цього завдання не можна користуватися списками.

t = (1, 6, 8, 9, 0)
def reverse_nums(t):
    if len(t) == 0:
        return
    reverse_nums(t[1:]) 
    print(t[0], end=' ')