#Задача №29.
#Ваня и Петя поспорили, кто быстрее решит 
#следующую задачу: “Задана последовательность
#неотрицательных целых чисел. Требуется определить
#значение наибольшего элемента
#последовательности, которая завершается первым
#встретившимся нулем (число 0 не входит в
#последовательность)”. Однако 2 друга оказались не 
#такими смышлеными. Никто из ребят не смог до 
#конца сделать это задание. Они решили так: у кого 
#будет меньше ошибок в коде, тот и выиграл спор. За 
#помощью товарищи обратились к Вам, студентам.
#Примечание: Программные коды на следующих 
#слайдах

#Ваня: 
#def find_max_before_zero(sequence):
#    max_num = 0
#    for num in sequence:
#        if num > max_num:
#            max_num = num
#    return max_num



#Петя: 
#def find_max_before_zero(sequence):
#    max_num = sequence[0]
#    for num in sequence:
#        if num > max_num:
#          max_num = num
#        elif num == 0:
#            break
#    return max_num

def find_max_before_zero(sequence):
    max_num = 0
    for num in sequence:
        if num > max_num:
            max_num = num
        if num == 0:
            break
    return max_num




