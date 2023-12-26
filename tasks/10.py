'''
10. Написать функцию генерации хеш-таблицы по заданным правилам
'''

def generate_hash(s: str) -> int:
    '''Генерирует хеш-число по заданной строке.

    Описание аргументов:
    - s (str) - Строка, по которой необходимо получить хеш-число.
    '''
    p: int = 67
    m: int = 1e9 + 9

    n: int = len(s)
    hash_value: int = 0


    for i in range(n):
        hash_value += (ord(s[i]) * (p ** i))


    hash_value %= m    
    return hash_value


s: str = 'test12345'
hash_number: int = generate_hash(s)

print(hash_number)
