#Задача 32
#Определить индексы элементов массива (списка),
#значения которых принадлежат заданному диапазону (т.е. не
#меньше заданного минимума и не больше заданногомаксимума

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# Введите ваше решение ниже
def find_indexes_in_range(arr, min_num, max_num):
    indexes = []
    for i in range(len(arr)):
        if min_num <= arr[i] <= max_num:
            indexes.append(i)
    return indexes


result = find_indexes_in_range(list_1, min_number, max_number)
for index in result:
    print(index)