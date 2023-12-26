'''
8. Прочитать csv документ, выводить строки по критерию поиска; который обозначил учитель до тех пока, пока не будет введено стоп слово (поиск осуществить линейно)
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

# Пусть критерие поиска будет ID проекта - столбец с индексом 2
n: int = 2


from typing import Union, Optional

file: list[str] = open('data/students.csv', encoding='UTF-8').readlines()
data: list[list[Union[str, int]]] = []


for line in file:
    line: str = line.replace('\n', '')
    splitted: list[str] = line.split(',')

    for i in range(len(splitted)):
        if splitted[i].isdigit():
            splitted[i] = int(splitted[i])

    data.append(splitted)


data = data[1:]


def find_project(project_id: int) -> Optional[list[Union[str, int]]]:
    '''Находит проект по указанному ID.

    Описание аргументов:
    - project_id (int) - ID, по которому необходимо найти проект'''
    for i in range(len(data)):
        if data[i][n] == project_id:
            return data[i]

    return None


while True:
    project_id: Union[str, int] = input('Введите ID проекта или слово "СТОП", чтобы закончить: ')

    if project_id.lower() == 'стоп': # переводим все символы из ввода в строчные буквы
        break
    

    if not project_id.isdigit():
        print('Введён некорректный ID проекта.')
    
    else:
        project_id = int(project_id)
        index: int = 0

        project = find_project(project_id)

        if project: 
            fio = project[1] # столбец с ФИО находится на 1 индексе в списке из данных таблицы
            score = project[5] # столбец с оценкой за проект находится на 5 (последнем) индексе в списке из данных таблицы
 
            print(f'Проект №{project_id}, делал: {fio}, он(а): получил(а) оценку: {score}.')
        else:
            print('Проект не найден.')
