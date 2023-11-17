#Задача 9

#По данному целому неотрицательному n вычислите 
#значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
#чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
#Input: 5
#Output: 120 

def VerificationInt(mes):
    while True:
        try:
            numer = int(input(mes))       
        except ValueError:
            print("Вы ввели не число. Попробуйте снова!")
            continue
        else:
            return numer

n = VerificationInt("Введите число: ")
i = 2
res = 1

while (i <= n):
    res *= i
    i += 1

print(f"{n}! = {res}")

    