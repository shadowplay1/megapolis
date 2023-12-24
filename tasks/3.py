'''
3. Прочитать csv документ, преобразовать все «None» значения в 0 и вывести первые 10 строк на экран
'''

'''
Структура данных в таблице (используем `students_with_none.csv`):
    - id (int) - ID записи в таблице (index = 0)
    - fio (str) - ФИО ученика (index = 1)
    - project_id (int) - ID проекта (index = 2)
    - class (str) - класс + буква класса, в котором учится ученик (index = 3)
    - student_id (int) - ID ученика (index = 4)
    - score (int | None) - оценка ученика за проект (index = 5)
'''

from typing import Union, Optional

file: list[str] = open('data/students_with_none.csv', encoding='UTF-8').readlines()
data: list[list[Union[str, int, Optional[int]]]] = []

for line in file:
    line: str = line.replace('\n', '')
    splitted: list[str] = line.split(',')

    for i in range(len(splitted)):
        if splitted[i].isdigit():
            splitted[i] = int(splitted[i])

        if splitted[i] == 'None':
            splitted[i] = 0

    data.append(splitted)


for item in data[1:11]:
    print(item)
