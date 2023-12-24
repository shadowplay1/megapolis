'''
2. Прочитать csv документ, преобразовать все «числовые» значения в числа и вывести первые 10 строк на экран
'''

'''
Структура данных в таблице:
    - id (int) - ID записи в таблице (index = 0)
    - fio (str) - ФИО ученика (index = 1)
    - project_id (int) - ID проекта (index = 2)
    - class (str) - класс + буква класса, в котором учится ученик (index = 3)
    - student_id (int) - ID ученика (index = 4)
    - score (int) - оценка ученика за поект (index = 5)
'''

from typing import Union


file: list[str] = open('data/students.csv', encoding='UTF-8').readlines()
data: list[list[Union[str, int]]] = []


for line in file:
    line = line.replace('\n', '')
    splitted: list[str] = line.split(',')

    for i in range(len(splitted)):
        if splitted[i].isdigit():
            splitted[i] = int(splitted[i])

    data.append(splitted)


for item in data[1:11]:
    print(item)
