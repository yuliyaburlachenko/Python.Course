#Задача №19. 
#Дана последовательность из N целых чисел и число 
#K. Необходимо сдвинуть всю последовательность 
#(сдвиг - циклический) на K элементов вправо, K – 
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]
#Примечание: Пользователь может вводить значения 
#Cписка или список задан изначально.

def cyclically_shift(sequence, k):
    k = k % len(sequence)  # Получаем остаток от деления, чтобы учесть цикличность
    
    # Формируем сдвинутую последовательность и выводим результат
    shifted_sequence = sequence[-k:] + sequence[:-k]
    return shifted_sequence

sequence = [1, 2, 3, 4, 5]
k = 3
result = cyclically_shift(sequence, k)
print(result)
