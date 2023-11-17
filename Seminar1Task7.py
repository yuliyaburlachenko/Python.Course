#Задача №7. 
#Дано натуральное число. Требуется определить, 
#является ли год с данным номером високосным. Если 
#год является високосным, то выведите YES, иначе 
#выведите NO. Напомним, что в соответствии с 
#григорианским календарем, год является 
#високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
#Input: 2016
#Output: YES
years = int(input("Какой сегодня год:"))
if (years % 4 == 0) and (years % 100 != 0) or (years % 400 == 0):
    print("YES")
else:
    print("NO")
    
