'''
1. Прочитать csv документ и вывести первые 10 строк на экран
'''

file: list[str] = open('data/students.csv', encoding='UTF-8').readlines() 

for item in file[1:11]:
    print(item)

