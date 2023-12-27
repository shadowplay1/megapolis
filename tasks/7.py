'''
7. Прочитать csv документ, отсортировать данные с помощью сортировки слиянием, сохранить данные в новый файл csv
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

# Пусть критерием, по которому будет выполняться сортировка - это оценки за проект (столбец с индексом 5)
n: int = 5


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


head = file[0]
data = data[1:]


def merge_sort(data: list[list[Union[str, int]]]) -> list[list[Union[str, int]]]:
    '''Выполняет сортировку таблицы по оценкам от большей к меньшей, используя алгоритм сортировки слиянием, и возвращает отсортированный результат.

    Описание аргументов:
    - data (list[list[Union[str, int]]]) - список с данными (таблица с проектами), которую надо отсортировать.
    '''
    if len(data) > 1:
        mid: int = len(data) // 2

        left: list[list[Union[str, int]]] = data[:mid] 
        right: list[list[Union[str, int]]] = data[mid:]

        merge_sort(left) 
        merge_sort(right) 

        i = j = k = 0


        while i < len(left) and j < len(right): 
            if left[i][n] > right[j][n]: 
                data[k] = left[i] 
                i += 1
            else: 
                data[k] = right[j] 
                j += 1

            k += 1


        while i < len(left): 
            data[k] = left[i]

            i += 1
            k += 1


        while j < len(right): 
            data[k] = right[j]

            j += 1
            k += 1


    return data



sorted_data = merge_sort(data)

new_file = open('data/students_sorted_task_7.csv', 'a') # создаём в папке 'data' новый csv-файл и открываем его для чтения
new_file_content = head # мы не добавляем сюда символ переноса строки \n, так как он уже содержится в конце 'head'


for i in range(len(sorted_data)):
    for j in range(len(sorted_data[i])):
        sorted_data[i][j] = str(sorted_data[i][j])

    new_file_content += ','.join(sorted_data[i]) + '\n'

new_file.write(new_file_content) # записываем обновлённые данные в раннее созданный csv-файл


for item in sorted_data[:10]:
    print(item) # выводим первые 10 строк отсортированной таблицы, чтобы понять, что всё отработало как надо
