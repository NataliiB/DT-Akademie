# 1. Створіть список на основі введеної послідовності цілих чисел і надрукуйте другу половину списку. Якщо кількість не парна, то вивести більшу кількість.

s = input("Please enter a consistency of numbers: ")
def print_half(s):
    list_from_s = s.strip().split()
    if len(list_from_s) % 2 == 1:
        print(list_from_s[(round(len(list_from_s)/2)-1):])
    else:
        print(list_from_s[(round(len(list_from_s)/2)):])  
print_half(s)

# 2. Створіть список на основі введеної послідовності цілих чисел і надрукуйте його елементи таким чином: два останні елементи переміщені з кінця в початок списку без зміни їх початкового порядку.

s = input("Please enter a consistency of numbers: ")
list_from_s = s.strip().split()
new_list = (list_from_s[len(list_from_s) - 2:len(list_from_s)]) + ( list_from_s[0:len(list_from_s) - 2])
print(new_list)

# 3. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в рядку через пропуск.

s = input("Please enter languages: ")
def print_sorted(s):
    list_from_s = s.strip().split()
    print(' '.join(sorted(list_from_s)))
print_sorted(s)

# 4. Виведіть елементи даного списку в зворотному порядку, не змінюючи сам список.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i, item in enumerate(range(len(l)), start=1):
    print(l[(len(l)-i)], end=" ")
    
# 5. Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i, item in enumerate(l):
    if i % 2 == 0:
      print(item)