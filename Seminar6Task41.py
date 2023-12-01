#Задача41
#Дан массив, состоящий из целых чисел. Напишите
#программу, которая в данном массиве определит
#количество элементов, у которых два соседних и, при
#этом, оба соседних элемента меньше данного. Сначала
#вводится число N — количество элементов в массиве 
#Далее записаны N чисел — элементы массива. Массив
#состоит из целых чисел.

def count_special_elements(arr):
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1
    return count

input_str = input("Введите количество элементов в массиве, а затем сами элементы: ")
values = list(map(int, input_str.split()))
N = values[0]
array = values[1:]

result = count_special_elements(array)
print(result)