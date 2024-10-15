from random import choice
from string import ascii_letters, digits, punctuation

chars = ascii_letters + digits + punctuation

while True:
    try:
        length = int(input('\nPassword length (At least 15 is recommended) >>> '))
        [print(choice(chars), end='') for _ in range(length)]

    except ValueError:
        print('Enter a number!')
