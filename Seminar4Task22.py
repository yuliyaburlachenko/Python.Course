#Задача 22:
#Даны два неупорядоченных набора целых чисел (может быть, с
#повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы множеств.


var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

from collections import Counter

n, m = map(int, var1.split())
set1 = set(map(int, var2.split()))
set2 = set(map(int, var3.split()))

common_elements = set1 & set2
result = sorted(common_elements)

print(*result)