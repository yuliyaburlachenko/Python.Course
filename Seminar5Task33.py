#Задача №33. 
#Хакер Василий получил доступ к классному журналу и
#хочет заменить все свои минимальные оценки на
#максимальные. Напишите программу, которая
#заменяет оценки Василия, но наоборот: все
#максимальные – на минимальные
def replace_grades(grades):
    min_grade = min(grades)
    max_grade = max(grades)
    replaced_grades = [max_grade if grade == min_grade else min_grade if grade == max_grade else grade for grade in grades]
    return replaced_grades

grades = [4, 7, 5, 3, 8, 2, 9]
new_grades = replace_grades(grades)
print(new_grades)  