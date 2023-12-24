'''
1. Прочитать csv документ и вывести первые 10 строк на экран
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

file: list[str] = open('data/students.csv', encoding='UTF-8').readlines() 


for item in file[1:11]:
    print(item)

