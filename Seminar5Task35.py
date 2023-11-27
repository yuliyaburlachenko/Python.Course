#Задача №35. 
#Напишите функцию, которая принимает одно число и
#проверяет, является ли оно простым
#Напоминание: Простое число - это число, которое
#имеет 2 делителя: 1 и n(само число)
def is_prime_number(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):  # Проверяем делители до корня из числа
            if n % i == 0:
                return False
        return True


result = is_prime_number(17)
print(result)  