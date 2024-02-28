from logger import input_data, print_data, change_data, delete_data


def interface():
    print ("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n МЕНЮ: \n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных  \n 4 - удаление данных")
    command = int (input('Выберите пункт меню: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print ("Неправильный ввод. ")
        command = int (input('Выбирите пункт меню из имеющихся: '))

    if command == 1:
        input_data ()
    elif command == 2:
        print_data ()
    elif command == 3:
        change_data ()
    elif command == 4:
        delete_data ()