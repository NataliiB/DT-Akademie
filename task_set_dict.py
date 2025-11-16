# #*Beginner level*
# # 1. Створіть словник зі списками добрих справ на сьогодні і на завтра. Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.

# d = {"today": ["Help my boyfriend`s mother with documents", "Feed the dogs","Go to the gym"], "tomorrow": ["Feed the birds","Go to the library" ]}

# def print_list():
#     for i, item in enumerate(d[key], start=1):
#       print(f"{i}. {item}\n")

# for key in d.keys():
#   if d[key] == "today":
#     print("Today:\n")
#     print_list()
#   else:
#     print("Tomorrow:\n")
#     print_list()

# # 2. Припустимо, що у нас є словник, в якому ключі є ідентифікаторами, а значення – іменами користувачів. Напишіть програму, яка виводить вітальне повідомлення користувачу на основі його ідентифікатора. Якщо ідентифікатор відсутній у словнику, виводиться вітання для усіх користувачів.

# d = { 0: "to all",
#      134:"Aleks",
#      223:"Maks",
#      389:"Anna", 
#      432:"Milena", 
#      509:"Sara",}

# def say_hello(id = 0):
#   print(f"Hello, {d[id]}!")

# say_hello()
#  say_hello(389)

# # 3. Напишіть програму для сортування за зростанням (за алфавітом) словника за ключами. Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами фільмів.

# films = {"Avengers: Endgame" : 2019,
#      "Guardians of the Galaxy" : 2014,
#      "Iron Man" : 2008,
#      "Thor" : 2011,}

# def sort_films(films):
#     sorted_keys = sorted(list(films.keys()))
#     sorted_films = {}
#     for key,value in films.items():
#       for i in range(len(sorted_keys)):
#         if sorted_keys[ i - (len(sorted_keys))]== key:
#            sorted_films[key] = value
#     print(sorted_films)

# sort_films(films)

# # 4. Надрукуйте елементи словника, де ключі - це числа від '1' до 'n' (обидва числа включно), а значення - квадрати ключів. 'n' – ціле число, яке вводить користувач.

# n = int(input("Enter the number: "))
# d = {}
# if n > 0:
#   for i in range(1, n + 1):
#     d[i] = i**2
#     print(f"{i} : {d[i]}\n")
# else:
#     for i in range(1, n-1, -1):
#       d[i] = i**2
#       print(f"{i} : {d[i]}\n")

# 5. Створіть словник, в кому ключі – назви днів тижня, а значення - цілі числа, що позначають порядковий номер дня тижня від 0 до 6. Надрукуйте назву дня за введеним порядковим номером дня. Якщо введений номер виходить за межі, програма жодних повідомлень не друкує і не повідомляє про помилку.

# days_dict = {
#     "Monday": 0,
#     "Tuesday": 1,
#     "Wednesday": 2,
#     "Thursday": 3,
#     "Friday": 4,
#     "Saturday": 5,
#     "Sunday": 6
# }

# n = int(input("Enter the number of a day: "))
# if n in days_dict.values():
#     for key,value in days_dict.items():
#             if value == n:
#               print(f"{key}")

# # 6. Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів.

# s = input("Enter a string: ")
# d = {}
# quantity = 0
# list_from_s = [i for i in s ]
# for i in list_from_s:
#   quantity = list_from_s.count(i)
#   d[i] = quantity
# print(d)

# # 7. Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.

# s = input("Enter a string: ")

# letters = [i for i in s if i != " " and i.isalpha()]
# digits = [i for i in s if i != " " and i.isdigit()]
# d = {}
# d["letters"] = len(letters)
# d["digits"] = len(digits)

# print(f"LETTERS: {d["letters"]}\nDIGITS: {d["digits"]}")
# *Middle level*

# # 8. Напишіть програму для видалення дублікатів зі списку цілих чисел.

# l = [1, 2, 3, 4, 5, 6, 7, 89, 4, 5, 32, 7, 9]

# def make_unique(l):
#     s = set(l)
#     print(s)
# make_unique(l)

# # 9. Дано список словників. Кожен словники має 2 пари елементів: ключ 'name' і значення імені студента, ключ 'points' і значення - список балів з різних дисциплін (цілі двоцифрові числа). Надрукуйте найменші значення балів, отримані кожним студентом, в один рядок з пропуском.

