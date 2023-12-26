'''
9. Написать функцию генерации пароля по заданным правилам
'''

import string
import random


def generate_password() -> str:
    '''Генерирует пароль, состоящий из 8 символов, включающий в себя заглавные и строчные буквы латинского алфавита, а так же цифры.'''
    password_length: int = 8

    chars: str = string.ascii_letters + string.digits
    generated_password: str = ''.join(random.choice(chars) for i in range(password_length))

    return generated_password


password: str = generate_password()
print(password)
