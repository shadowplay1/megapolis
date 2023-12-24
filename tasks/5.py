'''
5. Прочитать csv документ, заменить все значения столбца n на среднее арифметическое этого же столбца, вывести на экран первые 10 значений и сохранить данные в новом файле csv
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

# Примем столбец n за столбец с индексом 5 - столбец с оценками за проект
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


head: str = file[0]
data = data[1:]

sum_of_values: int = 0
avg_value: int = 0


for item in data:
    sum_of_values += item[n]


avg_value = sum_of_values / len(data)


for i in range(len(data)):
    data[i][n] = avg_value


new_file = open('data/students_task_5.csv', 'a') # создаём в папке 'data' новый csv-файл и открываем его для чтения
new_file_content = head # мы не добавляем сюда символ переноса строки \n, так как он уже содержится в 'head'


for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = str(data[i][j])

    new_file_content += ','.join(data[i]) + '\n'

new_file.write(new_file_content) # записываем наши обновлённые данные в раннее созданный csv-файл


for item in data[:10]:
    print(item)
