from data_createe import *

def input_data():
    name = name_data()
    lastname = lastname_data()
    phone = phone_data()

    with open("tel_spravochnik.txt", "a", encoding="utf-8") as file:
        file.write(f"{lastname} {name} {phone}; \n\n")

def print_data():
    with open("tel_spravochnik.txt", "r", encoding="utf-8") as data:
        spravochnick = data.read()
        print(spravochnick)
    return spravochnick 


def searching():
    lookfor = input("кого найти? ")
    with open("tel_spravochnik.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)
                print()

def load():
    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("tel_spravochnik.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)

def delete():
    what_delete = input("Кого нужно удалить? ")
    with open("tel_spravochnik.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("tel_spravochnik.txt", "w", encoding="utf-8") as data1:
            for line in lines:
                if what_delete not in line:
                    data1.write(line)
                else:
                    print(line)
                    ask = input("Эту запись нужно удалить? (y/n)")
                    if ask == "n":
                        data1.write
    return data1

def change():
    what_delete = input("Кого нужно изменить? ")
    with open("tel_spravochnik.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("tel_spravochnik.txt", "w", encoding="utf-8") as data1:
            for line in lines:
                if what_delete not in line:
                    data1.write(line)
                else:
                    print(line)
                    ask = input("Эту запись нужно изменить? (y/n)")
                    if ask == "n":
                        data1.write
                    else:
                        new_data = input("Введите корректные фамилию имя и телефон: ")
                        data1.write(new_data)
    return data1                    



input_data()
input_data()
print_data()
delete()
change()


