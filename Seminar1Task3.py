#В некоторой школе решили набрать три новых 
#математических класса и оборудовать кабинеты для 
#них новыми партами. За каждой партой может сидеть 
#два учащихся. Известно количество учащихся в 
#каждом из трех классов. Выведите наименьшее 
#число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32

a = int(input("введите количество учащихся первого кабинета:"))
b = int(input("введите количество учащихся второго кабинета:"))
c = int(input("введите количество учащихся третьего кабинета:"))
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)


