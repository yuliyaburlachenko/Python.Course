#Задача №31

#Последовательностью Фибоначчи называется
#последовательность чисел a0, a1, ..., an, ..., где a0= 0, a1= 1, ak= ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи
def fibonacci(n):
    if n <= 0:
        return "Введите целое положительное число"
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


result = fibonacci(10)
print(result)  