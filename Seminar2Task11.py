#Задача 11
#Дано натуральное число A > 1. Определите, каким по 
#счету числом Фибоначчи оно является, то есть 
#выведите такое число n, что φ(n)=A. Если А не 
#является числом Фибоначчи, выведите число -1.

n = 4
summ = 0
f_1 =1
f_2 =1
num = 3
while summ < n:
    summ = f_1 + f_2
    f_1 = f_2
    f_2 = summ
    num += 1
    print (f'{num}' if summ == n else' -1')