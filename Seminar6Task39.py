#Задача 39
#Даны два массива чисел. Требуется вывести те элементы
#первого массива (в том порядке, в каком они идут в первом
#массиве), которых нет во втором массиве. Пользователь вводит 
#число N - количество элементов в первом массиве, затем N
#чисел - элементы массива. Затем число M - количество
#элементов во втором массиве. Затем элементы второго массива

def find_missing_elements(arr1, arr2):
    missing_elements = [x for x in arr1 if x not in arr2]
    return missing_elements

N = int(input("Введите количество элементов в первом массиве: "))
array1 = [int(input()) for _ in range(N)]

M = int(input("Введите количество элементов во втором массиве: "))
array2 = [int(input()) for _ in range(M)]

result = find_missing_elements(array1, array2)
for element in result:
    print(element)
