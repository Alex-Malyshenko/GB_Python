"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

import csv

def display_all_records():
    "Выводит содержимое файла построчно в формате Фамилия/Имя/Номер телефона/Комментарий"
    for row in reader:
        print(f'Фамилия: {row[0]} Имя: {row[1]} Номер телефона: {row[2]} Комментарий: {row[3]}')

def find_last_name(reader):
    last_name = input('Введите фамилию: ')
    for elem in filter(lambda x: x[0] == last_name, reader):
        print(f'Фамилия: {elem[0]}\nИмя: {elem[1]}\nНомер телефона: {elem[2]}\nКомментарий: {elem[3]}\n')


def find_phone_number(reader):
    phone = input('Введите номер телефона: ')
    for elem in filter(lambda x: x[2] == phone, reader):
        print(f'Фамилия: {elem[0]}\nИмя: {elem[1]}\nНомер телефона: {elem[2]}\nКомментарий: {elem[3]}\n')


def add_abonent():
    with open('phonebook.csv', 'a', encoding='utf-8', newline='') as out_file:
        info = input('Введите данные абонента: ').split()
        csv.writer(out_file).writerow(info)

def save_phonebook():
    with open('phonebook.txt', 'w') as my_output_file:
        with open('phonebook.csv', 'r') as my_input_file:
            [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
        print("Файл сохранён!")

print("""\nВыберите необходимое действие:
          1. Отобразить весь справочник
          2. Найти абонента по фамилии
          3. Найти абонента по номеру телефона
          4. Добавить абонента в справочник
          5. Сохранить справочник в текстовом формате
          6. Закончить работу""")

for elem in iter(input, '6'):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        if elem == '1':
            display_all_records()

        elif elem == '2':
            find_last_name(reader)

        elif elem == '3':
            find_phone_number(reader)

        elif elem == '4':
            add_abonent()

        elif elem == '5':
            save_phonebook()
