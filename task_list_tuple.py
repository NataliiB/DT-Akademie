# 1. Створіть список на основі введеної послідовності цілих чисел і надрукуйте другу половину списку. Якщо кількість не парна, то вивести більшу кількість.

s = input("Please enter a consistency of numbers: ")
list_of_s = [i for i in s if i.isdigit()]

for i in range(len(list_of_s)):
    def print_num(i):
         if i >= len(list_of_s):
             return
         elif i >= round(len(list_of_s)/2):
            print (list_of_s[i])
    print_num(i)

# 2. Створіть список на основі введеної послідовності цілих чисел і надрукуйте його елементи таким чином: два останні елементи переміщені з кінця в початок списку без зміни їх початкового порядку.

s = input("Please enter a consistency of numbers: ")
list_of_s = [i for i in s if i.isdigit()]
new_list = (list_of_s[len(list_of_s) - 2:len(list_of_s)]) + ( list_of_s[0:len(list_of_s) - 2])

# 3. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в рядку через пропуск.

s = input("Please enter languages: ")
list_of_s = s.strip().split()
is_sorted = 0
for i in range(len(list_of_s)-1):
  if list_of_s[i] <= list_of_s[i + 1]:
    is_sorted += 1
    if is_sorted < len(list_of_s)-1:
     list_of_s.sort()
print(" ".join(list_of_s))

# 4. Виведіть елементи даного списку в зворотному порядку, не змінюючи сам список.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i, item in enumerate(range(len(l)), start=1):
    print(l[(len(l)-i)], end=" ")
    
# 5. Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i, item in enumerate(l):
    if i % 2 == 0:
      print(item)