# students = [
#     {"name": "Alice", "points": [85, 90, 78, 92]},
#     {"name": "Bob", "points": [76, 88, 95, 80]},
#     {"name": "Sara", "points": [90, 91, 85, 87]},
#     {"name": "Diana", "points": [82, 79, 88, 91]},
#     {"name": "Edward", "points": [94, 89, 90, 86]}
# ]
# for i in students:
#     print(f"{min(i["points"])} ",end="")

# # 10. Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в обох з них.

# l1 = [1, 2, 3, 176, 5, 5]
# l2 = [1, 4, 89, 89, 89]
# quantity = 0
# general_l = []

# for i in l1:
#     general_l += str(i)
# for i in general_l:
#     if general_l.count(i) == 1:
#       quantity += 1
# print(quantity)

# # 11. Дано три словники, в яких ключами є малі букви латинського алфавіту, а значеннями - цілі числа. Ключі у всіх словниках – різні, їх є по 3 в кожному словнику. Об’єднайте всі три словники в один і виведіть його вміст. Підказка. скористайтеся оператором **, що використовується для об’єднання довільної кількості словників.

# d1 = {'a': 5, 'b': 12, 'c': 7}
# d2 = {'d': 9, 'e': 3, 'f': 14}
# d3 = {'g': 6, 'h': 11, 'i': 8}

# general_d = {** d1, ** d2, ** d3}
# print(general_d)

# 12. Створіть словник, який відображає ідентифікатори акцій на біржі. Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. Надрукуйте ціни акцій та ідентифікатори у порядку зростання ціни.

# stocks = {
#     'ACME': 45.23,
#     'IBM': 205.55,
#     'AAPL': 612.78,
#     'HPQ': 37.2,
#     'FB': 10.75
# }

# l = sorted(stocks.values())
# for i in (l):
#    for key,value in stocks.items():
#       if i == value:
#          print(f"{value} {key}\n")

# # 13. В рядку записаний текст. Словом вважається послідовність непробільних символів, які йдуть підряд, слова розділені одним або більшим числом пропуском або символами кінця рядка. Для кожного слова з цього тексту підрахуйте, скільки разів воно зустрічалося в цьому тексті раніше.         

# s = "var list set tuple list tuple tuple dict var"
# l = s.split()
# for i in range(len(l)):
#    print(f"{(l[:i]).count(l[i])} ",end="")

# # *Hard level*

# # 14. Напишіть програму, яка зможе підрахувати слова у введеному рядку, розділені пропуском і вивести отриману статистику: для кожного унікального слова обчислити число його повторень (без урахування регістру), слова не повинні повторюватися, порядок слів довільний.

# s =  "a bb acD bb abc ac BCD a"
# l = s.split()
# d = {}
# for i,item in enumerate(l):
#     l[i] = l[i].lower()
#     d[item.lower()] = l.count(l[i])
# for key,value in d.items():
#     print(key, value)

# # 15. Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.

# l1 = [2, 5, 8, 11, 10, 9]
# l2 = [11, 3, 7, 6, 8, 5]
# general_l = list(set(l1) & set(l2))
# print(sorted(general_l))

# # 16. Напишіть програму, яка вміє шифрувати і розшифровувати використовуючи шифр підстановки. Програма приймає на вхід два рядки однакової довжини, у першому рядку записані символи початкового алфавіту, у другому рядку - символи кінцевого алфавіту (шифр підстановки), після чого йде рядок, який потрібно зашифрувати переданим шифром підстановки, і ще один рядок, який потрібно розшифрувати.

# s = "abcd"
# code = "1234"
# s_to_code = "ababcdcd"
# s_to_uncode = "44332211"

# code_dict = {}
# for i in range(len(s)):
#     code_dict[s[i]] = code[i]
# def code_uncode(s_to_code,s_to_uncode):
#     coded_s = ""
#     uncoded_s = ""
#     for i in range(len(s_to_code)):
#          for key,value in code_dict.items():
#             if s_to_code[i] == key:
#                coded_s += value
#     for u_i in range(len(s_to_uncode)):
#          for key,value in code_dict.items():
#              if s_to_uncode[u_i] == value:
#                 uncoded_s += key
#     return coded_s , uncoded_s
# print(code_uncode(s_to_code,s_to_uncode))                