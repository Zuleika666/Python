from loggerr import *

user = input("""
Выберите цифру:
1 - запись
2 -  поиск
3 - вывод на экран
4 - импорт в файл
5 - удаление
6 - изменение
""")
if user == "1":
    input_data()
elif user == "2":
    searching()
elif user == "3":
    print_data()
elif user == "4":
    load()
elif user == "5":
    delete()
elif user == "6":
    change()    