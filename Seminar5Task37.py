#Задача №37.
#Дано натуральное число N и
#последовательность из N элементов.
#Требуется вывести эту последовательность в
#обратном порядке.
#Примечание. В программе запрещается
#объявлять массивы и использовать циклы
#(даже для ввода и вывода).

def reverse_print_sequence(sequence, n):
    if n > 0:
        print(sequence[n - 1], end=" ")
        reverse_print_sequence(sequence, n - 1)

# Пример использования функции
sequence = [1, 2, 3, 4, 5]
reverse_print_sequence(sequence, len(sequence))
