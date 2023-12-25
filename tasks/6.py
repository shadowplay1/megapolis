'''
6. Прочитать csv документ, заменить ФИО на Фамилия инициалы; пример: Иванов Георгий Сидорович > Иванов Г.С,
'''

'''
Структура данных в таблице (используем `students.csv`):
    - id (int) - ID записи в таблице (index = 0)
    - fio (str) - ФИО ученика (index = 1)
    - project_id (int) - ID проекта (index = 2)
    - class (str) - класс + буква класса, в котором учится ученик (index = 3)
    - student_id (int) - ID ученика (index = 4)
    - score (int) - оценка ученика за проект (index = 5)
'''

from typing import Union

# Столбец с ФИО ученика находится на 1 индексе в списке данных таблицы
n: int = 1


file: list[str] = open('data/students.csv', encoding='UTF-8').readlines()
data: list[list[Union[str, int]]] = []

for line in file:
    line: str = line.replace('\n', '')
    splitted: list[str] = line.split(',')

    for i in range(len(splitted)):
        if splitted[i].isdigit():
            splitted[i] = int(splitted[i])

        if splitted[i] == 'None':
            splitted[i] = 0

    data.append(splitted)


data = data[1:]

for i in range(len(data)):
    # переводим список ['фамилия', 'имя', 'отчество'] в кортеж, чтобы из него 
    # можно было в отдельных переменных достать фамилию, имя и отчество
    f_, i_, o_ = tuple(data[i][n].split(' ')) 
    
    data[i][n] = f'{f_} {i_[0]}.{o_[0]}.'


# так как в условии не сказано, что нужно сделать с новыми данными, мы просто выведем
# первые 10 строк изменённой таблицы, по аналогии с предыдущими заданиями

for item in data[:10]:
    print(item)
