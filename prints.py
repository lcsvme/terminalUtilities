def info():
    """
    Creator: Luan Vieira
    Date: 17/09/2024
    Description: This file contains everything related to prints in the terminal."""

    print(help(info))


# Shows the usage of every print function in Python
print('Hello World'.upper()) # HELLO WORLD
print('Hello World'.lower()) # hello world
print('Hello World'.capitalize()) # Hello world
print('Hello World'.title()) # Hello World
print('Hello World'.swapcase()) # hELLO wORLD
print('Hello World'.center(50)) #                 Hello World
print('Hello World'.center(50, '-')) # ----------------Hello World-----------------
print('Hello World'.ljust(50)) # Hello World
print('Hello World'.ljust(50, '-')) # Hello World-------------------------------
print('Hello World'.rjust(50)) #                                     Hello World
print('Hello World'.rjust(50, '-')) # -------------------------------Hello World
print('Hello World'.zfill(50)) #000000000000000000000000000000000000Hello World
print('Hello World'.count('l')) # 3
print('Hello World'.count('l', 0, 5)) # 2
print('Hello World'.find('l')) # 2
print('Hello World'.find('x')) # -1
print('Hello World'.rfind('l')) # 9
print('Hello World'.rfind('x')) # -1
print('Hello World'.index('l')) # 2
print('Hello World'.index('x')) # ValueError: substring not found
print('Hello World'.rindex('l')) # 9
print('Hello World'.rindex('x')) # ValueError: substring not found
print('Hello World'.startswith('Hello')) # True
print('Hello World'.startswith('World')) # False
print('Hello World'.endswith('World')) # True
print('Hello World'.endswith('Hello')) # False
print('Hello World'.replace('World', 'Python')) # Hello Python
print('Hello World'.split()) # ['Hello', 'World']
print('Hello World'.split('o')) # ['Hell', ' W', 'rld']
print('Hello World'.split('o', 1)) # ['Hell', ' World']
print('Hello World'.rsplit()) # ['Hello', 'World']
print('Hello World'.rsplit('o')) # ['Hell', ' W', 'rld']
print('Hello World'.partition('o')) # ('Hell', 'o', ' World')
print('Hello World'.rpartition('o')) # ('Hello W', 'o', 'rld')
print('Hello World'.join(['1', '2', '3'])) # 1Hello World2Hello World3
print(' Hello World '.strip()) # Hello World
print('Hello World'.strip('Hd')) # ello Worl
print('Hello World'.encode()) # b'Hello World'
print(b'Hello World'.decode()) # Hello World
print('Hello World'.isalnum()) # False
print('HelloWorld'.isalnum()) # True
print('Hello World'.isalpha()) # False
print('HelloWorld'.isalpha()) # True
print('Hello World'.isascii()) # True
print('Olá'.isascii()) # False
print('Hello World'.isdecimal()) # False
print('123'.isdecimal()) # True
print('Hello World'.isdigit()) # False
print('123'.isdigit()) # True
print('Hello World'.isidentifier()) # False
print('HelloWorld'.isidentifier()) # True
print('Hello World'.islower()) # False
print('hello world'.islower()) # True
print('Hello World'.isnumeric()) # False
print('123'.isnumeric()) # True
print('Hello World'.isprintable()) # True
print('\n'.isprintable()) # False
print('Hello World'.isspace()) # False
print(' '.isspace()) # True
print('Hello World'.istitle()) # False
print('Hello World'.title().istitle()) # True
print('Hello World'.isupper()) # False
print('HELLO WORLD'.isupper()) # True