#Задача №38
#Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
#Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
#1. Программа должна выводить данные 
#2. Программа должна сохранять данные в текстовом файле 
#3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
#4. Использование функций. Ваша программа не должна быть линейной """ 

from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def init(self, txt):
        self.txt = txt

class NameError(Exception):
    def init(self, txt):
        self.txt = txt

def get_info():
    is_valid_name = False
    while not is_valid_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else: 
                is_valid_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_name = False
    while not is_valid_name:
        try:
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Не валидная фамилия")
            else: 
                is_valid_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else: 
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]

def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as data:
        f_reader = DictReader(data) 
        return list(f_reader)
    
def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже существует")
            return
        
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(res)

def delete_row(file_name, index):
    list = read_file(file_name)
    del list[index]
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(list)

def copy_row(file_name, new_file, index):
    if not exists(new_file):
        create_file(new_file)
    list = read_file(file_name)
    write_file(new_file, [list[index]["Имя"], list[index]["Фамилия"], list[index]["Телефон"]])

file_name = "phone.txt"
def main():
    while True:
        command = input("Введите комманду: \n0-выход\n1-создать\n2-прочитать\n3-копировать\n4-удалить\n")
        if command == "0":
            break
        elif command == "1":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == "2":
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            for i, item in enumerate(read_file(file_name)):
                print(i + 1, item, "\n")
            
        elif command == "3":
            index = int(input("Введите номер записи, которую хотите скопировать: "))
            new_file = input("Введите имя файла, куда хотите скопировать: ")
            copy_row(file_name, new_file, index - 1)
            continue
            
        elif command == "4":
            index = int(input("Введите номер записи, которую хотите удалить: "))
            delete_row(file_name, index - 1)
            continue

main()
























