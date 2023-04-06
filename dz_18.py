# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
import math 
n = int(input("Введите N  "))
list = [random.randint(1, n+1) for i in range(n)]
x = int(input("Введите Х  "))
list_2 = []

print(list)
for i in list:
    list_2.append(abs(i-x))
min_ind = list_2.index(min(list_2))
print("Самое ближайшее минимальное число: ", list[min_ind])


    