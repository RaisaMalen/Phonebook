from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print ("Неправильный ввод")
        var = int (input('Введите число '))
    
    if var == 1:
        with open ('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write (f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open ('data_second_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write (f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print ('Вывожу данные из 1 файла: \n')
    with open ('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len (data_first)):
            if data_first [i] == '\n' or i == len (data_first) - 1:
                data_first_list.append (''.join (data_first [j:i+1]))
                j = i
        print (''.join (data_first_list))


    print ('Вывожу данные из 2 файла: \n')
    with open ('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print (*data_second)

def change_data ():
    print ('Выберите файл, куда хотите внести зменения: \n 1 - data_first_variant.csv \n 2 - data_second_variant.csv')
    choosing_file = int (input ('Введите номер выбранного файла: '))
    
    while choosing_file != 1 and choosing_file != 2:
        print ("Неправильный ввод. ")
        choosing_file = int (input('Выбирите пункт меню из имеющихся: '))

    search_data = input ('Введите данные, которые необходимо заменить новыми данными: ')
    replace_data = input ('Введите новые данные: ')
    if choosing_file == 1:
        with open ('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            for search_data in file:
                data = file.readlines ()
                data = data.replace (search_data, replace_data)
                with open ('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
                    file.writelines (data)
            else:
                print ('Таких данных нет, введите другие.')
                change_data ()
    elif choosing_file == 2:
        with open ('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            for search_data in file:
                data = file.readlines ()
                data = data.replace (search_data, replace_data)
                with open ('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
                    file.writelines (data)
            else:
                print ('Таких данных нет, введите другие.')
                change_data ()
print ("Данные изменены")

def delete_data ():
    print ('Выберите файл, где хотите удалить данные: \n 1 - data_first_variant.csv \n 2 - data_second_variant.csv')
    choosing_file = int (input ('Введите номер выбранного файла: '))
    
    while choosing_file != 1 and choosing_file != 2:
        print ("Неправильный ввод.")
        choosing_file = int (input ('Выбирите пункт меню из имеющихся: '))
        
    if choosing_file == 1:
        data_for_delete = input ('Введите данные, которые необходимо удалить: ')
        with open ('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            data = file.readlines ()
            with open ('data_first_variant.csv','w', encoding = 'utf-8') as file:
                    for line in data:
                        if line.strip('\n') != data_for_delete:
                            file.write (line)
    elif choosing_file == 2:
        data_for_delete = input ('Введите данные, которые необходимо удалить: ')
        with open ('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            data = file.readlines ()
            with open ('data_second_variant.csv','w', encoding = 'utf-8') as file: 
                for line in data:
                    if line.strip('\n') != data_for_delete:
                        file.write (line)
print ("Данные удалены")